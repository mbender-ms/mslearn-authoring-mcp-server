#!/usr/bin/env python3
"""
Microsoft Style Guide MCP Client

This client connects to the Microsoft Style Guide MCP Server and provides
interfaces for VSCode, GitHub Copilot Chat, and command-line usage.
"""

import asyncio
import json
import logging
import sys
import argparse
from typing import Any, Dict, List, Optional
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import CallToolRequest, ListToolsRequest

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MicrosoftStyleGuideClient:
    """Client for Microsoft Style Guide MCP Server."""
    
    def __init__(self):
        """Initialize the client."""
        self.session: Optional[ClientSession] = None
        self.available_tools: List[str] = []
        self.server_process = None
    
    async def connect(self, server_script_path: str) -> bool:
        """Connect to the MCP server."""
        try:
            # Prepare server parameters
            server_params = StdioServerParameters(
                command=sys.executable,
                args=[server_script_path]
            )
            
            # Connect using stdio
            stdio_transport = await stdio_client(server_params)
            self.session = ClientSession(stdio_transport[0], stdio_transport[1])
            
            # Initialize the session
            init_result = await self.session.initialize()
            logger.info(f"Connected to Microsoft Style Guide MCP Server")
            logger.debug(f"Server info: {init_result}")
            
            # List available tools
            tools_result = await self.session.list_tools(ListToolsRequest())
            self.available_tools = [tool.name for tool in tools_result.tools]
            logger.info(f"Available tools: {', '.join(self.available_tools)}")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect to server: {e}")
            return False
    
    async def disconnect(self):
        """Disconnect from the MCP server."""
        if self.session:
            try:
                await self.session.close()
                logger.info("Disconnected from MCP server")
            except Exception as e:
                logger.error(f"Error during disconnect: {e}")
            finally:
                self.session = None
    
    async def analyze_content(self, text: str, analysis_type: str = "comprehensive") -> Dict[str, Any]:
        """Analyze content using the Microsoft Style Guide."""
        if not self.session:
            return {"success": False, "error": "Not connected to server"}
        
        try:
            result = await self.session.call_tool(
                CallToolRequest(
                    name="analyze_content",
                    arguments={
                        "text": text,
                        "analysis_type": analysis_type
                    }
                )
            )
            
            if result.content and result.content[0].type == "text":
                return {"success": True, "result": result.content[0].text}
            else:
                return {"success": False, "error": "No content returned"}
                
        except Exception as e:
            logger.error(f"Error analyzing content: {e}")
            return {"success": False, "error": str(e)}
    
    async def get_style_guidelines(self, category: str = "all") -> Dict[str, Any]:
        """Get Microsoft Style Guide guidelines."""
        if not self.session:
            return {"success": False, "error": "Not connected to server"}
        
        try:
            result = await self.session.call_tool(
                CallToolRequest(
                    name="get_style_guidelines",
                    arguments={"category": category}
                )
            )
            
            if result.content and result.content[0].type == "text":
                return {"success": True, "result": result.content[0].text}
            else:
                return {"success": False, "error": "No content returned"}
                
        except Exception as e:
            logger.error(f"Error getting guidelines: {e}")
            return {"success": False, "error": str(e)}
    
    async def suggest_improvements(self, text: str, focus_area: str = "all") -> Dict[str, Any]:
        """Get improvement suggestions for content."""
        if not self.session:
            return {"success": False, "error": "Not connected to server"}
        
        try:
            result = await self.session.call_tool(
                CallToolRequest(
                    name="suggest_improvements",
                    arguments={
                        "text": text,
                        "focus_area": focus_area
                    }
                )
            )
            
            if result.content and result.content[0].type == "text":
                return {"success": True, "result": result.content[0].text}
            else:
                return {"success": False, "error": "No content returned"}
                
        except Exception as e:
            logger.error(f"Error getting suggestions: {e}")
            return {"success": False, "error": str(e)}

    async def search_style_guide(self, query: str) -> Dict[str, Any]:
        """Search the Microsoft Style Guide website (web-enabled version only)."""
        if not self.session:
            return {"success": False, "error": "Not connected to server"}
        
        try:
            result = await self.session.call_tool(
                CallToolRequest(
                    name="search_style_guide",
                    arguments={"query": query}
                )
            )
            
            if result.content and result.content[0].type == "text":
                return {"success": True, "result": result.content[0].text}
            else:
                return {"success": False, "error": "No content returned"}
                
        except Exception as e:
            logger.error(f"Error searching style guide: {e}")
            return {"success": False, "error": str(e)}
    
    async def get_official_guidance(self, issue_type: str, specific_term: str = "") -> Dict[str, Any]:
        """Get official guidance for specific issues (web-enabled version only)."""
        if not self.session:
            return {"success": False, "error": "Not connected to server"}
        
        try:
            result = await self.session.call_tool(
                CallToolRequest(
                    name="get_official_guidance",
                    arguments={
                        "issue_type": issue_type,
                        "specific_term": specific_term
                    }
                )
            )
            
            if result.content and result.content[0].type == "text":
                return {"success": True, "result": result.content[0].text}
            else:
                return {"success": False, "error": "No content returned"}
                
        except Exception as e:
            logger.error(f"Error getting official guidance: {e}")
            return {"success": False, "error": str(e)}

class VSCodeInterface:
    """Interface for VSCode integration via GitHub Copilot Chat."""
    
    def __init__(self, client: MicrosoftStyleGuideClient):
        """Initialize VSCode interface."""
        self.client = client
    
    async def analyze_file(self, file_path: str, analysis_type: str = "comprehensive") -> Dict[str, Any]:
        """Analyze a file for Microsoft Style Guide compliance."""
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                return {"success": False, "error": f"File not found: {file_path}"}
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if not content.strip():
                return {"success": False, "error": "File is empty"}
            
            result = await self.client.analyze_content(content, analysis_type)
            if result["success"]:
                result["file_path"] = str(file_path)
                result["file_size"] = len(content)
            
            return result
            
        except Exception as e:
            logger.error(f"Error analyzing file {file_path}: {e}")
            return {"success": False, "error": str(e)}
    
    async def analyze_selection(self, text: str, analysis_type: str = "comprehensive") -> Dict[str, Any]:
        """Analyze selected text for Microsoft Style Guide compliance."""
        if not text.strip():
            return {"success": False, "error": "No text selected"}
        
        return await self.client.analyze_content(text, analysis_type)
    
    async def get_quick_fixes(self, text: str) -> Dict[str, Any]:
        """Get quick fix suggestions for text."""
        return await self.client.suggest_improvements(text, "all")

class GitHubCopilotInterface:
    """Interface for GitHub Copilot Chat integration."""
    
    def __init__(self, client: MicrosoftStyleGuideClient):
        """Initialize GitHub Copilot interface."""
        self.client = client
    
    async def process_chat_command(self, command: str, content: str = "") -> Dict[str, Any]:
        """Process GitHub Copilot chat commands for Microsoft Style Guide."""
        command = command.lower().strip()
        
        # Handle different command patterns
        if command in ["analyze", "check", "review", "style-check"]:
            if not content:
                return {"success": False, "error": "No content provided for analysis"}
            return await self.client.analyze_content(content, "comprehensive")
        
        elif command in ["voice", "tone", "voice-tone"]:
            if not content:
                return {"success": False, "error": "No content provided for voice analysis"}
            return await self.client.analyze_content(content, "voice_tone")
        
        elif command in ["grammar", "style", "writing"]:
            if not content:
                return {"success": False, "error": "No content provided for grammar analysis"}
            return await self.client.analyze_content(content, "grammar")
        
        elif command in ["terms", "terminology", "vocab"]:
            if not content:
                return {"success": False, "error": "No content provided for terminology analysis"}
            return await self.client.analyze_content(content, "terminology")
        
        elif command in ["accessibility", "inclusive", "bias"]:
            if not content:
                return {"success": False, "error": "No content provided for accessibility analysis"}
            return await self.client.analyze_content(content, "accessibility")
        
        elif command in ["improve", "suggest", "fix", "help"]:
            if not content:
                return {"success": False, "error": "No content provided for improvement suggestions"}
            return await self.client.suggest_improvements(content, "all")
        
        elif command in ["guidelines", "rules", "guide"]:
            return await self.client.get_style_guidelines("all")
        
        elif command.startswith("guidelines-"):
            category = command.replace("guidelines-", "")
            if category in ["voice", "grammar", "terminology", "accessibility"]:
                return await self.client.get_style_guidelines(category)
            else:
                return {"success": False, "error": f"Unknown guidelines category: {category}"}
        
        else:
            return {
                "success": False,
                "error": f"Unknown command: {command}",
                "available_commands": [
                    "analyze - Comprehensive style analysis",
                    "voice - Voice and tone analysis",
                    "grammar - Grammar and style analysis",
                    "terminology - Terminology consistency",
                    "accessibility - Inclusive language check",
                    "improve - Get improvement suggestions",
                    "guidelines - Get style guidelines",
                    "guidelines-voice - Voice guidelines only",
                    "guidelines-grammar - Grammar guidelines only",
                    "guidelines-terminology - Terminology guidelines only",
                    "guidelines-accessibility - Accessibility guidelines only"
                ]
            }
    
    async def analyze_file_from_chat(self, file_path: str, analysis_type: str = "comprehensive") -> Dict[str, Any]:
        """Analyze a file mentioned in chat."""
        vscode_interface = VSCodeInterface(self.client)
        return await vscode_interface.analyze_file(file_path, analysis_type)

class CLIInterface:
    """Command-line interface for the client."""
    
    def __init__(self, client: MicrosoftStyleGuideClient):
        """Initialize CLI interface."""
        self.client = client
        self.vscode = VSCodeInterface(client)
        self.copilot = GitHubCopilotInterface(client)
    
    async def run_interactive(self):
        """Run interactive mode for command-line usage."""
        print("🎯 Microsoft Style Guide MCP Client - Interactive Mode")
        print("=" * 60)
        print("Commands:")
        print("  analyze [text] - Analyze text content")
        print("  file [path] - Analyze a file")
        print("  voice [text] - Voice and tone analysis")
        print("  grammar [text] - Grammar analysis")
        print("  terms [text] - Terminology analysis")
        print("  access [text] - Accessibility analysis")
        print("  improve [text] - Get improvement suggestions")
        print("  guidelines [category] - Get style guidelines")
        print("  search [query] - Search official style guide (web version)")
        print("  guidance - Get official guidance for specific issues (web version)")
        print("  help - Show this help")
        print("  quit - Exit the program")
        print("=" * 60)
        
        while True:
            try:
                user_input = input("\n📝 Enter command: ").strip()
                
                if not user_input:
                    continue
                
                parts = user_input.split(None, 1)
                command = parts[0].lower()
                content = parts[1] if len(parts) > 1 else ""
                
                if command in ["quit", "exit", "q"]:
                    print("👋 Goodbye!")
                    break
                
                elif command == "help":
                    await self._show_help()
                
                elif command == "analyze":
                    if not content:
                        content = input("Enter text to analyze: ")
                    await self._handle_analyze(content, "comprehensive")
                
                elif command == "file":
                    if not content:
                        content = input("Enter file path: ")
                    await self._handle_file_analysis(content)
                
                elif command == "voice":
                    if not content:
                        content = input("Enter text for voice analysis: ")
                    await self._handle_analyze(content, "voice_tone")
                
                elif command == "grammar":
                    if not content:
                        content = input("Enter text for grammar analysis: ")
                    await self._handle_analyze(content, "grammar")
                
                elif command == "terms":
                    if not content:
                        content = input("Enter text for terminology analysis: ")
                    await self._handle_analyze(content, "terminology")
                
                elif command == "access":
                    if not content:
                        content = input("Enter text for accessibility analysis: ")
                    await self._handle_analyze(content, "accessibility")
                
                elif command == "improve":
                    if not content:
                        content = input("Enter text to improve: ")
                    await self._handle_improvements(content)
                
                elif command == "guidelines":
                    category = content or "all"
                    await self._handle_guidelines(category)
                
                elif command == "search":
                    if not content:
                        content = input("Enter search query for style guide: ")
                    await self._handle_search(content)
                
                elif command == "guidance":
                    issue_type = input("Enter issue type (voice_tone, grammar, terminology, accessibility): ")
                    specific_term = input("Enter specific term (optional): ")
                    await self._handle_official_guidance(issue_type, specific_term)
                
                else:
                    print(f"❌ Unknown command: {command}. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    async def _handle_analyze(self, text: str, analysis_type: str):
        """Handle analysis commands."""
        if not text.strip():
            print("❌ No text provided")
            return
        
        print(f"🔍 Analyzing content for {analysis_type.replace('_', ' ')}...")
        result = await self.client.analyze_content(text, analysis_type)
        
        if result["success"]:
            print("✅ Analysis complete:")
            print(result["result"])
        else:
            print(f"❌ Analysis failed: {result['error']}")
    
    async def _handle_file_analysis(self, file_path: str):
        """Handle file analysis."""
        if not file_path.strip():
            print("❌ No file path provided")
            return
        
        print(f"📄 Analyzing file: {file_path}")
        result = await self.vscode.analyze_file(file_path)
        
        if result["success"]:
            print("✅ File analysis complete:")
            print(result["result"])
        else:
            print(f"❌ File analysis failed: {result['error']}")
    
    async def _handle_improvements(self, text: str):
        """Handle improvement suggestions."""
        if not text.strip():
            print("❌ No text provided")
            return
        
        print("💡 Generating improvement suggestions...")
        result = await self.client.suggest_improvements(text)
        
        if result["success"]:
            print("✅ Suggestions generated:")
            print(result["result"])
        else:
            print(f"❌ Failed to generate suggestions: {result['error']}")
    
    async def _handle_guidelines(self, category: str):
        """Handle guidelines requests."""
        print(f"📚 Getting {category} guidelines...")
        result = await self.client.get_style_guidelines(category)
        
        if result["success"]:
            print("✅ Guidelines retrieved:")
            print(result["result"])
        else:
            print(f"❌ Failed to get guidelines: {result['error']}")
    
    async def _handle_search(self, query: str):
        """Handle style guide search (web-enabled version only)."""
        if not query.strip():
            print("❌ No search query provided")
            return
        
        print(f"🔍 Searching Microsoft Style Guide for: {query}")
        result = await self.client.search_style_guide(query)
        
        if result["success"]:
            print("✅ Search completed:")
            print(result["result"])
        else:
            print(f"❌ Search failed: {result['error']}")
            if "Unknown tool" in result.get("error", ""):
                print("💡 Note: Search requires the web-enabled server version (mcp_server_web.py)")
    
    async def _handle_official_guidance(self, issue_type: str, specific_term: str):
        """Handle official guidance requests (web-enabled version only)."""
        print(f"📖 Getting official guidance for {issue_type}...")
        result = await self.client.get_official_guidance(issue_type, specific_term)
        
        if result["success"]:
            print("✅ Official guidance retrieved:")
            print(result["result"])
        else:
            print(f"❌ Failed to get guidance: {result['error']}")
            if "Unknown tool" in result.get("error", ""):
                print("💡 Note: Official guidance requires the web-enabled server version (mcp_server_web.py)")
    
    async def _show_help(self):
        """Show detailed help information."""
        help_text = """
📋 Microsoft Style Guide MCP Client Help
========================================

🎯 Analysis Commands:
  analyze [text]    - Comprehensive Microsoft Style Guide analysis
  voice [text]      - Voice and tone analysis (warm, crisp, helpful)
  grammar [text]    - Grammar and style analysis (active voice, clarity)
  terms [text]      - Terminology consistency check
  access [text]     - Accessibility and inclusive language check
  
📄 File Commands:
  file [path]       - Analyze a file (supports .md, .txt, .rst files)
  
💡 Improvement Commands:
  improve [text]    - Get specific improvement suggestions
  
📚 Reference Commands:
  guidelines        - Get all Microsoft Style Guide guidelines
  guidelines voice  - Get voice and tone guidelines only
  guidelines grammar - Get grammar guidelines only
  guidelines terms  - Get terminology guidelines only
  guidelines access - Get accessibility guidelines only
  
🌐 Web-Enabled Commands (mcp_server_web.py only):
  search [query]    - Search official Microsoft Style Guide
  guidance          - Get official guidance for specific issues
  
🔧 Utility Commands:
  help             - Show this help
  quit             - Exit the program

📝 Example Usage:
  analyze Hello everyone, you can easily configure the settings.
  file README.md
  improve The user should utilize the functionality to facilitate...
  search "active voice examples"
  guidance (then follow prompts for issue type)
  guidelines voice

🎯 Microsoft Style Guide Principles:
  • Warm and relaxed: Natural, conversational tone
  • Crisp and clear: Direct, scannable content  
  • Ready to help: Action-oriented, supportive guidance
  • Use active voice and second person (you)
  • Use inclusive, bias-free language
  • Keep sentences under 25 words
  • Use contractions for natural tone
        """
        print(help_text)

def format_output_for_display(result: str) -> str:
    """Format the result for better console display."""
    lines = result.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('📋') or line.startswith('🎯') or line.startswith('📊'):
            formatted_lines.append(f"\n{line}")
        elif line.startswith('✅') or line.startswith('⚠️') or line.startswith('❌'):
            formatted_lines.append(f"  {line}")
        elif line and not line.startswith(' '):
            formatted_lines.append(line)
        else:
            formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

async def main():
    """Main entry point for the client."""
    parser = argparse.ArgumentParser(
        description="Microsoft Style Guide MCP Client",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python mcp_client.py --mode interactive
  
  # Analyze a file
  python mcp_client.py --mode file --file README.md
  
  # Analyze text with web-enabled version
  python mcp_client.py --mode text --text "Your content here" --server mcp_server_web.py
  
  # Search official style guide (web-enabled version only)
  python mcp_client.py --mode search --query "active voice examples" --server mcp_server_web.py
  
  # GitHub Copilot Chat integration
  python mcp_client.py --mode copilot --command analyze --text "Content to analyze"
  
  # Get style guidelines
  python mcp_client.py --mode guidelines --category voice
        """
    )
    
    parser.add_argument(
        "--server-script", "--server",
        default="mcp_server_web.py",
        help="Path to the MCP server script (default: mcp_server_web.py for web-enabled version)"
    )
    parser.add_argument(
        "--mode",
        choices=["interactive", "file", "text", "copilot", "guidelines", "search"],
        default="interactive",
        help="Client mode (default: interactive)"
    )
    parser.add_argument(
        "--file",
        help="File to analyze (for file mode)"
    )
    parser.add_argument(
        "--text",
        help="Text to analyze (for text mode)"
    )
    parser.add_argument(
        "--command",
        help="Command for copilot mode (analyze, voice, grammar, etc.)"
    )
    parser.add_argument(
        "--analysis-type",
        choices=["comprehensive", "voice_tone", "grammar", "terminology", "accessibility"],
        default="comprehensive",
        help="Type of analysis to perform (default: comprehensive)"
    )
    parser.add_argument(
        "--query",
        help="Search query for search mode"
    )
    parser.add_argument(
        "--category",
        choices=["voice", "grammar", "terminology", "accessibility", "all"],
        default="all",
        help="Category for guidelines mode (default: all)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Configure logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize client
    client = MicrosoftStyleGuideClient()
    cli = CLIInterface(client)
    
    try:
        # Check if server script exists
        server_path = Path(args.server_script)
        if not server_path.exists():
            print(f"❌ Error: Server script not found: {server_path}")
            print(f"   Please ensure {args.server_script} is in the current directory")
            return 1
        
        # Connect to server
        print(f"🔌 Connecting to Microsoft Style Guide MCP Server...")
        if not await client.connect(str(server_path)):
            print("❌ Failed to connect to MCP server")
            print("   Please ensure the server script is correct and dependencies are installed")
            return 1
        
        print("✅ Connected successfully!\n")
        
        # Run based on mode
        if args.mode == "interactive":
            await cli.run_interactive()
        
        elif args.mode == "file":
            if not args.file:
                print("❌ Error: --file argument required for file mode")
                return 1
            
            result = await cli.vscode.analyze_file(args.file, args.analysis_type)
            if result["success"]:
                print(format_output_for_display(result["result"]))
            else:
                print(f"❌ Error: {result['error']}")
                return 1
        
        elif args.mode == "text":
            if not args.text:
                print("❌ Error: --text argument required for text mode")
                return 1
            
            result = await client.analyze_content(args.text, args.analysis_type)
            if result["success"]:
                print(format_output_for_display(result["result"]))
            else:
                print(f"❌ Error: {result['error']}")
                return 1
        
        elif args.mode == "copilot":
            if not args.command:
                print("❌ Error: --command argument required for copilot mode")
                return 1
            
            copilot_interface = GitHubCopilotInterface(client)
            result = await copilot_interface.process_chat_command(args.command, args.text or "")
            
            if result["success"]:
                print(format_output_for_display(result["result"]))
            else:
                print(f"❌ Error: {result['error']}")
                if "available_commands" in result:
                    print("\n📋 Available commands:")
                    for cmd in result["available_commands"]:
                        print(f"  • {cmd}")
                return 1
        
        elif args.mode == "search":
            if not args.query:
                print("❌ Error: --query argument required for search mode")
                return 1
            
            result = await client.search_style_guide(args.query)
            if result["success"]:
                print(format_output_for_display(result["result"]))
            else:
                print(f"❌ Error: {result['error']}")
                if "Unknown tool" in result.get("error", ""):
                    print("💡 Note: Search requires the web-enabled server version (mcp_server_web.py)")
                return 1
        
        elif args.mode == "guidelines":
            result = await client.get_style_guidelines(args.category)
            if result["success"]:
                print(format_output_for_display(result["result"]))
            else:
                print(f"❌ Error: {result['error']}")
                return 1
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"❌ Unexpected error: {e}")
        return 1
    
    finally:
        # Disconnect from server
        await client.disconnect()

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)