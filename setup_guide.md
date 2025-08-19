# Microsoft Learn Content Authoring MCP Server (Python)

A Model Context Protocol (MCP) server designed specifically for authoring and editing Microsoft Learn content, with integrated Microsoft Writing Style Guide compliance checking.

## 🚀 Features

- **Fetch Style Guide Content**: Access any page from the Microsoft Writing Style Guide
- **Style Compliance Analysis**: Analyze your content against Microsoft's style guidelines
- **Content Outline Generation**: Generate structured outlines following Microsoft documentation standards
- **Style Guide Search**: Search across the Microsoft Writing Style Guide
- **Section Extraction**: Extract navigation and structure from style guide pages

## 📋 Prerequisites

- **Python 3.8 or higher**
- **Visual Studio Code** with GitHub Copilot extension
- **pip** package manager (included with Python)

## 🛠️ Installation

### Step 1: Create the Project

```bash
# Create project directory
mkdir mslearn-authoring-mcp-server
cd mslearn-authoring-mcp-server
```

### Step 2: Set Up Python Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

**Option A: Using requirements.txt**
```bash
# Create and install from requirements.txt
pip install -r requirements.txt
```

**Option B: Using pyproject.toml (if you have modern pip)**
```bash
# Install in development mode
pip install -e .
```

**Option C: Manual installation**
```bash
# Install core dependencies
pip install mcp requests beautifulsoup4 markdownify lxml
```

### Step 4: Create the Server File

Create `mslearn_authoring_server.py` and copy the Python server code from the first artifact.

### Step 5: Test the Installation

```bash
# Test the server runs without errors
python mslearn_authoring_server.py --help
```

## 🔧 VSCode Configuration

### Option 1: Workspace Configuration (Recommended)

Create `.vscode/mcp.json` in your workspace:

```json
{
  "mcpServers": {
    "mslearn-authoring": {
      "command": "python",
      "args": ["mslearn_authoring_server.py"],
      "cwd": "/full/path/to/mslearn-authoring-mcp-server",
      "env": {
        "PYTHONPATH": "."
      }
    }
  }
}
```

### Option 2: User Settings Configuration

Add to your VSCode User Settings (`settings.json`):

```json
{
  "mcp.servers": {
    "mslearn-authoring": {
      "command": "python",
      "args": ["/full/path/to/mslearn-authoring-mcp-server/mslearn_authoring_server.py"],
      "env": {
        "PYTHONPATH": "/full/path/to/mslearn-authoring-mcp-server"
      }
    }
  }
}
```

### Option 3: Use MCP: Add Server Command

1. Open Command Palette (`Cmd/Ctrl + Shift + P`)
2. Search for "MCP: Add Server"
3. Select "Local (stdio)"
4. Enter server name: `mslearn-authoring`
5. Enter command: `python`
6. Enter args: `["mslearn_authoring_server.py"]`
7. Set working directory to your project path

### Virtual Environment Configuration

If using a virtual environment, update the command path:

```json
{
  "mcpServers": {
    "mslearn-authoring": {
      "command": "/full/path/to/mslearn-authoring-mcp-server/venv/bin/python",
      "args": ["mslearn_authoring_server.py"],
      "cwd": "/full/path/to/mslearn-authoring-mcp-server"
    }
  }
}
```

**Windows users**: Use `venv\Scripts\python.exe` instead.

## 🎯 Usage Examples

Once configured, you can use the server with GitHub Copilot in VS Code:

### Fetch Style Guide Content

```
@mslearn-authoring fetch the Microsoft style guide welcome page in markdown format
```

### Analyze Content for Style Compliance

```
@mslearn-authoring analyze this content for Microsoft style guide compliance:

"Users should login to the application using their credentials. The software program will then validate the authentication."
```

### Generate Content Outline

```
@mslearn-authoring generate a tutorial outline for "Setting up Azure Functions" targeting intermediate developers
```

### Search Style Guide

```
@mslearn-authoring search the style guide for "accessibility"
```

### Extract Style Guide Sections

```
@mslearn-authoring extract all sections from the Microsoft Writing Style Guide
```

## 🔧 Available Tools

1. **fetch_style_guide_content**
   - Fetches content from Microsoft Learn Style Guide pages
   - Supports markdown, HTML, and text output formats
   - Example paths: `/en-us/style-guide/welcome/`, `/en-us/style-guide/bias-free-communication`

2. **analyze_style_compliance**
   - Analyzes text for Microsoft Writing Style Guide compliance
   - Checks voice & tone, bias-free language, and terminology
   - Provides actionable suggestions and compliance scores

3. **extract_style_guide_sections**
   - Extracts navigation and section structure from style guide pages
   - Useful for understanding the complete style guide organization

4. **search_style_guide**
   - Searches across Microsoft Writing Style Guide content
   - Returns relevant sections with snippets and relevance scores

5. **generate_content_outline**
   - Creates structured outlines following Microsoft documentation standards
   - Supports different content types: tutorial, concept, reference, how-to, overview
   - Includes style guide reminders and audience considerations

## 🚨 Troubleshooting

### Python/Virtual Environment Issues

**Server not starting:**
```bash
# Check Python version
python --version  # Should be 3.8+

# Verify dependencies
pip list | grep -E "(mcp|requests|beautifulsoup4)"

# Test server directly
python mslearn_authoring_server.py
```

**Import errors:**
```bash
# Reinstall dependencies
pip install --upgrade mcp requests beautifulsoup4 markdownify lxml

# Check PYTHONPATH
python -c "import sys; print(sys.path)"
```

### VSCode MCP Issues

**Server not recognized:**
1. Restart VSCode after adding configuration
2. Check Command Palette: "MCP: Restart Servers"
3. Verify absolute paths in configuration
4. Check VSCode output panel for MCP errors

**Permission errors (macOS/Linux):**
```bash
# Make script executable
chmod +x mslearn_authoring_server.py

# Or use absolute python path
which python  # Use this path in config
```

### Network/Access Issues

**SSL/Certificate errors:**
```bash
# Update certificates
pip install --upgrade certifi

# Or install with trust hosts
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org mcp
```

**Connection timeouts:**
- Ensure internet access to learn.microsoft.com
- Check firewall settings
- Try from command line: `curl https://learn.microsoft.com/en-us/style-guide/welcome/`

## 🎨 Development and Customization

### Project Structure
```
mslearn-authoring-mcp-server/
├── mslearn_authoring_server.py    # Main server code
├── requirements.txt               # Dependencies
├── pyproject.toml                # Project configuration (optional)
├── README.md                     # Documentation
├── .vscode/
│   └── mcp.json                  # VSCode MCP config
└── venv/                         # Virtual environment (if used)
```

### Adding New Features

The server is designed to be extensible. You can:

- Add more style guide rules to the compliance checker
- Integrate with additional Microsoft Learn APIs
- Add support for other Microsoft documentation sites
- Implement content validation for specific document types

### Running in Development Mode

```bash
# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run with debug output
python -u mslearn_authoring_server.py

# Format code
black mslearn_authoring_server.py

# Type checking
mypy mslearn_authoring_server.py
```

## 📦 Distribution

### Creating a Package

```bash
# Build distribution
python -m build

# Install from local package
pip install dist/mslearn_authoring_mcp_server-1.0.0-py3-none-any.whl
```

### Using as CLI Tool

After installation, you can run:
```bash
mslearn-authoring-mcp-server
```

## 🔄 Updating

```bash
# Update dependencies
pip install --upgrade mcp requests beautifulsoup4 markdownify

# Pull latest code changes
git pull origin main

# Restart VSCode MCP servers
# Command Palette: "MCP: Restart Servers"
```

## 📝 Contributing

1. Fork the repository
2. Create a virtual environment: `python -m venv venv`
3. Install development dependencies: `pip install -e ".[dev]"`
4. Make your changes
5. Run tests: `pytest`
6. Format code: `black .`
7. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🤝 Support

For issues and questions:
- Check the troubleshooting section above
- Review VSCode MCP server documentation
- Test the server directly with `python mslearn_authoring_server.py`
- Open an issue in the project repository

## 🌟 Tips for Success

1. **Use absolute paths** in VSCode configuration to avoid path issues
2. **Activate virtual environment** before running if you created one
3. **Test server independently** before configuring in VSCode
4. **Check Python version** - needs to be 3.8 or higher
5. **Restart VSCode** after configuration changes
6. **Monitor output panel** in VSCode for error messages

---

**Happy authoring with Python! 🐍🚀**