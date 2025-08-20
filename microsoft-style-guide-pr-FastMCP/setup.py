#!/usr/bin/env python3
"""
Setup script for Microsoft Style Guide FastMCP Server
"""

import subprocess
import sys
import os
from pathlib import Path


def install_requirements():
    """Install Python requirements."""
    print("Installing Python requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install requirements: {e}")
        return False


def verify_installation():
    """Verify that all required packages are installed."""
    print("Verifying installation...")
    try:
        import fastmcp
        import pydantic
        print("✓ All required packages are available!")
        return True
    except ImportError as e:
        print(f"✗ Missing package: {e}")
        return False


def create_start_script():
    """Create a start script for the server."""
    print("Creating start script...")
    
    if os.name == 'nt':  # Windows
        script_content = '''@echo off
echo Starting Microsoft Style Guide MCP Server...
python server.py
pause
'''
        with open("start_server.bat", "w") as f:
            f.write(script_content)
        print("✓ Created start_server.bat")
    else:  # Unix-like systems
        script_content = '''#!/bin/bash
echo "Starting Microsoft Style Guide MCP Server..."
python3 server.py
'''
        with open("start_server.sh", "w") as f:
            f.write(script_content)
        os.chmod("start_server.sh", 0o755)
        print("✓ Created start_server.sh")


def main():
    """Main setup function."""
    print("Microsoft Style Guide FastMCP Server Setup")
    print("=" * 50)
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Install requirements
    if not install_requirements():
        print("\nSetup failed. Please install requirements manually:")
        print("  pip install -r requirements.txt")
        return False
    
    # Verify installation
    if not verify_installation():
        print("\nSetup failed. Please check your Python installation.")
        return False
    
    # Create start script
    create_start_script()
    
    print("\n" + "=" * 50)
    print("✓ Setup completed successfully!")
    print("\nTo start the server:")
    if os.name == 'nt':
        print("  Double-click start_server.bat")
        print("  OR run: python server.py")
    else:
        print("  Run: ./start_server.sh")
        print("  OR run: python3 server.py")
    
    print("\nThe server provides the following tools:")
    print("  - search_style_guide: Search for style guide content")
    print("  - get_style_guide_entry: Get complete entry content")
    print("  - get_term_guidance: Get guidance for specific terms")
    print("  - list_categories: List all available categories")
    print("  - get_writing_guidance: Get writing guidance on topics")
    
    return True


if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
