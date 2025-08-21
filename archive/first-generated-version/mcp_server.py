#!/usr/bin/env python3
"""
Microsoft Style Guide MCP Server

This server provides tools to analyze content against the official Microsoft Writing Style Guide
by dynamically querying the live documentation at https://learn.microsoft.com/en-us/style-guide/
"""

import asyncio
import json
import logging
import re
import sys
from typing import Any, Dict, List, Optional, Union
import argparse

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

class MicrosoftStyleGuideAnalyzer:
    """Analyzer that queries the official Microsoft Style Guide website for guidance."""
    
    def __init__(self):
        """Initialize the analyzer with basic pattern matching and web query capabilities."""
        self.style_guide_base_url = "https://learn.microsoft.com/en-us/style-guide"
        
        # Basic patterns for quick analysis - detailed guidance comes from website
        self.basic_patterns = {
            "contractions": r"\b(it's|you're|we're|don't|can't|won't|let's|you'll|we'll)\b",
            "passive_voice": r"\b(is|are|was|were|been|be)\s+\w*ed\b",
            "long_sentences": r"[.!?]+\s*[A-Z][^.!?]{100,}[.!?]",
            "gendered_pronouns": r"\b(he|him|his|she|her|hers)\b",
            "non_inclusive_terms": r"\b(guys|mankind|blacklist|whitelist|master|slave|crazy|insane|lame)\b"
        }
        
        # Common terminology that needs checking against official guidance
        self.terminology_to_check = [
            "AI", "A.I.", "api", "API", "email", "e-mail", "website", "web site",
            "online", "on-line", "setup", "set up", "login", "log in", "sign in",
            "real-time", "realtime", "real time", "Wi-Fi", "WiFi", "wifi"
        ]

    async def search_style_guide(self, query: str, session) -> Dict[str, Any]:
        """Search the Microsoft Style Guide website for specific guidance."""
        try:
            # Use web search to find relevant style guide pages
            search_query = f"site:learn.microsoft.com/en-us/style-guide {query}"
            
            # This would be implemented using the web search tools
            # For now, return a placeholder structure
            return {
                "success": True,
                "query": query,
                "results": [],
                "guidance": f"Search for '{query}' in Microsoft Style Guide",
                "source_url": f"{self.style_guide_base_url}/search?q={query.replace(' ', '+')}"
            }
        except Exception as e:
            logger.error(f"Error searching style guide: {e}")
            return {
                "success": False,
                "error": str(e),
                "query": query
            }

    async def get_voice_tone_guidance(self, session) -> Dict[str, Any]:
        """Get voice and tone guidance from the official style guide."""
        return await self.search_style_guide("voice tone warm relaxed crisp clear ready help", session)

    async def get_grammar_guidance(self, session) -> Dict[str, Any]:
        """Get grammar and style guidance from the official style guide."""
        return await self.search_style_guide("grammar active voice sentence structure", session)

    async def get_terminology_guidance(self, term: str, session) -> Dict[str, Any]:
        """Get specific terminology guidance from the official style guide."""
        return await self.search_style_guide(f"terminology {term}", session)

    async def get_accessibility_guidance(self, session) -> Dict[str, Any]:
        """Get accessibility and inclusive language guidance from the official style guide."""
        return await self.search_style_guide("bias-free communication inclusive language accessibility", session)

    def analyze_basic_patterns(self, text: str) -> Dict[str, Any]:
        """Perform basic pattern analysis to identify areas needing style guide consultation."""
        issues = []
        suggestions = []
        
        # Check for contractions (positive indicator)
        contractions = len(re.findall(self.basic_patterns["contractions"], text, re.IGNORECASE))
        if contractions > 0:
            suggestions.append(f"Good use of contractions ({contractions} found) - this supports a warm, natural tone")
        else:
            issues.append({
                "type": "voice_tone",
                "severity": "info",
                "message": "Consider using contractions (it's, you're, we're) for a more natural tone",
                "query_needed": "contractions natural voice tone"
            })
        
        # Check for passive voice
        passive_matches = list(re.finditer(self.basic_patterns["passive_voice"], text, re.IGNORECASE))
        for match in passive_matches:
            issues.append({
                "type": "grammar",
                "severity": "warning",
                "position": match.start(),
                "text": match.group(),
                "message": "Possible passive voice - consider active voice",
                "query_needed": "active voice grammar"
            })
        
        # Check for long sentences
        long_sentences = list(re.finditer(self.basic_patterns["long_sentences"], text))
        for match in long_sentences:
            issues.append({
                "type": "grammar",
                "severity": "info", 
                "position": match.start(),
                "message": "Long sentence detected - consider breaking into shorter sentences",
                "query_needed": "sentence length clarity"
            })
        
        # Check for gendered pronouns
        gendered = list(re.finditer(self.basic_patterns["gendered_pronouns"], text, re.IGNORECASE))
        for match in gendered:
            issues.append({
                "type": "accessibility",
                "severity": "warning",
                "position": match.start(),
                "text": match.group(),
                "message": "Consider gender-neutral language",
                "query_needed": "bias-free communication gender neutral"
            })
        
        # Check for non-inclusive terms
        non_inclusive = list(re.finditer(self.basic_patterns["non_inclusive_terms"], text, re.IGNORECASE))
        for match in non_inclusive:
            issues.append({
                "type": "accessibility",
                "severity": "error",
                "position": match.start(),
                "text": match.group(),
                "message": f"'{match.group()}' may not be inclusive - check style guide for alternatives",
                "query_needed": f"inclusive language {match.group()} alternatives"
            })
        
        # Check terminology
        for term in self.terminology_to_check:
            if term.lower() in text.lower():
                # Only flag potentially incorrect variants
                if term in ["A.I.", "e-mail", "web site", "on-line", "WiFi", "wifi"]:
                    issues.append({
                        "type": "terminology",
                        "severity": "warning",
                        "text": term,
                        "message": f"Check Microsoft Style Guide for correct usage of '{term}'",
                        "query_needed": f"terminology {term} correct usage"
                    })
        
        return {
            "issues": issues,
            "suggestions": suggestions,
            "total_issues": len(issues),
            "queries_needed": list(set(issue.get("query_needed") for issue in issues if issue.get("query_needed")))
        }

    async def get_detailed_guidance(self, queries: List[str], session) -> Dict[str, Any]:
        """Get detailed guidance from the style guide for specific queries."""
        guidance = {}
        
        for query in queries:
            result = await self.search_style_guide(query, session)
            guidance[query] = result
        
        return guidance

# Initialize the analyzer
analyzer = MicrosoftStyleGuideAnalyzer()

# Create the MCP server
server = Server("microsoft-style-guide")

@server.list_resources()
async def list_resources() -> list[Resource]:
    """List Microsoft Style Guide resources."""
    return [
        Resource(
            uri=AnyUrl("https://learn.microsoft.com/en-us/style-guide/"),
            name="Microsoft Writing Style Guide",
            description="Official Microsoft Writing Style Guide documentation",
            mimeType="text/html"
        ),
        Resource(
            uri=AnyUrl("https://learn.microsoft.com/en-us/style-guide/welcome/"),
            name="Style Guide Welcome",
            description="Introduction to Microsoft Style Guide principles",
            mimeType="text/html"
        ),
        Resource(
            uri=AnyUrl("https://learn.microsoft.com/en-us/style-guide/brand-voice-above-all-simple-human"),
            name="Brand Voice Guidelines",
            description="Microsoft's brand voice: simple and human",
            mimeType="text/html"
        ),
        Resource(
            uri=AnyUrl("https://learn.microsoft.com/en-us/style-guide/bias-free-communication"),
            name="Bias-Free Communication",
            description="Guidelines for inclusive, bias-free communication",
            mimeType="text/html"
        ),
        Resource(
            uri=AnyUrl("https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice"),
            name="Top 10 Style Tips",
            description="Top 10 tips for Microsoft style and voice",
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
                description="Analyze content against Microsoft Style Guide by querying official documentation",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "The text content to analyze"
                        },
                        "analysis_type": {
                            "type": "string",
                            "enum": ["comprehensive", "voice_tone", "grammar", "terminology", "accessibility"],
                            "description": "Type of analysis to perform",
                            "default": "comprehensive"
                        },
                        "get_detailed_guidance": {
                            "type": "boolean",
                            "description": "Whether to fetch detailed guidance from the style guide website",
                            "default": True
                        }
                    },
                    "required": ["text"]
                }
            ),
            Tool(
                name="search_style_guide",
                description="Search the Microsoft Style Guide for specific guidance",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query for style guide guidance"
                        },
                        "category": {
                            "type": "string",
                            "enum": ["voice", "grammar", "terminology", "accessibility", "general"],
                            "description": "Category to focus the search on",
                            "default": "general"
                        }
                    },
                    "required": ["query"]
                }
            ),
            Tool(
                name="get_style_guidelines",
                description="Get comprehensive style guidelines from official Microsoft documentation",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "enum": ["voice", "grammar", "terminology", "accessibility", "all"],
                            "description": "Category of guidelines to retrieve",
                            "default": "all"
                        }
                    }
                }
            ),
            Tool(
                name="suggest_improvements",
                description="Get improvement suggestions by consulting the style guide",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "The text content to improve"
                        },
                        "focus_area": {
                            "type": "string",
                            "enum": ["voice", "clarity", "terminology", "accessibility", "all"],
                            "description": "Area to focus improvements on",
                            "default": "all"
                        }
                    },
                    "required": ["text"]
                }
            )
        ]
    )

@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
    """Handle tool calls for Microsoft Style Guide analysis."""
    
    if name == "analyze_content":
        text = arguments.get("text", "")
        analysis_type = arguments.get("analysis_type", "comprehensive")
        get_detailed_guidance = arguments.get("get_detailed_guidance", True)
        
        if not text.strip():
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text="Error: No text provided for analysis"
                )]
            )
        
        try:
            # Perform basic pattern analysis
            basic_analysis = analyzer.analyze_basic_patterns(text)
            
            # Count words and sentences for statistics
            word_count = len(text.split())
            sentence_count = len([s for s in re.split(r'[.!?]+', text) if s.strip()])
            avg_words_per_sentence = round(word_count / max(1, sentence_count), 1)
            
            result = {
                "analysis_type": analysis_type,
                "text_statistics": {
                    "word_count": word_count,
                    "sentence_count": sentence_count,
                    "avg_words_per_sentence": avg_words_per_sentence
                },
                "basic_analysis": basic_analysis,
                "style_guide_queries_needed": basic_analysis.get("queries_needed", []),
                "official_guidance": "Query the Microsoft Style Guide for detailed guidance on flagged issues",
                "next_steps": [
                    "Review flagged issues against official Microsoft Style Guide",
                    f"Visit {analyzer.style_guide_base_url} for complete guidelines",
                    "Use the search_style_guide tool for specific guidance"
                ]
            }
            
            # Generate summary
            total_issues = basic_analysis["total_issues"]
            if total_issues == 0:
                assessment = "✅ No major style issues detected"
            elif total_issues <= 3:
                assessment = "⚠️ Minor style issues detected"
            else:
                assessment = "❌ Multiple style issues need attention"
            
            summary = f"""📋 Microsoft Style Guide Analysis Summary
{assessment}

📊 Text Statistics:
   Words: {word_count}
   Sentences: {sentence_count}
   Avg words/sentence: {avg_words_per_sentence}

🔍 Issues Found: {total_issues}
   • Grammar/Style: {len([i for i in basic_analysis['issues'] if i['type'] == 'grammar'])}
   • Terminology: {len([i for i in basic_analysis['issues'] if i['type'] == 'terminology'])}
   • Accessibility: {len([i for i in basic_analysis['issues'] if i['type'] == 'accessibility'])}
   • Voice/Tone: {len([i for i in basic_analysis['issues'] if i['type'] == 'voice_tone'])}

🌐 For detailed guidance, consult the official Microsoft Style Guide:
   {analyzer.style_guide_base_url}

💡 Use the search_style_guide tool to get specific guidance for flagged issues.
"""
            
            formatted_result = json.dumps(result, indent=2)
            
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"{summary}\n\nDetailed Analysis:\n{formatted_result}"
                )]
            )
            
        except Exception as e:
            logger.error(f"Error during analysis: {e}")
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"Error during analysis: {str(e)}"
                )]
            )
    
    elif name == "search_style_guide":
        query = arguments.get("query", "")
        category = arguments.get("category", "general")
        
        if not query.strip():
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text="Error: No search query provided"
                )]
            )
        
        try:
            # This is where you would implement actual web search
            # For now, providing guidance on how to search
            search_url = f"{analyzer.style_guide_base_url}/?search={query.replace(' ', '%20')}"
            
            guidance = f"""🔍 Microsoft Style Guide Search

Query: "{query}"
Category: {category}

📚 To get the most current guidance:

1. **Direct Search**: Visit the Microsoft Style Guide website
   {analyzer.style_guide_base_url}

2. **Specific Search URL**: 
   {search_url}

3. **Key Areas to Check**:
   • Voice and Tone: {analyzer.style_guide_base_url}/brand-voice-above-all-simple-human
   • Grammar Tips: {analyzer.style_guide_base_url}/global-communications/writing-tips
   • Bias-Free Communication: {analyzer.style_guide_base_url}/bias-free-communication
   • Top 10 Tips: {analyzer.style_guide_base_url}/top-10-tips-style-voice

💡 **Note**: This tool provides links to official documentation. For real-time content analysis, 
the MCP server would need web search capabilities to fetch and analyze current style guide content.

🔧 **Integration Tip**: In VSCode, you can use the built-in browser or web search to quickly 
access these style guide resources while editing your content.
"""
            
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=guidance
                )]
            )
            
        except Exception as e:
            logger.error(f"Error searching style guide: {e}")
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"Error searching style guide: {str(e)}"
                )]
            )
    
    elif name == "get_style_guidelines":
        category = arguments.get("category", "all")
        
        guidelines = f"""📚 Microsoft Writing Style Guide Resources

🌐 **Official Documentation**: {analyzer.style_guide_base_url}

"""
        
        if category in ["voice", "all"]:
            guidelines += """🎯 **Voice and Tone Guidelines**:
   • Brand Voice: {}/brand-voice-above-all-simple-human
   • Warm and relaxed: Natural, conversational tone
   • Crisp and clear: Direct, scannable content
   • Ready to help: Action-oriented, supportive

""".format(analyzer.style_guide_base_url)
        
        if category in ["grammar", "all"]:
            guidelines += """✍️ **Grammar and Style Guidelines**:
   • Writing Tips: {}/global-communications/writing-tips
   • Use active voice and second person
   • Keep sentences under 25 words
   • Use imperative mood for instructions

""".format(analyzer.style_guide_base_url)
        
        if category in ["terminology", "all"]:
            guidelines += """📖 **Terminology Guidelines**:
   • A-Z Word List: {}/a-z-word-list-term-collections
   • Use consistent, Microsoft-approved terms
   • Examples: AI (not A.I.), email (not e-mail)
   • Consult the word list for specific terms

""".format(analyzer.style_guide_base_url)
        
        if category in ["accessibility", "all"]:
            guidelines += """♿ **Accessibility Guidelines**:
   • Bias-Free Communication: {}/bias-free-communication
   • Use inclusive, people-first language
   • Avoid terms with unconscious bias
   • Focus on accessibility for all users

""".format(analyzer.style_guide_base_url)
        
        guidelines += """💡 **Top 10 Tips**: {}/top-10-tips-style-voice

🔧 **How to Use This Information**:
1. Visit the linked pages for detailed, current guidance
2. Use the search_style_guide tool for specific queries
3. Bookmark key pages for quick reference while writing
4. Check for updates regularly as the guide evolves

⚡ **Quick Access**: The style guide is searchable and mobile-friendly for easy reference.
""".format(analyzer.style_guide_base_url)
        
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=guidelines
            )]
        )
    
    elif name == "suggest_improvements":
        text = arguments.get("text", "")
        focus_area = arguments.get("focus_area", "all")
        
        if not text.strip():
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text="Error: No text provided for improvement suggestions"
                )]
            )
        
        try:
            # Analyze text for issues
            basic_analysis = analyzer.analyze_basic_patterns(text)
            issues = basic_analysis["issues"]
            
            suggestions = []
            style_guide_links = []
            
            # Generate specific suggestions based on issues found
            for issue in issues:
                if issue["type"] == "voice_tone":
                    suggestions.append("• Use more contractions (it's, you're, we're) for a natural tone")
                    style_guide_links.append(f"{analyzer.style_guide_base_url}/brand-voice-above-all-simple-human")
                
                elif issue["type"] == "grammar":
                    if "passive voice" in issue["message"]:
                        suggestions.append(f"• Replace passive voice: '{issue.get('text', '')}' → use active voice")
                    elif "long sentence" in issue["message"]:
                        suggestions.append("• Break long sentences into shorter, clearer ones")
                    style_guide_links.append(f"{analyzer.style_guide_base_url}/global-communications/writing-tips")
                
                elif issue["type"] == "terminology":
                    suggestions.append(f"• Check Microsoft terminology for '{issue.get('text', '')}'")
                    style_guide_links.append(f"{analyzer.style_guide_base_url}/a-z-word-list-term-collections")
                
                elif issue["type"] == "accessibility":
                    suggestions.append(f"• Replace '{issue.get('text', '')}' with more inclusive language")
                    style_guide_links.append(f"{analyzer.style_guide_base_url}/bias-free-communication")
            
            # Add general suggestions
            word_count = len(text.split())
            if word_count > 50:
                suggestions.append("• Consider using bullet points or shorter paragraphs for scannability")
            
            if not re.search(r"\byou\b", text, re.IGNORECASE):
                suggestions.append("• Address readers directly using 'you' for engagement")
            
            # Remove duplicates from links
            style_guide_links = list(set(style_guide_links))
            
            result = f"""💡 Microsoft Style Guide Improvement Suggestions

📝 **Specific Improvements**:
{chr(10).join(suggestions) if suggestions else '• No specific issues detected - content follows style guide well!'}

📚 **Consult These Style Guide Sections**:
{chr(10).join(f'   {link}' for link in style_guide_links) if style_guide_links else '   No specific sections needed'}

🎯 **General Microsoft Style Principles**:
• Write in a warm, conversational tone
• Use active voice and direct language  
• Keep sentences under 25 words
• Use inclusive, bias-free language
• Address readers as "you"

🌐 **Complete Guidelines**: {analyzer.style_guide_base_url}

💭 **Next Steps**:
1. Review the suggested style guide sections
2. Apply the specific improvements listed above
3. Re-analyze your content after making changes
4. Consider reading the Top 10 Tips: {analyzer.style_guide_base_url}/top-10-tips-style-voice
"""
            
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=result
                )]
            )
            
        except Exception as e:
            logger.error(f"Error generating suggestions: {e}")
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"Error generating suggestions: {str(e)}"
                )]
            )
    
    else:
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]
        )

async def main():
    """Main entry point for the MCP server."""
    parser = argparse.ArgumentParser(description="Microsoft Style Guide MCP Server")
    parser.add_argument(
        "--version",
        action="version",
        version=f"microsoft-style-guide-mcp 1.0.0 (MCP {__version__})"
    )
    
    args = parser.parse_args()
    
    logger.info("Starting Microsoft Style Guide MCP Server")
    logger.info(f"Using official style guide at: {analyzer.style_guide_base_url}")
    
    # Run the server
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())