# Microsoft Learn Authoring MCP Server (Python) - Usage Examples

## Quick Start Test

After setting up the server, try these examples in VSCode with GitHub Copilot:

## 1. Basic Style Guide Access

**Prompt:**
```
@mslearn-authoring fetch the welcome page from the Microsoft style guide
```

**Expected Response:**
- Formatted content from https://learn.microsoft.com/en-us/style-guide/welcome/
- Title and URL information
- Clean markdown content without navigation elements

## 2. Content Analysis Example

**Prompt:**
```
@mslearn-authoring analyze this content for style compliance:

"The software application enables users to login to the system. The program allows people to access their data. Mankind has always struggled with technology adoption."
```

**Expected Analysis:**
- Voice & tone suggestions (use "sign in" instead of "login")
- Bias-free communication flags ("mankind" → "people" or "everyone")
- Terminology corrections
- Overall compliance score

## 3. Content Outline Generation

**Prompt:**
```
@mslearn-authoring generate a tutorial outline for "Building REST APIs with Azure Functions" for intermediate developers
```

**Expected Outline:**
```json
{
  "topic": "Building REST APIs with Azure Functions",
  "content_type": "tutorial",
  "target_audience": "intermediate",
  "outline": [
    "Overview and Prerequisites",
    "Getting Started",
    "Step-by-step Instructions",
    "Examples and Code Samples",
    "Troubleshooting",
    "Next Steps"
  ],
  "style_guide_reminders": [
    "Use active voice and conversational tone",
    "Address the reader directly with 'you'",
    "Keep sentences clear and concise",
    "Use inclusive, bias-free language"
  ]
}
```

## 4. Style Guide Search

**Prompt:**
```
@mslearn-authoring search the style guide for "accessibility"
```

**Expected Results:**
- Relevant sections containing accessibility information
- Snippet previews
- Relevance scores
- Direct links to full content

## 5. Advanced Workflow Example

**Multi-step Content Creation Workflow:**

1. **Research Phase:**
   ```
   @mslearn-authoring search the style guide for "voice and tone"
   ```

2. **Planning Phase:**
   ```
   @mslearn-authoring generate a concept outline for "Microsoft Graph API Overview" for mixed audience
   ```

3. **Writing Phase:**
   ```
   @mslearn-authoring analyze this draft for compliance:
   
   "Microsoft Graph API is a powerful tool that developers use to access Microsoft 365 data. You can use it to build applications that integrate with Office, Teams, and other Microsoft services."
   ```

4. **Reference Phase:**
   ```
   @mslearn-authoring fetch content from /en-us/style-guide/bias-free-communication in markdown format
   ```

## 6. Common Content Issues to Test

### Bias Language Detection
```
Test content: "The guys on the development team created a blacklist of IP addresses that the system considers harmful."

Expected suggestions:
- Replace "guys" with "developers" or "team members"
- Replace "blacklist" with "blocked list" or "deny list"
```

### Voice and Tone Improvements
```
Test content: "It is recommended that the configuration be updated by the administrator."

Expected suggestions:
- Use active voice: "We recommend that administrators update the configuration"
- More conversational: "You should update the configuration"
```

### Terminology Consistency
```
Test content: "Users can log in to the web site to access the e-mail application."

Expected suggestions:
- Use "sign in" instead of "log in"
- Use "website" instead of "web site"
- Use "email" instead of "e-mail"
```

## 7. Testing Different Content Types

### Tutorial Content
```
@mslearn-authoring generate a tutorial outline for "Setting up CI/CD with GitHub Actions" for beginners
```

### Reference Documentation
```
@mslearn-authoring generate a reference outline for "Azure REST API Error Codes" for advanced developers
```

### Conceptual Content
```
@mslearn-authoring generate a concept outline for "Understanding Microservices Architecture" for intermediate audience
```

## 8. Style Guide Navigation

**Extract full structure:**
```
@mslearn-authoring extract all sections from the style guide with subsections
```

**Access specific sections:**
```
@mslearn-authoring fetch content from /en-us/style-guide/top-10-tips-style-voice in text format
```

## 9. Debugging Commands

If something isn't working, try these diagnostic prompts:

```
@mslearn-authoring fetch content from /en-us/style-guide/welcome/ in html format
```

This will help you see the raw HTML structure if markdown parsing has issues.

## 10. Integration with Writing Workflow

**Content Creation Workflow:**

1. **Start with research:** Search style guide for your topic
2. **Create outline:** Generate structure based on content type and audience
3. **Write draft:** Create your content
4. **Analyze compliance:** Check against style guide
5. **Refine:** Use suggestions to improve content
6. **Final check:** Re-analyze to ensure compliance

**Example session:**
```
User: I need to write documentation for Azure Cognitive Services
Assistant: I'll help you create compliant Microsoft Learn content.

@mslearn-authoring search the style guide for "API documentation"
@mslearn-authoring generate a tutorial outline for "Getting Started with Azure Cognitive Services" for mixed audience
@mslearn-authoring fetch content from /en-us/style-guide/top-10-tips-style-voice for reference
```

## Pro Tips

1. **Use specific paths:** When fetching content, use the full path like `/en-us/style-guide/bias-free-communication`
2. **Specify format:** Choose markdown for editing, HTML for structure analysis, text for word counting
3. **Combine tools:** Use search to find relevant guidelines, then fetch full content
4. **Iterate on analysis:** Fix issues one category at a time (voice, bias, terminology)
5. **Save outlines:** Use generated outlines as templates for similar content types

## Python-Specific Troubleshooting

### Direct Server Testing

Before testing in VSCode, verify the server works independently:

```bash
# Activate virtual environment if used
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Test server directly
python mslearn_authoring_server.py

# Check dependencies
python -c "import mcp, requests, bs4, markdownify; print('All dependencies OK')"

# Test with setup script
python test_server.py
```

### Common Python Issues

**Import errors:**
```bash
# Reinstall dependencies
pip install --upgrade mcp requests beautifulsoup4 markdownify lxml

# Check virtual environment is activated
which python  # Should point to venv if using virtual environment
```

**Path issues:**
```bash
# Check PYTHONPATH
python -c "import sys; print('\\n'.join(sys.path))"

# Verify current directory
pwd  # Should be in project directory
```

**Virtual environment not working:**
```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## VSCode Integration Troubleshooting

If the server isn't working in VSCode:

1. **Test connection:**
   ```
   @mslearn-authoring extract style guide sections
   ```
   This should return basic structure data

2. **Check network access:**
   ```
   @mslearn-authoring fetch content from /en-us/style-guide/welcome/
   ```
   Should return the welcome page content

3. **Verify analysis function:**
   ```
   @mslearn-authoring analyze this text: "Hello world"
   ```
   Should return a basic analysis even for simple text

4. **Check VSCode configuration:**
   - Ensure Python path is correct in `.vscode/mcp.json`
   - Use absolute paths if relative paths don't work
   - Restart VSCode after configuration changes
   - Check VSCode output panel for error messages