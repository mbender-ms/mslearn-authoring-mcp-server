#!/bin/bash

echo "Microsoft Style Guide FastMCP Server"
echo "====================================="
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "Error: Python is not installed or not in PATH"
        echo "Please install Python 3.8 or higher"
        exit 1
    fi
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "Using Python $PYTHON_VERSION"

# Check if requirements are installed
echo "Checking dependencies..."
$PYTHON_CMD -c "import fastmcp" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    $PYTHON_CMD -m pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        echo "Please run: $PYTHON_CMD -m pip install -r requirements.txt"
        exit 1
    fi
fi

echo "Dependencies OK"
echo
echo "Starting server..."
echo "Press Ctrl+C to stop the server"
echo

$PYTHON_CMD server.py

echo
echo "Server stopped."
