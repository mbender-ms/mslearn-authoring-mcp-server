# mslearn-authoring-mcp-server

A Model Context Protocol (MCP) server for authoring and editing Microsoft Learn content, with integrated Microsoft Writing Style Guide compliance checking.

## 🚀 Features

- **Fetch Style Guide Content:** Access any page from the Microsoft Writing Style Guide.
- **Style Compliance Analysis:** Analyze your content against Microsoft's style guidelines.
- **Content Outline Generation:** Generate structured outlines following Microsoft documentation standards.
- **Style Guide Search:** Search across the Microsoft Writing Style Guide.
- **Section Extraction:** Extract navigation and structure from style guide pages.

## 📋 Prerequisites

- Python 3.8 or higher
- Visual Studio Code (with GitHub Copilot extension suggested)
- `pip` package manager

## ⚙️ Installation

1. **Clone this repository** and navigate to the project directory.

2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install mcp requests beautifulsoup4 markdownify lxml
   ```

4. **Configure the server:**
   - Create a file named `mslearn_authoring_server.py` with your server code.

5. **Test your setup:**
   ```bash
   python mslearn_authoring_server.py --help
   ```

## 🛠 VSCode Integration

Configure VSCode with a `.vscode/mcp.json` file for local MCP server development, or adjust your user settings as needed.

## 🌟 Usage Examples

- **Fetch Style Guide Page:**
  ```
  @mslearn-authoring fetch the Microsoft style guide welcome page in markdown format
  ```
- **Analyze Content for Compliance:**
  ```
  @mslearn-authoring analyze this content for Microsoft style guide compliance:

  "Users should login to the application using their credentials. The software program will then validate the authentication."
  ```
- **Generate a Tutorial Outline:**
  ```
  @mslearn-authoring generate a tutorial outline for "Setting up Azure Functions" targeting intermediate developers
  ```
- **Search the Style Guide:**
  ```
  @mslearn-authoring search the style guide for "accessibility"
  ```
- **Extract Guide Sections:**
  ```
  @mslearn-authoring extract all sections from the Microsoft Writing Style Guide
  ```

See [`usage_examples.md`](usage_examples.md) for more workflow and troubleshooting tips.

## 🗂 Project Structure

```
mslearn-authoring-mcp-server/
├── mslearn_authoring_server.py    # Main server code
├── requirements.txt               # Dependencies
├── README.md                      # Documentation
├── setup_guide.md                 # Setup and configuration guide
├── usage_examples.md              # Example prompts and workflows
├── .vscode/
│   └── mcp.json                   # VSCode MCP config (optional)
└── venv/                          # Virtual environment (if used)
```

## 🤝 Contributing

1. Fork this repository.
2. Create a virtual environment (`python -m venv venv`).
3. Install dev dependencies (`pip install -e .[dev]`).
4. Make your changes.
5. Run tests (`pytest`), format code (`black .`).
6. Submit a pull request.

## 📄 License

MIT License – see LICENSE for details.

## 🆘 Support

- Read the troubleshooting section in `setup_guide.md`.
- Open an issue in this repository.
- Test the server directly with `python mslearn_authoring_server.py`.

---

**Happy authoring with Python! 🚀**
