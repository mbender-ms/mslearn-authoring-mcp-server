#!/usr/bin/env python3

"""
Microsoft Learn Content Authoring MCP Server

This MCP server provides tools for authoring and editing Microsoft Learn content,
with a focus on the Microsoft Writing Style Guide and related documentation.
"""

import asyncio
import json
import re
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)
import mcp.types as types


class MSLearnAuthoringServer:
    def __init__(self):
        self.server = Server("mslearn-authoring-server")
        self.base_url = "https://learn.microsoft.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Register handlers
        self.setup_handlers()

    def setup_handlers(self):
        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            """List available tools for Microsoft Learn content authoring."""
            return [
                Tool(
                    name="fetch_style_guide_content",
                    description="Fetch content from Microsoft Learn Style Guide pages for authoring reference",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "path": {
                                "type": "string",
                                "description": "The path to the style guide page (e.g., '/en-us/style-guide/welcome/' or '/en-us/style-guide/bias-free-communication')",
                                "default": "/en-us/style-guide/welcome/"
                            },
                            "format": {
                                "type": "string",
                                "enum": ["markdown", "html", "text"],
                                "description": "Output format for the content",
                                "default": "markdown"
                            }
                        },
                        "required": ["path"]
                    }
                ),
                Tool(
                    name="analyze_style_compliance",
                    description="Analyze text content for Microsoft Writing Style Guide compliance",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "content": {
                                "type": "string",
                                "description": "The content to analyze for style guide compliance"
                            },
                            "focus_areas": {
                                "type": "array",
                                "items": {
                                    "type": "string",
                                    "enum": ["voice_tone", "bias_free", "terminology", "formatting", "accessibility"]
                                },
                                "description": "Specific areas to focus the analysis on",
                                "default": ["voice_tone", "bias_free", "terminology"]
                            }
                        },
                        "required": ["content"]
                    }
                ),
                Tool(
                    name="extract_style_guide_sections",
                    description="Extract and list all sections and navigation from the Microsoft Style Guide",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "include_subsections": {
                                "type": "boolean",
                                "description": "Whether to include subsections in the extraction",
                                "default": True
                            }
                        }
                    }
                ),
                Tool(
                    name="search_style_guide",
                    description="Search for specific topics within the Microsoft Writing Style Guide",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search query for finding relevant style guide content"
                            },
                            "max_results": {
                                "type": "number",
                                "description": "Maximum number of results to return",
                                "default": 5
                            }
                        },
                        "required": ["query"]
                    }
                ),
                Tool(
                    name="generate_content_outline",
                    description="Generate a content outline following Microsoft style guide principles",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "topic": {
                                "type": "string",
                                "description": "The main topic for the content outline"
                            },
                            "content_type": {
                                "type": "string",
                                "enum": ["tutorial", "concept", "reference", "how-to", "overview"],
                                "description": "Type of content to create an outline for",
                                "default": "tutorial"
                            },
                            "target_audience": {
                                "type": "string",
                                "enum": ["beginner", "intermediate", "advanced", "mixed"],
                                "description": "Target audience level",
                                "default": "mixed"
                            }
                        },
                        "required": ["topic"]
                    }
                )
            ]

        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
            """Handle tool execution."""
            try:
                if name == "fetch_style_guide_content":
                    return await self.fetch_style_guide_content(arguments)
                elif name == "analyze_style_compliance":
                    return await self.analyze_style_compliance(arguments)
                elif name == "extract_style_guide_sections":
                    return await self.extract_style_guide_sections(arguments)
                elif name == "search_style_guide":
                    return await self.search_style_guide(arguments)
                elif name == "generate_content_outline":
                    return await self.generate_content_outline(arguments)
                else:
                    raise ValueError(f"Unknown tool: {name}")
            except Exception as e:
                return [types.TextContent(
                    type="text",
                    text=f"Error executing tool {name}: {str(e)}"
                )]

    async def fetch_style_guide_content(self, args: Dict[str, Any]) -> List[types.TextContent]:
        """Fetch content from Microsoft Learn Style Guide pages."""
        path = args.get("path", "/en-us/style-guide/welcome/")
        format_type = args.get("format", "markdown")
        
        url = urljoin(self.base_url, path)
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove navigation, ads, and other non-content elements
            for element in soup.find_all(['nav', 'script', 'style', 'aside', 'footer']):
                element.decompose()
            
            # Remove elements with specific classes that are typically navigation/ads
            for class_name in ['breadcrumb', 'feedback', 'page-actions', 'site-header', 'site-footer']:
                for element in soup.find_all(class_=class_name):
                    element.decompose()
            
            # Extract the main content area
            main_content = None
            for selector in ['.content', '.main-content', 'article', '.markdown-body', 'main']:
                main_content = soup.select_one(selector)
                if main_content:
                    break
            
            if not main_content:
                main_content = soup.find('body') or soup
            
            # Format content based on requested format
            if format_type == "markdown":
                formatted_content = md(str(main_content), heading_style="atx")
            elif format_type == "html":
                formatted_content = str(main_content)
            elif format_type == "text":
                formatted_content = main_content.get_text(strip=True)
            else:
                formatted_content = md(str(main_content), heading_style="atx")
            
            title = soup.find('title')
            title_text = title.get_text(strip=True) if title else "Untitled"
            
            result = {
                "url": url,
                "title": title_text,
                "format": format_type,
                "content": formatted_content,
                "extracted_at": datetime.now().isoformat()
            }
            
            return [types.TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
            
        except requests.RequestException as e:
            return [types.TextContent(
                type="text",
                text=f"Error fetching content from {url}: {str(e)}"
            )]
        except Exception as e:
            return [types.TextContent(
                type="text",
                text=f"Error processing content: {str(e)}"
            )]

    async def analyze_style_compliance(self, args: Dict[str, Any]) -> List[types.TextContent]:
        """Analyze content for Microsoft Writing Style Guide compliance."""
        content = args.get("content", "")
        focus_areas = args.get("focus_areas", ["voice_tone", "bias_free", "terminology"])
        
        analysis_results = {
            "overall_score": 0,
            "focus_areas": {},
            "suggestions": [],
            "compliant_elements": []
        }
        
        # Voice and tone analysis
        if "voice_tone" in focus_areas:
            voice_analysis = self.analyze_voice_and_tone(content)
            analysis_results["focus_areas"]["voice_tone"] = voice_analysis
        
        # Bias-free communication analysis
        if "bias_free" in focus_areas:
            bias_analysis = self.analyze_bias_free(content)
            analysis_results["focus_areas"]["bias_free"] = bias_analysis
        
        # Terminology analysis
        if "terminology" in focus_areas:
            term_analysis = self.analyze_terminology(content)
            analysis_results["focus_areas"]["terminology"] = term_analysis
        
        # Calculate overall score
        scores = [area.get("score", 0) for area in analysis_results["focus_areas"].values()]
        if scores:
            analysis_results["overall_score"] = sum(scores) / len(scores)
        
        return [types.TextContent(
            type="text",
            text=json.dumps(analysis_results, indent=2)
        )]

    def analyze_voice_and_tone(self, content: str) -> Dict[str, Any]:
        """Analyze voice and tone compliance."""
        issues = []
        strengths = []
        
        # Check for Microsoft's warm and conversational tone
        conversational_words = ["you", "your", "we", "our", "let's"]
        conversational_count = sum(
            len(re.findall(rf'\b{word}\b', content.lower())) 
            for word in conversational_words
        )
        
        if conversational_count > 0:
            strengths.append("Uses conversational tone with direct address")
        else:
            issues.append("Consider using more conversational language (you, your, we)")
        
        # Check for overly complex sentences
        sentences = re.split(r'[.!?]+', content)
        long_sentences = [s for s in sentences if len(s.split()) > 25]
        
        if long_sentences:
            issues.append(f"{len(long_sentences)} sentences are over 25 words - consider breaking them up")
        
        # Check for passive voice
        passive_indicators = ["is being", "was being", "been", "be done"]
        passive_count = sum(
            len(re.findall(indicator, content.lower())) 
            for indicator in passive_indicators
        )
        
        if passive_count > len(sentences) * 0.2:
            issues.append("High use of passive voice - consider using active voice more frequently")
        
        return {
            "score": max(0, 10 - len(issues) * 2),
            "issues": issues,
            "strengths": strengths
        }

    def analyze_bias_free(self, content: str) -> Dict[str, Any]:
        """Analyze bias-free communication compliance."""
        issues = []
        strengths = []
        
        # Check for potentially biased terms
        biased_terms = [
            "guys", "mankind", "manpower", "blacklist", "whitelist", "master/slave",
            "crazy", "insane", "stupid", "dumb", "lame"
        ]
        
        for term in biased_terms:
            if term.lower() in content.lower():
                issues.append(f'Consider replacing potentially biased term: "{term}"')
        
        # Check for inclusive language
        inclusive_terms = ["everyone", "people", "users", "individuals"]
        inclusive_count = sum(
            len(re.findall(rf'\b{term}\b', content.lower())) 
            for term in inclusive_terms
        )
        
        if inclusive_count > 0:
            strengths.append("Uses inclusive language")
        
        return {
            "score": max(0, 10 - len(issues) * 3),
            "issues": issues,
            "strengths": strengths
        }

    def analyze_terminology(self, content: str) -> Dict[str, Any]:
        """Analyze Microsoft terminology compliance."""
        issues = []
        strengths = []
        
        # Check for consistent Microsoft terminology
        microsoft_terms = {
            "app": ["application", "program"],
            "sign in": ["login", "log in"],
            "email": ["e-mail"],
            "website": ["web site"],
            "internet": ["Internet"]
        }
        
        for preferred, alternatives in microsoft_terms.items():
            for alt in alternatives:
                if alt.lower() in content.lower():
                    issues.append(f'Use "{preferred}" instead of "{alt}"')
            
            if preferred.lower() in content.lower():
                strengths.append(f'Correctly uses "{preferred}"')
        
        return {
            "score": max(0, 10 - len(issues) * 2),
            "issues": issues,
            "strengths": strengths
        }

    async def extract_style_guide_sections(self, args: Dict[str, Any]) -> List[types.TextContent]:
        """Extract sections and navigation from the Microsoft Style Guide."""
        include_subsections = args.get("include_subsections", True)
        
        try:
            url = f"{self.base_url}/en-us/style-guide/welcome/"
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            sections = []
            
            # Extract navigation or table of contents
            nav_links = soup.select('nav a, .toc a, .navigation a')
            for link in nav_links:
                href = link.get('href', '')
                text = link.get_text(strip=True)
                
                if href and text and 'style-guide' in href:
                    full_url = urljoin(self.base_url, href) if not href.startswith('http') else href
                    sections.append({
                        "title": text,
                        "url": full_url,
                        "level": self.determine_link_level(link) if include_subsections else 1
                    })
            
            # If no navigation found, extract from page content
            if not sections:
                headings = soup.find_all(['h1', 'h2', 'h3'])
                for heading in headings:
                    text = heading.get_text(strip=True)
                    if text:
                        level = int(heading.name[1])  # h1 -> 1, h2 -> 2, etc.
                        anchor = heading.get('id', text.lower().replace(' ', '-'))
                        sections.append({
                            "title": text,
                            "level": level,
                            "anchor": anchor
                        })
            
            result = {
                "total_sections": len(sections),
                "sections": sections,
                "extracted_at": datetime.now().isoformat()
            }
            
            return [types.TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
            
        except requests.RequestException as e:
            return [types.TextContent(
                type="text",
                text=f"Error extracting sections: {str(e)}"
            )]

    def determine_link_level(self, element) -> int:
        """Determine the nesting level of a navigation link."""
        classes = element.get('class', [])
        if any('level-2' in cls or 'sub' in cls for cls in classes):
            return 2
        if any('level-3' in cls for cls in classes):
            return 3
        return 1

    async def search_style_guide(self, args: Dict[str, Any]) -> List[types.TextContent]:
        """Search for topics within the Microsoft Writing Style Guide."""
        query = args.get("query", "")
        max_results = args.get("max_results", 5)
        
        search_results = []
        
        try:
            # Search through known style guide sections
            common_sections = [
                "/en-us/style-guide/welcome/",
                "/en-us/style-guide/top-10-tips-style-voice",
                "/en-us/style-guide/bias-free-communication",
                "/en-us/style-guide/global-communications/",
                "/en-us/style-guide/accessibility/overview"
            ]
            
            for section in common_sections[:max_results]:
                try:
                    url = f"{self.base_url}{section}"
                    response = self.session.get(url, timeout=30)
                    response.raise_for_status()
                    
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Extract main content
                    main_content = soup.select_one('.content, .main-content, article')
                    if not main_content:
                        main_content = soup.find('body')
                    
                    content_text = main_content.get_text().lower() if main_content else ""
                    
                    if query.lower() in content_text:
                        title = soup.find('title')
                        title_text = title.get_text(strip=True) if title else "Untitled"
                        
                        search_results.append({
                            "url": url,
                            "title": title_text,
                            "relevance": self.calculate_relevance(content_text, query.lower()),
                            "snippet": self.extract_snippet(content_text, query.lower())
                        })
                        
                except requests.RequestException:
                    continue
            
            # Sort by relevance
            search_results.sort(key=lambda x: x["relevance"], reverse=True)
            
            result = {
                "query": query,
                "total_results": len(search_results),
                "results": search_results[:max_results]
            }
            
            return [types.TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
            
        except Exception as e:
            return [types.TextContent(
                type="text",
                text=f"Search failed: {str(e)}"
            )]

    def calculate_relevance(self, content: str, query: str) -> int:
        """Calculate relevance score for search results."""
        words = query.split()
        score = 0
        
        for word in words:
            matches = len(re.findall(word, content, re.IGNORECASE))
            score += matches
        
        return score

    def extract_snippet(self, content: str, query: str) -> str:
        """Extract a relevant snippet from content."""
        sentences = content.split('.')
        query_words = query.split()
        
        for sentence in sentences:
            if any(word in sentence.lower() for word in query_words):
                return sentence.strip()[:200] + "..."
        
        return content[:200] + "..."

    async def generate_content_outline(self, args: Dict[str, Any]) -> List[types.TextContent]:
        """Generate a content outline following Microsoft style guide principles."""
        topic = args.get("topic", "")
        content_type = args.get("content_type", "tutorial")
        target_audience = args.get("target_audience", "mixed")
        
        outlines = {
            "tutorial": [
                "Overview and Prerequisites",
                "Getting Started",
                "Step-by-step Instructions",
                "Examples and Code Samples",
                "Troubleshooting",
                "Next Steps"
            ],
            "concept": [
                "Introduction",
                "Key Concepts",
                "How It Works",
                "Benefits and Use Cases",
                "Best Practices",
                "Related Topics"
            ],
            "reference": [
                "Overview",
                "Syntax and Parameters",
                "Examples",
                "Return Values",
                "Error Codes",
                "See Also"
            ],
            "how-to": [
                "Prerequisites",
                "Step 1: [Action]",
                "Step 2: [Action]",
                "Step 3: [Action]",
                "Verification",
                "Clean up (if applicable)"
            ],
            "overview": [
                "What is [Topic]?",
                "Key Features",
                "Getting Started",
                "Common Scenarios",
                "Architecture",
                "Next Steps"
            ]
        }
        
        base_outline = outlines.get(content_type, outlines["tutorial"])
        
        style_guide_reminders = [
            "Use active voice and conversational tone",
            "Address the reader directly with 'you'",
            "Keep sentences clear and concise",
            "Use inclusive, bias-free language",
            "Follow Microsoft terminology standards",
            "Include accessibility considerations",
            "Provide clear next steps"
        ]
        
        audience_considerations = {
            "beginner": "Include more context and explanations",
            "intermediate": "Balance context with efficiency",
            "advanced": "Focus on technical details and edge cases",
            "mixed": "Provide progressive disclosure with expandable sections"
        }
        
        # Replace placeholders in outline
        processed_outline = []
        for section in base_outline:
            processed_section = section.replace("[Topic]", topic).replace("[Action]", f"Configure {topic}")
            processed_outline.append(processed_section)
        
        result = {
            "topic": topic,
            "content_type": content_type,
            "target_audience": target_audience,
            "outline": processed_outline,
            "style_guide_reminders": style_guide_reminders,
            "audience_considerations": audience_considerations.get(target_audience, ""),
            "generated_at": datetime.now().isoformat()
        }
        
        return [types.TextContent(
            type="text",
            text=json.dumps(result, indent=2)
        )]

    async def run(self):
        """Run the MCP server."""
        async with self.server.stdio_session() as session:
            await session.run()


async def main():
    """Main entry point for the server."""
    server = MSLearnAuthoringServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())