@echo off

:: Move to the directory where this script is located
cd /d %~dp0

:: Try to run with 'python' first
python currency_exchange.py

:: If it fails (errorlevel 1), try 'py' (the Windows launcher)
if %errorlevel% neq 0 (
    py currency_exchange.py
)

:: If both fail, then Python was not found. Python installation is needed.
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Python was not found. 
    echo Please ensure Python is installed and added to your PATH.
    pause
)