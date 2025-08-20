#!/usr/bin/env python3
"""
Microsoft Style Guide MCP Server - Web-Enabled Version

This server provides tools to analyze content against the official Microsoft Writing Style Guide
by dynamically querying and fetching content from https://learn.microsoft.com/en-us/style-guide/
"""

import asyncio
import json
import logging
import re
import sys
import aiohttp
from typing import Any, Dict, List, Optional, Union
import argparse
from urllib.parse import quote_plus, urljoin

from mcp import Server, __version__
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequest,
    CallToolResult,
    ListToolsRequest,
    ListToolsResult,
    TextContent,
    Tool,
    AnyUrl,
    Resource
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebStyleGuideAnalyzer:
    """Analyzer that fetches guidance from the official Microsoft Style Guide website."""
    
    def __init__(self):
        """Initialize the analyzer with web capabilities."""
        self.style_guide_base_url = "https://learn.microsoft.com/en-us/style-guide"
        self.session = None
        
        # Core style guide URLs for quick reference
        self.core_urls = {
            "voice_tone": f"{self.style_guide_base_url}/brand-voice-above-all-simple-human",
            "top_tips": f"{self.style_guide_base_url}/top-10-tips-style-voice",
            "bias_free": f"{self.style_guide_base_url}/bias-free-communication",
            "writing_tips": f"{self.style_guide_base_url}/global-communications/writing-tips",
            "welcome": f"{self.style_guide_base_url}/welcome/",
            "word_list": f"{self.style_guide_base_url}/a-z-word-list-term-collections"
        }
        
        # Basic patterns for quick local analysis
        self.basic_patterns = {
            "contractions": r"\b(it's|you're|we're|don't|can't|won't|let's|you'll|we'll)\b",
            "passive_voice": r"\b(is|are|was|were|been|be)\s+\w*ed\b",
            "long_sentences": r"[.!?]+\s*[A-Z][^.!?]{100,}[.!?]",
            "gendered_pronouns": r"\b(he|him|his|she|her|hers)\b",
            "non_inclusive_terms": r"\b(guys|mankind|blacklist|whitelist|master|slave|crazy|insane|lame)\b",
            "you_addressing": r"\byou\b",
            "second_person": r"\b(the user|users|one should|people should)\b"
        }

    async def init_session(self):
        """Initialize the HTTP session for web requests."""
        if not self.session:
            self.session = aiohttp.ClientSession(
                headers={'User-Agent': 'Microsoft-Style-Guide-MCP-Server/1.0'},
                timeout=aiohttp.ClientTimeout(total=30)
            )

    async def close_session(self):
        """Close the HTTP session."""
        if self.session:
            await self.session.close()
            self.session = None

    async def fetch_page_content(self, url: str) -> Dict[str, Any]:
        """Fetch content from a Microsoft Style Guide page."""
        try:
            await self.init_session()
            
            async with self.session.get(url) as response:
                if response.status == 200:
                    content = await response.text()
                    
                    # Extract main content (simplified - would need better parsing in production)
                    # Look for main content between common markers
                    title_match = re.search(r'<title>([^<]+)</title>', content)
                    title = title_match.group(1) if title_match else "Microsoft Style Guide"
                    
                    # Extract text content (basic implementation)
                    # In production, you'd want to use BeautifulSoup or similar
                    text_content = re.sub(r'<[^>]+>', ' ', content)
                    text_content = ' '.join(text_content.split())
                    
                    return {
                        "success": True,
                        "url": url,
                        "title": title,
                        "content": text_content[:2000],  # Limit content size
                        "full_url": url
                    }
                else:
                    return {
                        "success": False,
                        "error": f"HTTP {response.status}",
                        "url": url
                    }
                    
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return {
                "success": False,
                "error": str(e),
                "url": url
            }

    async def search_style_guide(self, query: str) -> Dict[str, Any]:
        """Search Microsoft Learn for style guide content."""
        try:
            # Use Microsoft Learn search
            search_url = f"https://learn.microsoft.com/en-us/search/?terms={quote_plus(query)}&scope=StyleGuide"
            
            await self.init_session()
            async with self.session.get(search_url) as response:
                if response.status == 200:
                    content = await response.text()
                    
                    # Extract search results (simplified)
                    results = []
                    
                    # Look for style guide links in the search results
                    style_guide_links = re.findall(
                        r'href="(/en-us/style-guide/[^"]+)"[^>]*>([^<]+)</a>',
                        content
                    )
                    
                    for link, title in style_guide_links[:5]:  # Limit to top 5 results
                        full_url = f"https://learn.microsoft.com{link}"
                        results.append({
                            "title": title.strip(),
                            "url": full_url,
                            "relevance": "high" if query.lower() in title.lower() else "medium"
                        })
                    
                    return {
                        "success": True,
                        "query": query,
                        "results": results,
                        "search_url": search_url
                    }
                else:
                    # Fallback to direct URL construction
                    return await self._fallback_search(query)
                    
        except Exception as e:
            logger.error(f"Error searching style guide: {e}")
            return await self._fallback_search(query)

    async def _fallback_search(self, query: str) -> Dict[str, Any]:
        """Fallback search using predefined URLs based on query keywords."""
        results = []
        
        query_lower = query.lower()
        
        if any(word in query_lower for word in ["voice", "tone", "warm", "crisp", "help"]):
            results.append({
                "title": "Microsoft's brand voice: above all, simple and human",
                "url": self.core_urls["voice_tone"],
                "relevance": "high"
            })
        
        if any(word in query_lower for word in ["tip", "top", "best"]):
            results.append({
                "title": "Top 10 tips for Microsoft style and voice",
                "url": self.core_urls["top_tips"],
                "relevance": "high"
            })
        
        if any(word in query_lower for word in ["bias", "inclusive", "accessibility", "gender"]):
            results.append({
                "title": "Bias-free communication",
                "url": self.core_urls["bias_free"],
                "relevance": "high"
            })
        
        if any(word in query_lower for word in ["grammar", "writing", "sentence", "active"]):
            results.append({
                "title": "Writing tips",
                "url": self.core_urls["writing_tips"],
                "relevance": "high"
            })
        
        if any(word in query_lower for word in ["terminology", "word", "term"]):
            results.append({
                "title": "A-Z word list and term collections",
                "url": self.core_urls["word_list"],
                "relevance": "high"
            })
        
        # If no specific matches, include welcome page
        if not results:
            results.append({
                "title": "Welcome to Microsoft Writing Style Guide",
                "url": self.core_urls["welcome"],
                "relevance": "medium"
            })
        
        return {
            "success": True,
            "query": query,
            "results": results,
            "search_method": "fallback_keyword_matching"
        }

    async def get_guidance_for_issue(self, issue_type: str, specific_term: str = "") -> Dict[str, Any]:
        """Get specific guidance for a detected issue."""
        if issue_type == "voice_tone":
            search_query = "voice tone warm relaxed crisp clear ready help"
        elif issue_type == "grammar":
            search_query = "active voice grammar writing tips"
        elif issue_type == "terminology":
            search_query = f"terminology {specific_term}" if specific_term else "terminology word list"
        elif issue_type == "accessibility":
            search_query = "bias-free communication inclusive language"
        else:
            search_query = "style guide best practices"
        
        search_results = await self.search_style_guide(search_query)
        
        if search_results["success"] and search_results["results"]:
            # Fetch content from the most relevant result
            top_result = search_results["results"][0]
            content = await self.fetch_page_content(top_result["url"])
            
            return {
                "issue_type": issue_type,
                "guidance_found": True,
                "source": top_result,
                "content": content,
                "search_results": search_results
            }
        else:
            return {
                "issue_type": issue_type,
                "guidance_found": False,
                "error": "Could not find specific guidance",
                "search_results": search_results
            }

    def analyze_text_patterns(self, text: str) -> Dict[str, Any]:
        """Analyze text for basic patterns and flag areas needing style guide consultation."""
        issues = []
        suggestions = []
        
        # Positive indicators
        contractions = len(re.findall(self.basic_patterns["contractions"], text, re.IGNORECASE))
        you_usage = len(re.findall(self.basic_patterns["you_addressing"], text, re.IGNORECASE))
        
        if contractions > 0:
            suggestions.append({
                "type": "positive",
                "message": f"Good use of contractions ({contractions} found) - supports warm, natural tone",
                "style_principle": "warm_and_relaxed"
            })
        
        if you_usage > 0:
            suggestions.append({
                "type": "positive", 
                "message": f"Good use of second person 'you' ({you_usage} instances) - directly engages readers",
                "style_principle": "ready_to_help"
            })
        
        # Issues to flag for style guide consultation
        
        # Passive voice detection
        passive_matches = list(re.finditer(self.basic_patterns["passive_voice"], text, re.IGNORECASE))
        for match in passive_matches:
            issues.append({
                "type": "grammar",
                "severity": "warning",
                "position": match.start(),
                "text": match.group(),
                "message": "Possible passive voice detected",
                "style_guide_query": "active voice grammar",
                "principle": "Use active voice for clarity and engagement"
            })
        
        # Third person usage
        third_person = list(re.finditer(self.basic_patterns["second_person"], text, re.IGNORECASE))
        for match in third_person:
            issues.append({
                "type": "voice_tone",
                "severity": "info",
                "position": match.start(),
                "text": match.group(),
                "message": "Consider using second person ('you') instead",
                "style_guide_query": "voice tone addressing readers",
                "principle": "Address readers directly for engagement"
            })
        
        # Long sentences
        long_sentences = list(re.finditer(self.basic_patterns["long_sentences"], text))
        for match in long_sentences:
            issues.append({
                "type": "grammar",
                "severity": "info",
                "position": match.start(),
                "message": "Long sentence detected - consider breaking up for clarity",
                "style_guide_query": "sentence length writing tips",
                "principle": "Keep sentences under 25 words when possible"
            })
        
        # Non-inclusive language
        non_inclusive = list(re.finditer(self.basic_patterns["non_inclusive_terms"], text, re.IGNORECASE))
        for match in non_inclusive:
            issues.append({
                "type": "accessibility",
                "severity": "error",
                "position": match.start(),
                "text": match.group(),
                "message": f"'{match.group()}' may not be inclusive",
                "style_guide_query": f"bias-free communication {match.group()} alternatives",
                "principle": "Use inclusive, bias-free language"
            })
        
        # Gendered pronouns
        gendered = list(re.finditer(self.basic_patterns["gendered_pronouns"], text, re.IGNORECASE))
        for match in gendered:
            issues.append({
                "type": "accessibility",
                "severity": "warning",
                "position": match.start(),
                "text": match.group(),
                "message": "Consider gender-neutral alternatives",
                "style_guide_query": "gender neutral language bias-free",
                "principle": "Use gender-neutral language in generic references"
            })
        
        return {
            "issues": issues,
            "suggestions": suggestions,
            "total_issues": len(issues),
            "queries_for_guidance": list(set(issue.get("style_guide_query") for issue in issues if issue.get("style_guide_query")))
        }

# Initialize the analyzer
analyzer = WebStyleGuideAnalyzer()

# Create the MCP server
server = Server("microsoft-style-guide")

@server.list_resources()
async def list_resources() -> list[Resource]:
    """List Microsoft Style Guide resources."""
    return [
        Resource(
            uri=AnyUrl(analyzer.style_guide_base_url + "/"),
            name="Microsoft Writing Style Guide",
            description="Official Microsoft Writing Style Guide documentation",
            mimeType="text/html"
        ),
        Resource(
            uri=AnyUrl(analyzer.core_urls["voice_tone"]),
            name="Brand Voice Guidelines",
            description="Microsoft's brand voice: simple and human",
            mimeType="text/html"
        ),
        Resource(
            uri=AnyUrl(analyzer.core_urls["top_tips"]),
            name="Top 10 Style Tips",
            description="Top 10 tips for Microsoft style and voice",
            mimeType="text/html"
        ),
        Resource(
            uri=AnyUrl(analyzer.core_urls["bias_free"]),
            name="Bias-Free Communication",
            description="Guidelines for inclusive, bias-free communication",
            mimeType="text/html"
        ),
        Resource(
            uri=AnyUrl(analyzer.core_urls["writing_tips"]),
            name="Writing Tips",
            description="Grammar and writing guidance",
            mimeType="text/html"
        )
    ]

@server.list_tools()
async def list_tools() -> ListToolsResult:
    """List available tools for Microsoft Style Guide analysis."""
    return ListToolsResult(
        tools=[
            Tool(
                name="analyze_content",
                description="Analyze content against Microsoft Style Guide with real-time web guidance",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "The text content to analyze"
                        },
                        "fetch_guidance": {
                            "type": "boolean",
                            "description": "Whether to fetch detailed guidance from the style guide website",
                            "default": True
                        },
                        "analysis_depth": {
                            "type": "string",
                            "enum": ["basic", "detailed", "comprehensive"],
                            "description": "Depth of analysis and guidance fetching",
                            "default": "detailed"
                        }
                    },
                    "required": ["text"]
                }
            ),
            Tool(
                name="search_style_guide",
                description="Search the Microsoft Style Guide website for specific guidance",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query for style guide guidance"
                        },
                        "fetch_content": {
                            "type": "boolean",
                            "description": "Whether to fetch full content from top results",
                            "default": True
                        }
                    },
                    "required": ["query"]
                }
            ),
            Tool(
                name="get_official_guidance",
                description="Get official guidance for specific style issues from Microsoft docs",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "issue_type": {
                            "type": "string",
                            "enum": ["voice_tone", "grammar", "terminology", "accessibility"],
                            "description": "Type of style issue to get guidance for"
                        },
                        "specific_term": {
                            "type": "string",
                            "description": "Specific term or phrase to get guidance for",
                            "default": ""
                        }
                    },
                    "required": ["issue_type"]
                }
            ),
            Tool(
                name="fetch_style_guide_page",
                description="Fetch content from a specific Microsoft Style Guide page",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL of the style guide page to fetch"
                        }
                    },
                    "required": ["url"]
                }
            )
        ]
    )

@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
    """Handle tool calls for Microsoft Style Guide analysis."""
    
    try:
        if name == "analyze_content":
            text = arguments.get("text", "")
            fetch_guidance = arguments.get("fetch_guidance", True)
            analysis_depth = arguments.get("analysis_depth", "detailed")
            
            if not text.strip():
                return CallToolResult(
                    content=[TextContent(
                        type="text",
                        text="Error: No text provided for analysis"
                    )]
                )
            
            # Perform pattern analysis
            pattern_analysis = analyzer.analyze_text_patterns(text)
            
            # Calculate basic statistics
            words = text.split()
            sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
            word_count = len(words)
            sentence_count = len(sentences)
            avg_words_per_sentence = round(word_count / max(1, sentence_count), 1)
            
            result = {
                "analysis_summary": {
                    "total_issues": pattern_analysis["total_issues"],
                    "text_statistics": {
                        "word_count": word_count,
                        "sentence_count": sentence_count,
                        "avg_words_per_sentence": avg_words_per_sentence
                    }
                },
                "pattern_analysis": pattern_analysis,
                "style_guide_consultation": {}
            }
            
            # Fetch guidance if requested and issues found
            if fetch_guidance and pattern_analysis["total_issues"] > 0:
                guidance_results = {}
                
                if analysis_depth in ["detailed", "comprehensive"]:
                    # Get guidance for each type of issue
                    issue_types = set(issue["type"] for issue in pattern_analysis["issues"])
                    
                    for issue_type in issue_types:
                        # Find specific terms for terminology issues
                        specific_terms = [
                            issue.get("text", "") for issue in pattern_analysis["issues"] 
                            if issue["type"] == issue_type and issue.get("text")
                        ]
                        specific_term = specific_terms[0] if specific_terms else ""
                        
                        guidance = await analyzer.get_guidance_for_issue(issue_type, specific_term)
                        guidance_results[issue_type] = guidance
                
                result["style_guide_consultation"] = guidance_results
            
            # Generate summary
            if pattern_analysis["total_issues"] == 0:
                status = "✅ Excellent"
                assessment = "Content follows Microsoft Style Guide principles well"
            elif pattern_analysis["total_issues"] <= 2:
                status = "⚠️ Good"  
                assessment = "Minor style improvements suggested"
            else:
                status = "❌ Needs Work"
                assessment = "Multiple style issues detected"
            
            summary = f"""📋 Microsoft Style Guide Analysis

{status} - {assessment}

📊 **Text Statistics:**
   • Words: {word_count}
   • Sentences: {sentence_count}  
   • Avg words/sentence: {avg_words_per_sentence}

🔍 **Issues Detected:** {pattern_analysis['total_issues']}
   • Grammar/Style: {len([i for i in pattern_analysis['issues'] if i['type'] == 'grammar'])}
   • Voice/Tone: {len([i for i in pattern_analysis['issues'] if i['type'] == 'voice_tone'])}
   • Accessibility: {len([i for i in pattern_analysis['issues'] if i['type'] == 'accessibility'])}

✅ **Positive Elements:** {len(pattern_analysis['suggestions'])}

🌐 **Official Guidance:** {'Fetched from Microsoft Style Guide' if fetch_guidance and pattern_analysis['total_issues'] > 0 else 'Available via search_style_guide tool'}
"""
            
            formatted_result = json.dumps(result, indent=2)
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"{summary}\n\n**Detailed Analysis:**\n{formatted_result}"
                )]
            )
        
        elif name == "search_style_guide":
            query = arguments.get("query", "")
            fetch_content = arguments.get("fetch_content", True)
            
            if not query.strip():
                return CallToolResult(
                    content=[TextContent(
                        type="text",
                        text="Error: No search query provided"
                    )]
                )
            
            search_results = await analyzer.search_style_guide(query)
            
            result = {
                "search_query": query,
                "search_results": search_results,
                "content_fetched": []
            }
            
            # Fetch content from top results if requested
            if fetch_content and search_results.get("success") and search_results.get("results"):
                for search_result in search_results["results"][:2]:  # Fetch top 2
                    content = await analyzer.fetch_page_content(search_result["url"])
                    result["content_fetched"].append(content)
            
            # Format response
            response = f"""🔍 Microsoft Style Guide Search Results

**Query:** "{query}"

**Results Found:** {len(search_results.get('results', []))}
"""
            
            if search_results.get("results"):
                response += "\n**Top Results:**\n"
                for i, result_item in enumerate(search_results["results"][:3], 1):
                    response += f"{i}. **{result_item['title']}**\n"
                    response += f"   📎 {result_item['url']}\n"
                    response += f"   🎯 Relevance: {result_item.get('relevance', 'medium')}\n\n"
            
            if result["content_fetched"]:
                response += "**Content Summary:**\n"
                for content in result["content_fetched"]:
                    if content["success"]:
                        response += f"📄 **{content['title']}**\n"
                        response += f"   {content['content'][:300]}...\n\n"
            
            formatted_result = json.dumps(result, indent=2)
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"{response}\n**Raw Data:**\n{formatted_result}"
                )]
            )
        
        elif name == "get_official_guidance":
            issue_type = arguments.get("issue_type")
            specific_term = arguments.get("specific_term", "")
            
            guidance = await analyzer.get_guidance_for_issue(issue_type, specific_term)
            
            if guidance.get("guidance_found"):
                source = guidance["source"]
                content = guidance["content"]
                
                response = f"""📚 Official Microsoft Style Guide Guidance

**Issue Type:** {issue_type.replace('_', ' ').title()}
**Specific Term:** {specific_term or 'General guidance'}

**Source:** {source['title']}
**URL:** {source['url']}

"""
                if content.get("success"):
                    response += f"**Official Guidance:**\n{content['content'][:800]}...\n\n"
                    response += f"📎 **Read Full Guidance:** {source['url']}\n"
                else:
                    response += f"⚠️ Could not fetch full content. Please visit: {source['url']}\n"
            else:
                response = f"""❌ Could not find specific guidance for {issue_type}

**Recommended Actions:**
1. Visit the main style guide: {analyzer.style_guide_base_url}
2. Try a broader search query
3. Check the A-Z word list for terminology questions

**General Resources:**
• Voice & Tone: {analyzer.core_urls['voice_tone']}
• Writing Tips: {analyzer.core_urls['writing_tips']}
• Bias-Free Communication: {analyzer.core_urls['bias_free']}
"""
            
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=response
                )]
            )
        
        elif name == "fetch_style_guide_page":
            url = arguments.get("url", "")
            
            if not url:
                return CallToolResult(
                    content=[TextContent(
                        type="text",
                        text="Error: No URL provided"
                    )]
                )
            
            # Validate it's a Microsoft Style Guide URL
            if "learn.microsoft.com/en-us/style-guide" not in url:
                return CallToolResult(
                    content=[TextContent(
                        type="text",
                        text="Error: URL must be from the Microsoft Style Guide (learn.microsoft.com/en-us/style-guide)"
                    )]
                )
            
            content = await analyzer.fetch_page_content(url)
            
            if content["success"]:
                response = f"""📄 Microsoft Style Guide Page Content

**Title:** {content['title']}
**URL:** {content['url']}

**Content:**
{content['content']}

📎 **Read Full Page:** {content['url']}
"""
            else:
                response = f"""❌ Failed to fetch page content

**URL:** {url}
**Error:** {content.get('error', 'Unknown error')}

**Suggestions:**
• Check if the URL is correct
• Visit the page directly in your browser
• Try the main style guide: {analyzer.style_guide_base_url}
"""
            
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=response
                )]
            )
        
        else:
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"Unknown tool: {name}"
                )]
            )
            
    except Exception as e:
        logger.error(f"Error in tool {name}: {e}")
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Error executing {name}: {str(e)}"
            )]
        )

async def main():
    """Main entry point for the MCP server."""
    parser = argparse.ArgumentParser(description="Microsoft Style Guide MCP Server - Web Enabled")
    parser.add_argument(
        "--version",
        action="version",
        version=f"microsoft-style-guide-mcp-web 1.0.0 (MCP {__version__})"
    )
    
    args = parser.parse_args()
    
    logger.info("Starting Microsoft Style Guide MCP Server (Web-Enabled)")
    logger.info(f"Querying official style guide at: {analyzer.style_guide_base_url}")
    
    try:
        # Run the server
        async with stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                server.create_initialization_options()
            )
    finally:
        # Clean up
        await analyzer.close_session()

if __name__ == "__main__":
    asyncio.run(main())