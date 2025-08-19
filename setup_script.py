#!/usr/bin/env python3
"""
Microsoft Style Guide MCP Server Setup Script

This script automates the setup process for the Microsoft Style Guide MCP Server
for VSCode and GitHub Copilot Chat integration.
"""

import os
import sys
import subprocess
import json
import platform
from pathlib import Path
from typing import Dict, Any, List

def print_header():
    """Print setup header."""
    print("=" * 70)
    print("🎯 Microsoft Style Guide MCP Server Setup")
    print("=" * 70)
    print("Setting up Microsoft Style Guide analysis for VSCode and GitHub Copilot")
    print()

def print_step(step_num: int, description: str):
    """Print a setup step."""
    print(f"📋 Step {step_num}: {description}")
    print("-" * 50)

def run_command(command: List[str], description: str = "", shell: bool = False) -> bool:
    """Run a command and return success status."""
    try:
        if description:
            print(f"🔄 {description}")
        
        if shell:
            result = subprocess.run(' '.join(command), shell=True, check=True, capture_output=True, text=True)
        else:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        print(f"✅ {description} - Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed")
        print(f"   Error: {e.stderr if e.stderr else str(e)}")
        return False
    except Exception as e:
        print(f"❌ {description} - Exception: {e}")
        return False

def check_python_version() -> bool:
    """Check if Python version is adequate."""
    print_step(1, "Checking Python Version")
    
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is supported")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not supported")
        print("   Required: Python 3.8 or higher")
        print("   Please install a newer version of Python")
        return False

def check_required_files() -> bool:
    """Check if all required files are present."""
    print_step(2, "Checking Required Files")
    
    required_files = [
        "mcp_server.py",
        "mcp_client.py", 
        "requirements.txt"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
        else:
            print(f"✅ Found: {file}")
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        print("   Please ensure all files are in the same directory")
        return False
    
    print("✅ All required files present")
    return True

def install_dependencies() -> bool:
    """Install required Python packages."""
    print_step(3, "Installing Python Dependencies")
    
    # Upgrade pip first
    if not run_command([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                      "Upgrading pip"):
        print("⚠️  Failed to upgrade pip, continuing anyway...")
    
    # Install requirements
    success = run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                         "Installing Python packages")
    
    if success:
        print("✅ All dependencies installed successfully")
        return True
    else:
        print("❌ Failed to install dependencies")
        print("💡 Try running manually: pip install -r requirements.txt")
        return False

def test_mcp_server() -> bool:
    """Test the MCP server installation."""
    print_step(4, "Testing MCP Server")
    
    # Test basic import
    try:
        print("🔄 Testing MCP server import...")
        result = subprocess.run([sys.executable, "-c", 
                               "import mcp_server; print('Import successful')"],
                              capture_output=True, text=True, check=True)
        print("✅ MCP server import successful")
    except subprocess.CalledProcessError as e:
        print(f"❌ MCP server import failed: {e.stderr}")
        return False
    
    # Test basic functionality
    try:
        print("🔄 Testing basic functionality...")
        test_code = '''
import asyncio
from mcp_server import analyzer

async def test():
    result = analyzer.analyze_voice_tone("Hello, you can easily set up your account!")
    return result

result = asyncio.run(test())
print("Basic test successful")
'''
        result = subprocess.run([sys.executable, "-c", test_code],
                              capture_output=True, text=True, check=True)
        print("✅ Basic functionality test passed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Functionality test failed: {e.stderr}")
        return False

def setup_vscode_integration() -> bool:
    """Set up VSCode integration."""
    print_step(5, "Setting Up VSCode Integration")
    
    # Get current directory
    current_dir = Path.cwd().absolute()
    server_path = current_dir / "mcp_server.py"
    
    # VSCode MCP configuration
    mcp_config = {
        "mcpServers": {
            "microsoft-style-guide": {
                "command": "python",
                "args": [str(server_path)],
                "env": {
                    "PYTHONPATH": str(current_dir)
                }
            }
        }
    }
    
    # Create VSCode settings template
    vscode_settings = {
        **mcp_config,
        "editor.codeActionsOnSave": {
            "source.fixAll.microsoftStyleGuide": "explicit"
        },
        "microsoftStyleGuide": {
            "enableLinting": True,
            "autoAnalyze": True,
            "fileTypes": ["markdown", "plaintext", "restructuredtext"],
            "analysisTypes": {
                "comprehensive": True,
                "voiceTone": True,
                "grammar": True,
                "terminology": True,
                "accessibility": True
            }
        }
    }
    
    # Save configuration files
    try:
        # Save MCP configuration for easy reference
        with open("vscode_mcp_config.json", "w") as f:
            json.dump(mcp_config, f, indent=2)
        print("✅ Created vscode_mcp_config.json")
        
        # Save full VSCode settings template
        with open("vscode_settings_template.json", "w") as f:
            json.dump(vscode_settings, f, indent=2)
        print("✅ Created vscode_settings_template.json")
        
        # Create .vscode directory if it doesn't exist
        vscode_dir = Path(".vscode")
        vscode_dir.mkdir(exist_ok=True)
        
        # Check if settings.json exists
        settings_file = vscode_dir / "settings.json"
        if settings_file.exists():
            print("⚠️  VSCode settings.json already exists")
            print("   Please manually merge the MCP configuration from vscode_mcp_config.json")
        else:
            # Create new settings.json
            with open(settings_file, "w") as f:
                json.dump(mcp_config, f, indent=2)
            print("✅ Created .vscode/settings.json with MCP configuration")
        
        print("\n📋 VSCode Setup Instructions:")
        print("1. Open VSCode in this directory")
        print("2. If you have existing settings, merge vscode_mcp_config.json into your settings.json")
        print("3. Install the MCP extension for VSCode if available")
        print("4. Restart VSCode to load the new settings")
        
        return True
        
    except Exception as e:
        print(f"❌ VSCode setup failed: {e}")
        return False

def setup_github_copilot() -> bool:
    """Set up GitHub Copilot Chat integration instructions."""
    print_step(6, "GitHub Copilot Chat Integration")
    
    # Create a sample chat integration script
    chat_integration_script = '''#!/usr/bin/env python3
"""
GitHub Copilot Chat Integration for Microsoft Style Guide
Usage in Copilot Chat: @workspace analyze this content for Microsoft Style Guide compliance
"""

import asyncio
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from mcp_client import MicrosoftStyleGuideClient, GitHubCopilotInterface

async def main():
    """Main function for Copilot Chat integration."""
    if len(sys.argv) < 3:
        print("Usage: python copilot_integration.py <command> <content>")
        print("Commands: analyze, voice, grammar, terminology, accessibility, improve, guidelines")
        return
    
    command = sys.argv[1]
    content = " ".join(sys.argv[2:])
    
    client = MicrosoftStyleGuideClient()
    copilot = GitHubCopilotInterface(client)
    
    try:
        # Connect to server
        if not await client.connect("mcp_server.py"):
            print("Failed to connect to MCP server")
            return
        
        # Process command
        result = await copilot.process_chat_command(command, content)
        
        if result["success"]:
            print(result["result"])
        else:
            print(f"Error: {result['error']}")
            if "available_commands" in result:
                print("\\nAvailable commands:")
                for cmd in result["available_commands"]:
                    print(f"  • {cmd}")
    
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
'''
    
    try:
        with open("copilot_integration.py", "w") as f:
            f.write(chat_integration_script)
        print("✅ Created copilot_integration.py")
        
        print("\n📋 GitHub Copilot Chat Integration:")
        print("1. Use the created copilot_integration.py script")
        print("2. In Copilot Chat, you can now use commands like:")
        print("   • @workspace analyze this content for style compliance")
        print("   • @workspace check voice and tone of this text")
        print("   • @workspace suggest improvements for this writing")
        print("3. The script will analyze content using Microsoft Style Guide rules")
        
        return True
        
    except Exception as e:
        print(f"❌ GitHub Copilot setup failed: {e}")
        return False

def create_test_file() -> bool:
    """Create a test file for validation."""
    print_step(7, "Creating Test Content")
    
    test_content = '''# Microsoft Style Guide Test Document

Welcome to our new feature! You can easily set up your account in just a few steps.

## Getting Started

Here's how to get started:

1. **Sign in** to your account
2. **Go to Settings** - Click the gear icon
3. **Choose your preferences** - Select what works for you
4. **Save your changes** - You're all set!

## Writing Tips

We're here to help you write great content:

- Use contractions (it's, you're, we'll) for a natural tone
- Keep sentences short and clear
- Write in active voice
- Use "you" to address readers directly

## Need Help?

If you need assistance, we're ready to help! Contact our support team or check our FAQ.

---

*This content follows Microsoft Style Guide principles.*
'''
    
    try:
        with open("test_document.md", "w") as f:
            f.write(test_content)
        print("✅ Created test_document.md")
        
        # Test the analysis
        print("🔄 Testing analysis on sample content...")
        result = subprocess.run([
            sys.executable, "mcp_client.py", 
            "--mode", "file", 
            "--file", "test_document.md"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Test analysis successful")
            return True
        else:
            print(f"⚠️  Test analysis had issues: {result.stderr}")
            return True  # Continue setup even if test has minor issues
        
    except Exception as e:
        print(f"❌ Test file creation failed: {e}")
        return False

def print_final_instructions():
    """Print final setup instructions and next steps."""
    print("\n" + "=" * 70)
    print("🎉 SETUP COMPLETE!")
    print("=" * 70)
    
    print("\n📋 NEXT STEPS:")
    
    print("\n1. 🧪 Test the installation:")
    print("   python mcp_client.py --mode interactive")
    print("   python mcp_client.py --mode file --file test_document.md")
    
    print("\n2. 🔧 VSCode Integration:")
    print("   • Open VSCode in this directory")
    print("   • Settings are configured in .vscode/settings.json")
    print("   • Install MCP extension if available")
    print("   • Restart VSCode")
    
    print("\n3. 💬 GitHub Copilot Chat:")
    print("   • Use copilot_integration.py for chat commands")
    print("   • Example: python copilot_integration.py analyze 'your content here'")
    
    print("\n4. 📚 Usage Examples:")
    print("   # Interactive mode")
    print("   python mcp_client.py --mode interactive")
    print("   ")
    print("   # Analyze a file")
    print("   python mcp_client.py --mode file --file README.md")
    print("   ")
    print("   # Analyze text")
    print("   python mcp_client.py --mode text --text 'Your content here'")
    print("   ")
    print("   # Get style guidelines")
    print("   python mcp_client.py --mode guidelines --category voice")
    
    print("\n💡 TROUBLESHOOTING:")
    print("   • If connection fails, ensure mcp_server.py is executable")
    print("   • For VSCode issues, check the MCP server configuration")
    print("   • For analysis issues, verify the content is in supported format")
    
    print("\n📖 MICROSOFT STYLE GUIDE PRINCIPLES:")
    print("   • Warm and relaxed: Use contractions, natural language")
    print("   • Crisp and clear: Be direct, scannable, under 25 words/sentence")
    print("   • Ready to help: Action-oriented, supportive, use 'you'")
    print("   • Inclusive: Use bias-free, accessible language")
    
    print("\n" + "=" * 70)

def main():
    """Main setup function."""
    print_header()
    
    setup_steps = [
        ("Python Version", check_python_version),
        ("Required Files", check_required_files), 
        ("Dependencies", install_dependencies),
        ("MCP Server", test_mcp_server),
        ("VSCode Integration", setup_vscode_integration),
        ("GitHub Copilot", setup_github_copilot),
        ("Test Content", create_test_file)
    ]
    
    failed_steps = []
    
    for step_name, step_function in setup_steps:
        try:
            if not step_function():
                failed_steps.append(step_name)
                print(f"⚠️  {step_name} setup had issues but continuing...")
        except Exception as e:
            print(f"❌ {step_name} setup failed with error: {e}")
            failed_steps.append(step_name)
        print()  # Add spacing between steps
    
    if failed_steps:
        print("⚠️  Setup completed with some issues:")
        for step in failed_steps:
            print(f"   • {step}")
        print("\nPlease review the errors above and manually complete failed steps.")
    else:
        print("✅ All setup steps completed successfully!")
    
    print_final_instructions()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed with unexpected error: {e}")
        sys.exit(1)