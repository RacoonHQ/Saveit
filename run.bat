@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
SET SCRIPT_DIR=%~dp0
CD /D "%SCRIPT_DIR%"

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.9+ first.
    pause
    exit /b 1
)

pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo pip is not installed. Please install pip.
    pause
    exit /b 1
)

IF NOT EXIST ".env" (
    echo Creating .env file...
    copy ".env.example" ".env" >nul
    set /p API_ID="Enter your API_ID: "
    set /p API_HASH="Enter your API_HASH: "
    set /p HANDLER="Enter your HANDLER (e.g., .saveit): "
    
    (echo API_ID_1=%API_ID%
    echo API_HASH_1=%API_HASH%
    echo HANDLER=%HANDLER%) > .env
)

pip install --upgrade telethon python-dotenv pillow

echo Starting SaveIt Bot...
python Saveit.py
echo Done.
pause