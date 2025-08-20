# Microsoft Style Guide MCP Server

A professional Model Context Protocol (MCP) server implementation for analyzing content against the **official Microsoft Writing Style Guide**. This tool provides seamless integration with **VS Code**, **GitHub Copilot Chat**, and other MCP-compatible AI tools to help content creators ensure their writing follows Microsoft's style principles: **warm and relaxed**, **crisp and clear**, and **ready to help**.

## 🚀 Two Server Versions

### 🌐 **Web-Enabled Version** (`mcp_server_web.py`) - **Recommended**
- **Fetches live guidance** from the official Microsoft Style Guide website
- Always up-to-date with the latest style guide changes
- Provides real official content and examples from Microsoft Learn
- Requires internet connection for comprehensive analysis

### 📚 **Offline Version** (`mcp_server.py`)
- Built-in style guide rules and patterns
- Fast local analysis without internet dependency
- Perfect for secure environments or offline work
- Provides links to official documentation for detailed guidance

## ✨ Key Features

- **🔍 Official Style Guide Integration**: Fetches current guidance from Microsoft Learn
- **🛠️ VS Code Integration**: Seamless MCP protocol integration with automated setup
- **💬 AI Chat Compatible**: Works with GitHub Copilot, Claude, and other MCP-enabled AI tools
- **📊 Comprehensive Analysis**: Voice/tone, grammar, terminology, and accessibility checking
- **⚡ One-Command Setup**: Fully automated installation and configuration
- **🌐 Always Current**: Web version stays synchronized with official style guide updates

## 🚀 Quick Installation

### Prerequisites
- **Python 3.8+**
- **VS Code** (for IDE integration)
- **Internet connection** (for web-enabled version)

### One-Command Setup

```bash
# Clone or download this repository
git clone https://github.com/your-username/mslearn-authoring-mcp-server.git
cd mslearn-authoring-mcp-server

# Run automated setup (chooses web version by default)
python setup_script.py
```

**That's it!** The setup script will:
- ✅ Install Python dependencies
- ✅ Configure VS Code MCP integration
- ✅ Set up AI chat tool compatibility
- ✅ Test server functionality
- ✅ Create all necessary configuration files

### Advanced Setup Options

```bash
# Auto-select web version (default)
python setup_script.py --auto

# Force offline version
python setup_script.py --offline

# Skip all prompts with environment variable
set AUTOMATED_SETUP=true & python setup_script.py
```

## 📁 Project Structure

```
mslearn-authoring-mcp-server/
├── mcp_server.py              # Offline MCP server implementation
├── mcp_server_web.py          # Web-enabled MCP server (recommended)
├── mcp_client.py              # Client for testing and interaction
├── mcp_manifest.json          # MCP server manifest for VS Code
├── setup_script.py            # Automated installation script
├── requirements.txt           # Python dependencies
└── README.md                  # This documentation
```

## 📖 Usage

### Command Line Interface

#### Quick Test
```bash
# Test with simple text (web version)
python mcp_client.py --mode text --text "Your content here"

# Interactive mode
python mcp_client.py --mode interactive

# Analyze a specific file
python mcp_client.py --mode file --file document.md
```

#### Available Analysis Types
- `comprehensive` - Complete style analysis (default)
- `voice_tone` - Voice and tone compliance
- `grammar` - Grammar and style patterns
- `terminology` - Terminology consistency
- `accessibility` - Inclusive language checking

### VS Code Integration

After running the setup script, the MCP server is automatically configured in VS Code:

1. **Automatic Configuration**: Setup script creates all necessary VS Code settings
2. **MCP Server Detection**: Server appears in MCP-compatible extensions
3. **AI Chat Integration**: Works with GitHub Copilot Chat and other AI tools
4. **Real-time Analysis**: Content analysis through MCP protocol

#### Using with GitHub Copilot Chat

In VS Code, use Copilot Chat with commands like:
```
@workspace analyze this document for Microsoft Style Guide compliance
@workspace check the voice and tone of this content
@workspace suggest style improvements for this text
```

### Direct MCP Integration

For developers integrating with other MCP clients:

```python
# Server connection parameters
{
  "command": "python",
  "args": ["path/to/mcp_server_web.py"],
  "env": {
    "PYTHONPATH": "path/to/project"
  }
}
```

## 🎯 Microsoft Style Guide Principles

This tool analyzes content based on Microsoft's core principles:

### Voice and Tone
- **Warm and Relaxed**: Use contractions, natural language
- **Crisp and Clear**: Direct, scannable content under 25 words per sentence
- **Ready to Help**: Action-oriented, supportive language

### Grammar and Style Standards
- **Active Voice**: "You can configure settings" vs "Settings can be configured"
- **Second Person**: Address readers as "you"
- **Imperative Mood**: Use for instructions (Click, Choose, Select)
- **Scannable Format**: Use headers, bullets, and short paragraphs

### Terminology Consistency
| Preferred | Avoid | Context |
|-----------|-------|---------|
| AI | A.I. | No periods in abbreviation |
| email | e-mail | One word |
| sign in (verb) | login, log in | Microsoft standard |
| website | web site | One word |

### Accessibility and Inclusion
- Use "everyone" instead of "guys"
- Use "allow list" instead of "whitelist"
- People-first language: "people with disabilities"

## 📊 Example Analysis Output

### Web-Enabled Version
```
📋 Microsoft Style Guide Analysis

✅ Good - Minor improvements suggested

📊 Text Statistics:
   • Words: 45 | Sentences: 3 | Avg: 15.0 words/sentence

🔍 Issues Found: 2
   • Voice/Tone: Use more contractions for natural tone
   • Accessibility: Consider "everyone" instead of "users"

🌐 Official Microsoft Guidance:
   Voice and tone - Use contractions like "it's" and "you're" 
   to create a friendly, approachable tone...

📎 Reference: https://learn.microsoft.com/en-us/style-guide/voice-tone
```

### Offline Version
```
📋 Microsoft Style Guide Analysis

⚠️ Minor style issues detected

📊 Text Statistics:
   Words: 45 | Sentences: 3 | Avg: 15.0 words/sentence

🔍 Issues Found: 2
   • Voice/Tone: Consider more conversational language
   • Terminology: Check official Microsoft terms

🌐 For detailed guidance:
   https://learn.microsoft.com/en-us/style-guide
```

## 🛠️ Development and Testing

### Running Tests
```bash
# Test server functionality
python mcp_client.py --mode text --text "Test content"

# Verify web version connectivity
python -c "import mcp_server_web; print('Web server OK')"

# Check offline version
python -c "import mcp_server; print('Offline server OK')"
```

### Server Configuration

Both servers expose these MCP tools:
- `analyze_content` - Main analysis function
- `get_style_guidelines` - Retrieve specific guidelines  
- `suggest_improvements` - Get improvement recommendations
- `search_style_guide` - Search official documentation (web version only)

## 🐛 Troubleshooting

### Common Issues

**Setup Script Fails**
```bash
# Check Python version
python --version  # Should be 3.8+

# Install dependencies manually
pip install -r requirements.txt
```

**VS Code Integration Not Working**
- Restart VS Code completely after running setup
- Check that MCP-compatible extensions are installed
- Verify server appears in extension settings

**Web Version Connection Issues**
- Check internet connectivity
- Verify firewall allows Python to access microsoft.com
- Try offline version as fallback

### Debug Mode
```bash
# Run with verbose output
python mcp_client.py --mode text --text "test" --verbose

# Check server logs
python mcp_server_web.py  # Should start without errors
```

## 🔧 Configuration Options

### Environment Variables
```bash
# Force specific server version
set MCP_SERVER_VERSION=web
set MCP_SERVER_VERSION=offline

# Enable debug logging
set MCP_DEBUG=true

# Skip VS Code configuration
set SKIP_VSCODE_CONFIG=true
```

### VS Code Settings
The setup script creates comprehensive VS Code configuration:
- MCP server registration
- Multiple extension compatibility
- Automatic server discovery
- Debug configuration

## 🤝 Contributing

1. Fork this repository
2. Create a feature branch
3. Follow Microsoft Style Guide principles in code and documentation
4. Test with both server versions
5. Submit a pull request

### Development Setup
```bash
git clone your-fork-url
cd mslearn-authoring-mcp-server
python setup_script.py --auto
# Make changes and test
python mcp_client.py --mode interactive
```

## 📚 References

- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [VS Code MCP Integration](https://code.visualstudio.com/)

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## ⚠️ Disclaimer

This tool is not officially affiliated with Microsoft. It's an independent implementation based on publicly available Microsoft Style Guide principles and documentation.

---

**Built for better technical writing and communication** ✨

For questions or issues, please check the troubleshooting section or create an issue in this repository.
