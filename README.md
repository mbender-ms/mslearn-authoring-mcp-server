# Microsoft Style Guide MCP Server

A comprehensive Model Context Protocol (MCP) server and client implementation for analyzing content against the **official Microsoft Writing Style Guide**. This tool integrates seamlessly with **VSCode** and **GitHub Copilot Chat** to help content developers ensure their writing follows Microsoft's style principles: **warm and relaxed**, **crisp and clear**, and **ready to lend a hand**.

## 🚀 Two Versions Available

### 📚 **Standard Version** (`mcp_server.py`)
- Built-in style guide rules and patterns
- Fast local analysis without internet dependency
- Perfect for basic style checking and offline use
- Provides links to official documentation for detailed guidance

### 🌐 **Web-Enabled Version** (`mcp_server_web.py`) 
- **Fetches live guidance** from the official Microsoft Style Guide website
- Always up-to-date with the latest style guide changes
- Provides real official content and examples
- Requires internet connection for full functionality

## 🎯 Features

- **🔍 Live Style Guide Integration**: Fetches current guidance from official Microsoft docs
- **🛠️ VSCode Integration**: Real-time analysis through MCP protocol
- **💬 GitHub Copilot Chat**: Interactive style checking and suggestions
- **📊 Multiple Analysis Types**: Choose comprehensive, voice/tone, grammar, terminology, or accessibility focus
- **💡 Official Guidance**: Get real recommendations directly from Microsoft Style Guide
- **🌐 Always Current**: Web version stays updated with official style guide changes
- **⚡ Fast Local Analysis**: Standard version provides instant feedback

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** 
- **VSCode** with MCP support
- **GitHub Copilot** (for chat integration)

### 1. Choose Your Version

**For most users, we recommend the Web-Enabled Version** for the most accurate, up-to-date guidance.

```bash
# Web-Enabled Version (Recommended)
python setup_script.py --server mcp_server_web.py

# OR Standard Version (Offline-capable)
python setup_script.py --server mcp_server.py
```

### 2. Automated Setup (Recommended)

```bash
# 1. Create project directory
mkdir microsoft-style-guide-mcp
cd microsoft-style-guide-mcp

# 2. Save all project files to this directory
# (both mcp_server.py and mcp_server_web.py, mcp_client.py, requirements.txt, setup_script.py)

# 3. Run automated setup with your preferred version
python setup_script.py
```

The setup script will:
- ✅ Check Python version compatibility
- ✅ Install required dependencies
- ✅ Test MCP server functionality  
- ✅ Configure VSCode integration
- ✅ Set up GitHub Copilot Chat integration
- ✅ Create test files and examples

### 2. Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Test the installation
python mcp_client.py --mode interactive

# Analyze a file
python mcp_client.py --mode file --file README.md
```

## 🔧 Configuration

### Choosing the Right Version

| Feature | Standard Version | Web-Enabled Version |
|---------|------------------|---------------------|
| **Internet Required** | ❌ No | ✅ Yes |
| **Speed** | ⚡ Very Fast | 🌐 Fast (with caching) |
| **Accuracy** | ✅ Good | 🎯 Excellent (official source) |
| **Up-to-date** | ⚠️ Manual updates needed | ✅ Always current |
| **Official Content** | 📎 Links only | 📚 Full content |
| **Use Case** | Offline work, basic checking | Production use, detailed guidance |

**Recommendation**: Use the **Web-Enabled Version** (`mcp_server_web.py`) for production work where you need the most accurate, current guidance from the official Microsoft Style Guide.

### VSCode Integration

Both versions work identically with VSCode. The setup script creates `.vscode/settings.json` with MCP configuration:

```json
{
  "mcpServers": {
    "microsoft-style-guide": {
      "command": "python",
      "args": ["/absolute/path/to/mcp_server_web.py"],
      "env": {
        "PYTHONPATH": "/absolute/path/to/project"
      }
    }
  }
}
```

**Manual VSCode Setup:**
1. Open VSCode in your project directory
2. Install the MCP extension (if available)
3. Update paths in `.vscode/settings.json` to absolute paths
4. Restart VSCode

### GitHub Copilot Chat Integration

Use the provided `copilot_integration.py` script:

```bash
# Analyze content
python copilot_integration.py analyze "Your content here"

# Voice and tone check
python copilot_integration.py voice "Welcome to our app!"

# Get improvement suggestions
python copilot_integration.py improve "The user should utilize the functionality"

# Get style guidelines
python copilot_integration.py guidelines
```

## 📖 Usage

### Command Line Interface

#### Interactive Mode
```bash
python mcp_client.py --mode interactive
```

**Available commands:**
- `analyze [text]` - Comprehensive style analysis
- `voice [text]` - Voice and tone analysis
- `grammar [text]` - Grammar and style check
- `terms [text]` - Terminology consistency
- `access [text]` - Accessibility and bias check
- `improve [text]` - Get improvement suggestions
- `file [path]` - Analyze a file
- `guidelines [category]` - Get style guidelines

#### Direct Analysis
```bash
# Analyze a file (Web-Enabled Version)
python mcp_client.py --mode file --file document.md --server mcp_server_web.py

# Analyze text with live guidance
python mcp_client.py --mode text --text "Your content here" --server mcp_server_web.py

# Get live style guidelines
python mcp_client.py --mode guidelines --category voice --server mcp_server_web.py

# Search the official style guide
python mcp_client.py --mode search --query "active voice examples"
```

### Analysis Types

| Type | Description | Standard Version | Web-Enabled Version |
|------|-------------|------------------|---------------------|
| `comprehensive` | Complete analysis (default) | ✅ Pattern matching | 🌐 Patterns + Official guidance |
| `voice_tone` | Voice and tone compliance | ✅ Basic scoring | 🌐 Official examples & tips |
| `grammar` | Grammar and style | ✅ Pattern detection | 🌐 Official writing tips |
| `terminology` | Terminology consistency | ✅ Basic checking | 🌐 Live A-Z word list |
| `accessibility` | Inclusive language | ✅ Pattern matching | 🌐 Official bias-free guide |

### VSCode Usage

Once configured, the MCP server provides:

1. **Real-time Analysis**: Automatic content checking
2. **Code Actions**: Quick fixes and suggestions
3. **Hover Information**: Style guide tips
4. **Commands**: Direct access to analysis tools

**Example VSCode Commands:**
- `Ctrl+Shift+P` → "Microsoft Style Guide: Analyze Document"
- `Ctrl+Shift+P` → "Microsoft Style Guide: Get Guidelines"

### GitHub Copilot Chat Commands

In Copilot Chat, use these patterns:

```
@workspace analyze this content for Microsoft Style Guide compliance
@workspace check the voice and tone of this text
@workspace suggest improvements for this writing
@workspace show Microsoft Style Guide rules for terminology
```

## 🎯 Microsoft Style Guide Principles

This tool analyzes content based on Microsoft's core principles:

### 1. Voice and Tone

**Warm and Relaxed**
- ✅ Use contractions (it's, you're, we'll)
- ✅ Natural, conversational language
- ❌ Avoid overly formal terms (utilize, leverage)

**Crisp and Clear**  
- ✅ Direct, scannable content
- ✅ Sentences under 25 words
- ❌ Avoid weak modifiers (very, really)

**Ready to Help**
- ✅ Action-oriented language (you can, let's, here's how)
- ✅ Supportive tone
- ❌ Avoid tentative language (maybe, perhaps)

### 2. Grammar and Style

- **Active Voice**: "You can configure settings" vs "Settings can be configured"
- **Second Person**: Address readers as "you"
- **Imperative Mood**: Use for instructions (Click, Choose, Select)
- **Parallel Structure**: Consistent formatting in lists

### 3. Terminology Standards

| Correct | Avoid | Note |
|---------|-------|------|
| AI | A.I. | No periods |
| email | e-mail | One word |
| sign in (verb) | login, log in | Microsoft standard |
| setup (noun) | set-up | One word as noun |
| website | web site | One word |
| Wi-Fi | WiFi, wifi | Hyphenated, both caps |

### 4. Accessibility and Inclusion

**Inclusive Language:**
- Use "everyone" instead of "guys"
- Use "allow list" instead of "whitelist"  
- Use "primary/secondary" instead of "master/slave"

**People-First Language:**
- "People with disabilities" not "disabled people"
- Focus on the person, not the condition

## 📊 Example Analysis Output

### Web-Enabled Version Output
```bash
📋 Microsoft Style Guide Analysis

✅ Good - Minor style improvements suggested

📊 Text Statistics:
   • Words: 45
   • Sentences: 3
   • Avg words/sentence: 15.0

🔍 Issues Detected: 2
   • Grammar/Style: 1
   • Voice/Tone: 0
   • Accessibility: 1

✅ Positive Elements: 2

🌐 Official Guidance: Fetched from Microsoft Style Guide

📚 Official Microsoft Style Guide Guidance:
**Issue Type:** Grammar
**Source:** Writing tips - Microsoft Style Guide
**URL:** https://learn.microsoft.com/en-us/style-guide/global-communications/writing-tips

**Official Guidance:**
Use active voice and indicative mood most of the time. Use imperative mood in procedures. 
Keep adjectives and adverbs close to the words they modify...

📎 Read Full Guidance: https://learn.microsoft.com/en-us/style-guide/global-communications/writing-tips
```

### Standard Version Output
```bash
📋 Microsoft Style Guide Analysis Summary
⚠️ Minor style issues detected

📊 Text Statistics:
   Words: 45
   Sentences: 3
   Avg words/sentence: 15.0

🔍 Issues Found: 2
   • Grammar/Style: 1
   • Terminology: 0
   • Accessibility: 1
   • Voice/Tone: 0

🌐 For detailed guidance, consult the official Microsoft Style Guide:
   https://learn.microsoft.com/en-us/style-guide

💡 Use the search_style_guide tool to get specific guidance for flagged issues.
```

## 🛠️ Development

### Project Structure

```
microsoft-style-guide-mcp/
├── mcp_server.py              # MCP server implementation
├── mcp_client.py              # MCP client and interfaces
├── requirements.txt           # Python dependencies
├── setup_script.py            # Automated setup
├── README.md                  # This documentation
├── test_document.md           # Sample test file
├── copilot_integration.py     # GitHub Copilot integration
├── vscode_mcp_config.json     # VSCode MCP configuration
├── vscode_settings_template.json # Complete VSCode settings
└── .vscode/
    └── settings.json          # VSCode MCP settings
```

### Running Tests

```bash
# Test server functionality
python -c "import mcp_server; print('Server OK')"

# Test client connection
python mcp_client.py --mode text --text "Test content"

# Test file analysis
python mcp_client.py --mode file --file test_document.md
```

### Extending the Analyzer

The `MicrosoftStyleAnalyzer` class in `mcp_server.py` can be extended with additional rules:

```python
# Add new terminology standards
self.terminology_standards["new_term"] = {
    "correct": "new-term",
    "avoid": ["newterm", "new term"],
    "note": "Use hyphenated form"
}

# Add new voice pattern
self.voice_guidelines["new_category"] = {
    "positive_patterns": [r"\b(helpful|pattern)\b"],
    "negative_patterns": [r"\b(avoid|this)\b"]
}
```

## 🐛 Troubleshooting

### Common Issues

**1. "Module not found" errors**
```bash
pip install -r requirements.txt
```

**2. VSCode MCP server not connecting**
- Ensure absolute paths in VSCode settings
- Check Python is in PATH
- Restart VSCode after configuration changes
- Verify MCP extension is installed

**3. "Server script not found"**
```bash
# Ensure files are in the same directory
ls -la mcp_server.py mcp_client.py
```

**4. Analysis returns empty results**
- Check file encoding (should be UTF-8)
- Verify file contains text content
- Ensure file is not binary

### Debug Mode

```bash
# Enable verbose logging
python mcp_client.py --mode interactive --verbose

# Test with simple content
python mcp_client.py --mode text --text "Hello world" --verbose
```

### VSCode Troubleshooting

1. **Check MCP Server Status**:
   - Open VSCode Developer Tools
   - Look for MCP connection logs
   - Verify server process is running

2. **Reset Configuration**:
   ```bash
   # Regenerate VSCode settings
   python setup_script.py
   ```

3. **Manual Configuration**:
   - Copy `vscode_mcp_config.json` content
   - Paste into VSCode `settings.json`
   - Update paths to absolute paths

## 📚 References

- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [VSCode MCP Integration](https://code.visualstudio.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes following Microsoft Style Guide principles
4. Test thoroughly with the provided test suite
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Issues**: Check troubleshooting section above
- **Style Guide Questions**: Refer to [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/)
- **MCP Questions**: Check [MCP Documentation](https://modelcontextprotocol.io/)

---

**Note**: This tool is not officially affiliated with Microsoft. It's an independent implementation based on publicly available Microsoft Style Guide principles.

Built with ❤️ for better technical writing and communication.