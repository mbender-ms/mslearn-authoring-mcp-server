#!/usr/bin/env python3
"""
Microsoft Style Guide MCP Server - Quick Start

This script provides a quick demonstration of the Microsoft Style Guide MCP Server
functionality and helps users get started with the tool.
"""

import asyncio
import sys
import time
from pathlib import Path
from typing import Dict, Any

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from mcp_client import MicrosoftStyleGuideClient
except ImportError:
    print("❌ Error: Could not import mcp_client.py")
    print("   Please ensure all files are in the same directory")
    sys.exit(1)

class QuickStartDemo:
    """Quick start demonstration of Microsoft Style Guide MCP Server."""
    
    def __init__(self):
        """Initialize the demo."""
        self.client = MicrosoftStyleGuideClient()
        
        # Demo content samples
        self.demo_content = {
            "excellent": """
            Welcome to our new feature! You can easily set up your account in just a few steps.
            
            Here's how to get started:
            1. Sign in to your account
            2. Go to Settings
            3. Choose your preferences
            4. Save your changes
            
            We're here to help if you need assistance!
            """,
            
            "needs_work": """
            The utilization of this functionality can be leveraged to facilitate the implementation 
            of advanced configurations which might be considered by users who are perhaps interested 
            in exploring the various options that are available to them through the interface.
            
            Hey guys, this is a crazy feature! The master configuration controls the slave processes.
            You'll need to whitelist the trusted sources and blacklist the malicious ones.
            """,
            
            "terminology_demo": """
            To setup your e-mail account, go to the web-site and login using your user-name.
            The A.I. system will help configure your WiFi settings for real time synchronization.
            """,
            
            "voice_demo": """
            You should perhaps consider utilizing the advanced functionality to facilitate
            optimal performance. The user might want to leverage the configuration options
            that are available through the interface.
            """
        }
    
    async def setup(self) -> bool:
        """Set up the demo environment."""
        print("🔧 Setting up demo environment...")
        
        # Check for server file
        if not Path("mcp_server.py").exists():
            print("❌ Error: mcp_server.py not found")
            print("   Please ensure the MCP server file is in the same directory")
            return False
        
        # Connect to server
        if not await self.client.connect("mcp_server.py"):
            print("❌ Error: Could not connect to MCP server")
            print("   Please check that dependencies are installed: pip install -r requirements.txt")
            return False
        
        print("✅ Demo environment ready!")
        return True
    
    async def cleanup(self):
        """Clean up demo environment."""
        if self.client:
            await self.client.disconnect()
    
    def print_header(self, title: str):
        """Print a formatted header."""
        print(f"\n{'='*60}")
        print(f"🎯 {title}")
        print(f"{'='*60}")
    
    def print_section(self, title: str):
        """Print a formatted section header."""
        print(f"\n📋 {title}")
        print("-" * 40)
    
    async def demo_comprehensive_analysis(self):
        """Demonstrate comprehensive content analysis."""
        self.print_header("Comprehensive Analysis Demo")
        
        print("Let's analyze two different pieces of content:")
        print("\n🟢 EXCELLENT CONTENT:")
        print(self.demo_content["excellent"][:100] + "...")
        
        print("\n🔴 CONTENT THAT NEEDS WORK:")
        print(self.demo_content["needs_work"][:100] + "...")
        
        # Analyze excellent content
        self.print_section("Analysis of Excellent Content")
        result = await self.client.analyze_content(self.demo_content["excellent"], "comprehensive")
        if result["success"]:
            print(self._extract_summary(result["result"]))
        else:
            print(f"❌ Analysis failed: {result['error']}")
        
        # Analyze problematic content
        self.print_section("Analysis of Content That Needs Work")
        result = await self.client.analyze_content(self.demo_content["needs_work"], "comprehensive")
        if result["success"]:
            print(self._extract_summary(result["result"]))
        else:
            print(f"❌ Analysis failed: {result['error']}")
    
    async def demo_voice_tone_analysis(self):
        """Demonstrate voice and tone analysis."""
        self.print_header("Voice & Tone Analysis Demo")
        
        print("Microsoft Style Guide focuses on three key voice principles:")
        print("• 🤗 Warm and relaxed (natural, conversational)")
        print("• ✨ Crisp and clear (direct, scannable)")
        print("• 🤝 Ready to help (action-oriented, supportive)")
        
        self.print_section("Analyzing Voice and Tone")
        result = await self.client.analyze_content(self.demo_content["voice_demo"], "voice_tone")
        if result["success"]:
            print(self._extract_voice_scores(result["result"]))
        else:
            print(f"❌ Analysis failed: {result['error']}")
    
    async def demo_terminology_check(self):
        """Demonstrate terminology checking."""
        self.print_header("Terminology Standards Demo")
        
        print("Microsoft has specific terminology standards:")
        print("• AI (not A.I.) • email (not e-mail) • website (not web site)")
        print("• sign in (not login) • setup (noun) vs set up (verb)")
        
        self.print_section("Checking Terminology")
        print("Sample text with terminology issues:")
        print(f'"{self.demo_content["terminology_demo"].strip()}"')
        
        result = await self.client.analyze_content(self.demo_content["terminology_demo"], "terminology")
        if result["success"]:
            print("\n" + self._extract_terminology_issues(result["result"]))
        else:
            print(f"❌ Analysis failed: {result['error']}")
    
    async def demo_accessibility_check(self):
        """Demonstrate accessibility and inclusive language checking."""
        self.print_header("Accessibility & Inclusive Language Demo")
        
        print("Microsoft emphasizes inclusive, bias-free communication:")
        print("• Use 'everyone' instead of 'guys'")
        print("• Use 'allow list' instead of 'whitelist'")
        print("• Use 'primary/secondary' instead of 'master/slave'")
        
        self.print_section("Checking for Accessibility Issues")
        result = await self.client.analyze_content(self.demo_content["needs_work"], "accessibility")
        if result["success"]:
            print(self._extract_accessibility_issues(result["result"]))
        else:
            print(f"❌ Analysis failed: {result['error']}")
    
    async def demo_improvement_suggestions(self):
        """Demonstrate improvement suggestions."""
        self.print_header("Improvement Suggestions Demo")
        
        print("Get specific suggestions to improve your content:")
        
        self.print_section("Getting Improvement Suggestions")
        result = await self.client.suggest_improvements(self.demo_content["voice_demo"], "all")
        if result["success"]:
            print(self._extract_suggestions(result["result"]))
        else:
            print(f"❌ Suggestions failed: {result['error']}")
    
    async def demo_style_guidelines(self):
        """Demonstrate style guidelines retrieval."""
        self.print_header("Style Guidelines Demo")
        
        print("Access Microsoft Style Guide principles directly:")
        
        self.print_section("Voice Guidelines")
        result = await self.client.get_style_guidelines("voice")
        if result["success"]:
            print("✅ Voice guidelines retrieved (sample):")
            print("   • Use contractions for natural tone")
            print("   • Write like you speak")
            print("   • Be helpful and supportive")
        else:
            print(f"❌ Guidelines failed: {result['error']}")
    
    async def demo_command_line_usage(self):
        """Demonstrate command line usage."""
        self.print_header("Command Line Usage Demo")
        
        print("You can use the MCP client from the command line:")
        print()
        
        print("📁 Analyze a file:")
        print("   python mcp_client.py --mode file --file document.md")
        print()
        
        print("📝 Analyze text:")
        print('   python mcp_client.py --mode text --text "Your content here"')
        print()
        
        print("💬 Interactive mode:")
        print("   python mcp_client.py --mode interactive")
        print()
        
        print("📚 Get guidelines:")
        print("   python mcp_client.py --mode guidelines --category voice")
        print()
        
        print("🎯 Specific analysis types:")
        print("   --analysis-type voice_tone")
        print("   --analysis-type grammar")
        print("   --analysis-type terminology")
        print("   --analysis-type accessibility")
        print("   --analysis-type comprehensive (default)")
    
    async def demo_integration_info(self):
        """Show integration information."""
        self.print_header("Integration Information")
        
        print("🛠️ VSCode Integration:")
        print("   • Configure MCP server in VSCode settings")
        print("   • Real-time analysis as you write")
        print("   • Quick fixes and suggestions")
        print("   • See vscode_settings_template.json for setup")
        print()
        
        print("💬 GitHub Copilot Chat:")
        print("   • Use copilot_integration.py for chat commands")
        print("   • Example: @workspace analyze this content")
        print("   • Automatic PR analysis with GitHub Actions")
        print()
        
        print("🚀 GitHub Actions:")
        print("   • Automatic style checking on PRs")
        print("   • Comment-triggered analysis")
        print("   • See style-analysis.yml workflow file")
    
    def _extract_summary(self, result: str) -> str:
        """Extract key information from analysis result."""
        lines = result.split('\n')
        summary_lines = []
        
        for line in lines:
            if any(indicator in line for indicator in ['📊', '🎯', '✅', '⚠️', '❌']):
                summary_lines.append(line)
            if len(summary_lines) >= 8:  # Limit output
                break
        
        return '\n'.join(summary_lines) if summary_lines else "Analysis completed successfully"
    
    def _extract_voice_scores(self, result: str) -> str:
        """Extract voice and tone scores from result."""
        lines = result.split('\n')
        score_lines = []
        
        for line in lines:
            if '🎯 Voice & Tone Scores:' in line:
                score_lines.append(line)
            elif line.strip().startswith('✅') or line.strip().startswith('⚠️') or line.strip().startswith('❌'):
                if 'relaxed' in line.lower() or 'clear' in line.lower() or 'help' in line.lower():
                    score_lines.append(line)
        
        return '\n'.join(score_lines) if score_lines else "Voice scores calculated"
    
    def _extract_terminology_issues(self, result: str) -> str:
        """Extract terminology issues from result."""
        if 'issues found' in result.lower():
            return "✅ Terminology issues detected and suggestions provided"
        else:
            return "✅ No terminology issues found"
    
    def _extract_accessibility_issues(self, result: str) -> str:
        """Extract accessibility issues from result."""
        if any(term in result.lower() for term in ['guys', 'master', 'slave', 'blacklist', 'whitelist']):
            return "✅ Accessibility issues detected - suggestions provided for inclusive alternatives"
        else:
            return "✅ Accessibility analysis completed"
    
    def _extract_suggestions(self, result: str) -> str:
        """Extract improvement suggestions from result."""
        if 'suggestions' in result.lower():
            return "✅ Improvement suggestions generated successfully"
        else:
            return "✅ Suggestions analysis completed"
    
    async def run_full_demo(self):
        """Run the complete demonstration."""
        print("🚀 Microsoft Style Guide MCP Server - Quick Start Demo")
        print("This demo shows how to analyze content using Microsoft Style Guide principles")
        
        # Run all demos
        await self.demo_comprehensive_analysis()
        await self.demo_voice_tone_analysis()
        await self.demo_terminology_check()
        await self.demo_accessibility_check()
        await self.demo_improvement_suggestions()
        await self.demo_style_guidelines()
        await self.demo_command_line_usage()
        await self.demo_integration_info()
        
        # Final summary
        self.print_header("Demo Complete!")
        print("🎉 You've seen the key features of the Microsoft Style Guide MCP Server!")
        print()
        print("Next steps:")
        print("1. 🧪 Try the interactive mode: python mcp_client.py --mode interactive")
        print("2. 📄 Analyze your own files: python mcp_client.py --mode file --file yourfile.md")
        print("3. ⚙️  Set up VSCode integration using vscode_settings_template.json")
        print("4. 🤖 Configure GitHub Copilot Chat with copilot_integration.py")
        print("5. 📚 Read the full documentation in README.md")
        print()
        print("Happy writing! 📝✨")

async def main():
    """Main function for running the demo."""
    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            print("""
Microsoft Style Guide MCP Server - Quick Start Demo

Usage:
  python quickstart.py           # Run interactive demo
  python quickstart.py --help    # Show this help

This demo shows you how to:
• Analyze content for Microsoft Style Guide compliance
• Check voice and tone (warm, crisp, helpful)
• Verify terminology standards
• Ensure accessibility and inclusive language
• Get improvement suggestions
• Access style guidelines
• Use command line tools
• Set up VSCode and GitHub Copilot integration

Requirements:
• Python 3.8+
• MCP server and client files
• Dependencies: pip install -r requirements.txt
            """)
            return
    
    demo = QuickStartDemo()
    
    try:
        # Set up demo
        if not await demo.setup():
            return 1
        
        # Run the demonstration
        await demo.run_full_demo()
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
        return 1
    except Exception as e:
        print(f"\n\n❌ Demo failed: {e}")
        return 1
    finally:
        await demo.cleanup()

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)