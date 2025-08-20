@echo off
echo Microsoft Style Guide FastMCP Server
echo =====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
python -c "import fastmcp" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing dependencies...
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Error: Failed to install dependencies
        echo Please run: python -m pip install -r requirements.txt
        pause
        exit /b 1
    )
)

echo Dependencies OK
echo.
echo Starting server...
echo Press Ctrl+C to stop the server
echo.

python server.py

echo.
echo Server stopped.
pause
