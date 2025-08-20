#!/usr/bin/env python3
"""
Microsoft Style Guide FastMCP Server

A Model Context Protocol server that provides access to Microsoft Style Guide content.
This server allows clients to search, retrieve, and get guidance from the comprehensive
Microsoft Style Guide documentation.
"""

import asyncio
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

from fastmcp import FastMCP
from pydantic import BaseModel


class StyleGuideServer:
    """Microsoft Style Guide MCP Server implementation."""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.mcp = FastMCP("Microsoft Style Guide")
        self._register_tools()
    
    def _register_tools(self):
        """Register all available tools with the MCP server."""
        
        @self.mcp.tool()
        def search_style_guide(
            query: str,
            category: Optional[str] = None,
            limit: int = 10
        ) -> Dict[str, Any]:
            """
            Search the Microsoft Style Guide for content matching the query.
            
            Args:
                query: Search term or phrase
                category: Optional category filter (e.g., 'a-z', 'punctuation', 'capitalization')
                limit: Maximum number of results to return (default: 10)
            
            Returns:
                Dictionary containing search results with titles, paths, and content snippets
            """
            results = []
            query_lower = query.lower()
            
            # Define search directories based on category
            search_dirs = []
            if category:
                if category == "a-z":
                    search_dirs = [
                        self.base_path / "styleguide" / "a-z-word-list-term-collections",
                        self.base_path / "product-style-guide-msft-internal" / "a_z_names_terms"
                    ]
                elif category == "punctuation":
                    search_dirs = [
                        self.base_path / "product-style-guide-msft-internal" / "punctuation"
                    ]
                elif category == "capitalization":
                    search_dirs = [
                        self.base_path / "product-style-guide-msft-internal" / "capitalization-standards"
                    ]
                else:
                    search_dirs = [self.base_path]
            else:
                search_dirs = [self.base_path]
            
            # Search through markdown files
            for search_dir in search_dirs:
                if not search_dir.exists():
                    continue
                    
                for md_file in search_dir.rglob("*.md"):
                    try:
                        with open(md_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            
                        # Check if query matches in title or content
                        if (query_lower in content.lower() or 
                            query_lower in md_file.name.lower()):
                            
                            # Extract title from frontmatter or filename
                            title = self._extract_title(content, md_file.name)
                            
                            # Extract relevant snippet
                            snippet = self._extract_snippet(content, query_lower)
                            
                            relative_path = str(md_file.relative_to(self.base_path))
                            
                            results.append({
                                "title": title,
                                "path": relative_path,
                                "snippet": snippet,
                                "file_path": str(md_file)
                            })
                            
                    except Exception as e:
                        continue
            
            # Sort by relevance and limit results
            results = sorted(results, key=lambda x: self._calculate_relevance(x, query_lower))
            results = results[:limit]
            
            return {
                "query": query,
                "category": category,
                "total_results": len(results),
                "results": results
            }
        
        @self.mcp.tool()
        def get_style_guide_entry(file_path: str) -> Dict[str, Any]:
            """
            Get the complete content of a specific style guide entry.
            
            Args:
                file_path: Relative path to the markdown file
            
            Returns:
                Dictionary containing the full content and metadata of the entry
            """
            full_path = self.base_path / file_path
            
            if not full_path.exists():
                return {
                    "error": f"File not found: {file_path}",
                    "available": False
                }
            
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Parse frontmatter and content
                frontmatter, body = self._parse_frontmatter(content)
                
                return {
                    "path": file_path,
                    "title": frontmatter.get("title", self._extract_title(content, full_path.name)),
                    "description": frontmatter.get("description", ""),
                    "frontmatter": frontmatter,
                    "content": body,
                    "available": True
                }
                
            except Exception as e:
                return {
                    "error": f"Error reading file: {str(e)}",
                    "path": file_path,
                    "available": False
                }
        
        @self.mcp.tool()
        def get_term_guidance(term: str) -> Dict[str, Any]:
            """
            Get specific guidance for a term or phrase from the style guide.
            
            Args:
                term: The term or phrase to look up
            
            Returns:
                Dictionary containing guidance, examples, and related information
            """
            # Search for the term in various directories
            term_lower = term.lower().replace(" ", "-").replace("/", "-")
            possible_paths = []
            
            # Check common locations for terms
            possible_dirs = [
                self.base_path / "styleguide" / "a-z-word-list-term-collections",
                self.base_path / "product-style-guide-msft-internal" / "a_z_names_terms",
            ]
            
            for base_dir in possible_dirs:
                if not base_dir.exists():
                    continue
                    
                # Try direct file match
                for md_file in base_dir.rglob("*.md"):
                    if (term_lower in md_file.name.lower() or 
                        md_file.stem.lower() == term_lower):
                        possible_paths.append(md_file)
            
            if not possible_paths:
                # Fallback: search content
                search_results = search_style_guide(term, limit=5)
                if search_results["results"]:
                    best_match = search_results["results"][0]
                    return get_style_guide_entry(best_match["path"])
                else:
                    return {
                        "term": term,
                        "found": False,
                        "message": f"No specific guidance found for '{term}'. Try searching with a broader query."
                    }
            
            # Use the best match
            best_file = possible_paths[0]
            relative_path = str(best_file.relative_to(self.base_path))
            
            return get_style_guide_entry(relative_path)
        
        @self.mcp.tool()
        def list_categories() -> Dict[str, Any]:
            """
            List all available categories and sections in the style guide.
            
            Returns:
                Dictionary containing organized categories and their descriptions
            """
            categories = {}
            
            # Main style guide sections
            main_sections = [
                ("styleguide", "Public Microsoft Style Guide"),
                ("product-style-guide-msft-internal", "Internal Product Style Guide"),
                ("writing-style-guide-msft-internal", "Internal Writing Style Guide")
            ]
            
            for section_dir, description in main_sections:
                section_path = self.base_path / section_dir
                if section_path.exists():
                    categories[section_dir] = {
                        "description": description,
                        "subsections": self._get_subsections(section_path)
                    }
            
            return {
                "categories": categories,
                "total_sections": len(categories)
            }
        
        @self.mcp.tool()
        def get_writing_guidance(topic: str) -> Dict[str, Any]:
            """
            Get specific writing guidance on topics like capitalization, punctuation, etc.
            
            Args:
                topic: Writing topic (e.g., 'capitalization', 'punctuation', 'bias-free')
            
            Returns:
                Dictionary containing relevant writing guidance and examples
            """
            topic_lower = topic.lower()
            guidance_files = []
            
            # Search in includes directory
            includes_dir = self.base_path / "includes"
            if includes_dir.exists():
                for file in includes_dir.glob("*.md"):
                    if topic_lower in file.name.lower():
                        guidance_files.append(file)
            
            # Search in style guide sections
            style_dirs = [
                self.base_path / "product-style-guide-msft-internal",
                self.base_path / "styleguide"
            ]
            
            for style_dir in style_dirs:
                if not style_dir.exists():
                    continue
                    
                for file in style_dir.rglob("*.md"):
                    if topic_lower in file.name.lower() or topic_lower in str(file.parent).lower():
                        guidance_files.append(file)
            
            if not guidance_files:
                return {
                    "topic": topic,
                    "found": False,
                    "message": f"No specific guidance found for topic '{topic}'"
                }
            
            # Get content from the most relevant file
            best_file = guidance_files[0]
            relative_path = str(best_file.relative_to(self.base_path))
            
            return get_style_guide_entry(relative_path)
    
    def _extract_title(self, content: str, filename: str) -> str:
        """Extract title from markdown content or filename."""
        # Try to extract from frontmatter first
        if content.startswith("---"):
            try:
                lines = content.split('\n')
                for line in lines[1:]:
                    if line.startswith("title:"):
                        return line.replace("title:", "").strip().strip('"\'')
                    if line == "---":
                        break
            except:
                pass
        
        # Try to extract from first heading
        for line in content.split('\n'):
            if line.startswith('# '):
                return line[2:].strip()
        
        # Fall back to filename
        return filename.replace(".md", "").replace("-", " ").title()
    
    def _extract_snippet(self, content: str, query: str, max_length: int = 200) -> str:
        """Extract a relevant snippet from content based on query."""
        lines = content.split('\n')
        
        # Find the most relevant line
        best_line = ""
        best_score = 0
        
        for line in lines:
            if query in line.lower():
                # Count query occurrences and line length relevance
                score = line.lower().count(query) + (1 if len(line) > 20 else 0)
                if score > best_score:
                    best_score = score
                    best_line = line.strip()
        
        if not best_line:
            # Take first non-empty line as fallback
            for line in lines:
                if line.strip() and not line.startswith('#') and not line.startswith('---'):
                    best_line = line.strip()
                    break
        
        # Truncate if too long
        if len(best_line) > max_length:
            best_line = best_line[:max_length-3] + "..."
        
        return best_line
    
    def _calculate_relevance(self, result: Dict[str, Any], query: str) -> float:
        """Calculate relevance score for sorting results."""
        score = 0
        
        # Title match is most important
        if query in result["title"].lower():
            score += 10
        
        # File name match
        if query in result["path"].lower():
            score += 5
        
        # Snippet relevance
        snippet_matches = result["snippet"].lower().count(query)
        score += snippet_matches * 2
        
        return -score  # Negative for descending sort
    
    def _parse_frontmatter(self, content: str) -> tuple[Dict[str, Any], str]:
        """Parse YAML frontmatter from markdown content."""
        frontmatter = {}
        body = content
        
        if content.startswith("---"):
            try:
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    fm_text = parts[1].strip()
                    body = parts[2].strip()
                    
                    # Simple YAML parsing for common fields
                    for line in fm_text.split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            frontmatter[key.strip()] = value.strip().strip('"\'')
            except:
                pass
        
        return frontmatter, body
    
    def _get_subsections(self, path: Path) -> List[str]:
        """Get list of subsections in a directory."""
        subsections = []
        
        for item in path.iterdir():
            if item.is_dir():
                subsections.append(item.name)
        
        return sorted(subsections)
    
    def run(self):
        """Run the FastMCP server."""
        self.mcp.run()


def main():
    """Main entry point."""
    # Get the base path of the style guide
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Create and run the server
    server = StyleGuideServer(base_path)
    server.run()


if __name__ == "__main__":
    main()
