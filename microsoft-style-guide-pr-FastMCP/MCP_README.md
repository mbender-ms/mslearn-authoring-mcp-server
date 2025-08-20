# Microsoft Style Guide FastMCP Server

A Model Context Protocol (MCP) server that provides programmatic access to the Microsoft Style Guide documentation. This server allows AI assistants and other MCP clients to search, retrieve, and get guidance from the comprehensive Microsoft Style Guide.

## Features

- **Comprehensive Search**: Search across all style guide sections including A-Z terms, writing guidance, and product-specific guidelines
- **Term Lookup**: Get specific guidance for terms and phrases
- **Category Browsing**: List and browse organized categories
- **Writing Guidance**: Get detailed guidance on writing topics like capitalization, punctuation, and bias-free communication
- **Full Content Access**: Retrieve complete entries with metadata and formatting

## Available Tools

### 1. `search_style_guide`
Search the Microsoft Style Guide for content matching a query.

**Parameters:**
- `query` (string): Search term or phrase
- `category` (optional string): Filter by category ('a-z', 'punctuation', 'capitalization', etc.)
- `limit` (optional int): Maximum results to return (default: 10)

**Example:**
```json
{
  "query": "capitalization",
  "category": "writing",
  "limit": 5
}
```

### 2. `get_style_guide_entry`
Get the complete content of a specific style guide entry.

**Parameters:**
- `file_path` (string): Relative path to the markdown file

**Example:**
```json
{
  "file_path": "styleguide/capitalization.md"
}
```

### 3. `get_term_guidance`
Get specific guidance for a term or phrase.

**Parameters:**
- `term` (string): The term or phrase to look up

**Example:**
```json
{
  "term": "client/server"
}
```

### 4. `list_categories`
List all available categories and sections in the style guide.

**Parameters:** None

### 5. `get_writing_guidance`
Get specific writing guidance on topics.

**Parameters:**
- `topic` (string): Writing topic (e.g., 'capitalization', 'punctuation', 'bias-free')

**Example:**
```json
{
  "topic": "bias-free communication"
}
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start

1. **Run the setup script:**
   ```bash
   python setup.py
   ```
   
   This will:
   - Install required Python packages
   - Verify the installation
   - Create start scripts

2. **Start the server:**
   
   **Windows:**
   ```cmd
   start_server.bat
   ```
   or
   ```cmd
   python server.py
   ```
   
   **Linux/Mac:**
   ```bash
   ./start_server.sh
   ```
   or
   ```bash
   python3 server.py
   ```

### Manual Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the server:**
   ```bash
   python server.py
   ```

## Integration Guide

### VS Code Integration

#### Manual Setup

1. **Install the Copilot Chat extension** (if not already installed)
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "GitHub Copilot Chat"
   - Install the extension

2. **Configure MCP Server in VS Code**
   
   **Option A: Using settings.json**
   - Open VS Code Settings (Ctrl+,)
   - Click "Open Settings (JSON)" in the top right
   - Add the MCP server configuration:
   
   ```json
   {
     "github.copilot.chat.mcpServers": {
       "microsoft-style-guide": {
         "command": "python",
         "args": ["C:/Users/YourUsername/path/to/microsoft-style-guide-pr/server.py"],
         "env": {
           "PYTHONPATH": "C:/Users/YourUsername/path/to/microsoft-style-guide-pr"
         }
       }
     }
   }
   ```

   **Option B: Using VS Code Command Palette**
   - Open Command Palette (Ctrl+Shift+P)
   - Type "GitHub Copilot Chat: Add MCP Server"
   - Enter the server details when prompted

3. **Restart VS Code** to apply the changes

#### Agent-Assisted Setup

Ask GitHub Copilot Chat in VS Code:

> "Please help me configure an MCP server for the Microsoft Style Guide. The server is located at `C:/Users/YourUsername/path/to/microsoft-style-guide-pr/server.py` and I want it accessible in VS Code for style guide queries."

Or use this specific prompt:

> "I have a FastMCP server for Microsoft Style Guide at path `[YOUR_PATH]/server.py`. Please add it to my VS Code MCP configuration with the server name 'microsoft-style-guide'. The server requires Python to run and needs the server directory in PYTHONPATH."

### Claude Desktop Integration

#### Manual Setup

1. **Locate Claude Desktop configuration file**
   
   **Windows:**
   ```
   %APPDATA%/Claude/claude_desktop_config.json
   ```
   
   **macOS:**
   ```
   ~/Library/Application Support/Claude/claude_desktop_config.json
   ```
   
   **Linux:**
   ```
   ~/.config/Claude/claude_desktop_config.json
   ```

2. **Edit the configuration file**
   
   If the file doesn't exist, create it. Add or update the `mcpServers` section:
   
   ```json
   {
     "mcpServers": {
       "microsoft-style-guide": {
         "command": "python",
         "args": ["C:/path/to/microsoft-style-guide-pr/server.py"],
         "env": {
           "PYTHONPATH": "C:/path/to/microsoft-style-guide-pr"
         }
       }
     }
   }
   ```

3. **Restart Claude Desktop** to apply the changes

#### Agent-Assisted Setup

Ask Claude Desktop:

> "I need help configuring an MCP server for Microsoft Style Guide documentation. Can you help me add it to my Claude Desktop configuration? The server is a Python script located at `[YOUR_PATH]/server.py`."

Or use this detailed prompt:

> "Please help me configure Claude Desktop to use my Microsoft Style Guide MCP server. Here are the details:
> - Server name: microsoft-style-guide  
> - Command: python
> - Script path: [YOUR_ACTUAL_PATH]/server.py
> - Environment: PYTHONPATH should be set to the server directory
> 
> Can you show me the exact configuration and where to place it?"

### Configuration Examples

#### Windows Configuration
```json
{
  "mcpServers": {
    "microsoft-style-guide": {
      "command": "python",
      "args": ["C:/Users/YourUsername/Documents/microsoft-style-guide-pr/server.py"],
      "env": {
        "PYTHONPATH": "C:/Users/YourUsername/Documents/microsoft-style-guide-pr"
      }
    }
  }
}
```

#### macOS/Linux Configuration
```json
{
  "mcpServers": {
    "microsoft-style-guide": {
      "command": "python3",
      "args": ["/Users/YourUsername/Documents/microsoft-style-guide-pr/server.py"],
      "env": {
        "PYTHONPATH": "/Users/YourUsername/Documents/microsoft-style-guide-pr"
      }
    }
  }
}
```

#### Using Virtual Environment
```json
{
  "mcpServers": {
    "microsoft-style-guide": {
      "command": "/path/to/venv/bin/python",
      "args": ["/path/to/microsoft-style-guide-pr/server.py"],
      "env": {
        "PYTHONPATH": "/path/to/microsoft-style-guide-pr"
      }
    }
  }
}
```

### Testing Your Configuration

#### In VS Code
1. Open Copilot Chat panel
2. Ask: "Can you search the Microsoft Style Guide for guidance on API formatting?"
3. You should see the MCP server respond with style guide content

#### In Claude Desktop
1. Start a new conversation
2. Ask: "What does the Microsoft Style Guide say about capitalization rules?"
3. Claude should access the style guide through your MCP server

### Troubleshooting Integration

#### Common Issues

1. **Server not found**
   - Verify the path to `server.py` is correct
   - Use absolute paths instead of relative paths
   - Check that Python is accessible from the specified path

2. **Permission errors**
   - Ensure the server script has execute permissions
   - On Windows, try using `python.exe` instead of `python`
   - Check that the PYTHONPATH directory exists and is readable

3. **Configuration not loading**
   - Restart the client application after configuration changes
   - Verify JSON syntax is correct (use a JSON validator)
   - Check client application logs for MCP-related errors

#### Verification Steps

1. **Test server standalone:**
   ```bash
   cd /path/to/microsoft-style-guide-pr
   python server.py
   ```

2. **Check configuration file syntax:**
   - Use an online JSON validator
   - Ensure all paths use forward slashes or properly escaped backslashes

3. **Enable debug logging** (if supported by your client)
   - Look for MCP connection messages
   - Check for server startup errors

### Advanced Configuration

#### Environment Variables
You can also set environment variables for the server:

```json
{
  "mcpServers": {
    "microsoft-style-guide": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {
        "PYTHONPATH": "/path/to/microsoft-style-guide-pr",
        "STYLE_GUIDE_ROOT": "/path/to/microsoft-style-guide-pr",
        "MCP_DEBUG": "true"
      }
    }
  }
}
```

#### Multiple Server Configurations
You can configure multiple MCP servers:

```json
{
  "mcpServers": {
    "microsoft-style-guide": {
      "command": "python",
      "args": ["/path/to/microsoft-style-guide-pr/server.py"]
    },
    "other-mcp-server": {
      "command": "node",
      "args": ["/path/to/other-server/index.js"]
    }
  }
}
```

## Usage Examples

### Search for Terms
Ask your MCP client:
> "Search the Microsoft Style Guide for guidance on 'API' formatting"

### Get Specific Guidance
Ask your MCP client:
> "What's the Microsoft Style Guide guidance for 'client/server'?"

### Writing Topics
Ask your MCP client:
> "Show me the Microsoft guidance on bias-free communication"

### Browse Categories
Ask your MCP client:
> "What categories are available in the Microsoft Style Guide?"

## Content Coverage

This server provides access to:

- **Microsoft Style Guide** (`/styleguide/`): Public style guide with A-Z word lists, punctuation, and general writing guidance
- **Product Style Guide** (`/product-style-guide-msft-internal/`): Internal product-specific naming and terminology
- **Writing Style Guide** (`/writing-style-guide-msft-internal/`): Internal writing guidelines
- **Includes** (`/includes/`): Shared content snippets and specialized guidance

## Development

### Server Structure
- `server.py`: Main FastMCP server implementation
- `requirements.txt`: Python dependencies
- `setup.py`: Installation and setup script
- `mcp-config.json`: Example MCP client configuration

### Adding New Tools
To add new tools, modify the `_register_tools()` method in the `StyleGuideServer` class in `server.py`.

### Testing
You can test the server locally by running:
```bash
python server.py
```

The server will start and display available tools and their descriptions.

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all requirements are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. **File not found errors**: Ensure the server is running from the correct directory (the root of the microsoft-style-guide-pr repository).

3. **Permission errors**: On Unix-like systems, make sure the start script is executable:
   ```bash
   chmod +x start_server.sh
   ```

### Logs
The server outputs logs to the console. Check for any error messages when starting the server.

## Contributing

This FastMCP server is designed to work with the Microsoft Style Guide repository structure. When contributing:

1. Ensure the server can handle new directory structures
2. Update tool descriptions if functionality changes
3. Test with various search queries and terms
4. Maintain compatibility with the existing MCP protocol

## License

This project follows the same license as the Microsoft Style Guide repository.
