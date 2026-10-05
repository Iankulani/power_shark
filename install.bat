@echo off
REM ============================================================================
REM POWER-SHARK v1.0.0 - Windows Installation Script
REM ============================================================================

setlocal EnableDelayedExpansion

REM Colors (using ANSI escape codes - Windows 10+)
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do set "ESC=%%b"
set "RED=%ESC%[91m"
set "GREEN=%ESC%[92m"
set "YELLOW=%ESC%[93m"
set "CYAN=%ESC%[96m"
set "WHITE=%ESC%[97m"
set "BOLD=%ESC%[1m"
set "RESET=%ESC%[0m"

REM Configuration
set "SCRIPT_DIR=%~dp0"
set "INSTALL_DIR=%USERPROFILE%\power-shark"
set "VENV_DIR=%INSTALL_DIR%\venv"
set "PYTHON_MIN=3.7"

REM ============================================================================
REM Banner
REM ============================================================================
echo %CYAN%%BOLD%
echo ================================================================================
echo                                                                              
echo    ██████╗  ██████╗ ██╗    ██╗███████╗██████╗     ███████╗██╗  ██╗ █████╗ ██████╗██╗  ██╗
echo    ██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗    ██╔════╝██║  ██║██╔══██╗██╔══██╗██║ ██╔╝
echo    ██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝    ███████╗███████║███████║██████╔╝█████╔╝ 
echo    ██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗    ╚════██║██╔══██║██╔══██║██╔══██╗██╔═██╗ 
echo    ██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║    ███████║██║  ██║██║  ██║██║  ██║██║  ██╗
echo    ╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
echo                                                                              
echo                     POWER-SHARK v1.0.0 - Windows Installer                  
echo                          Author: Ian Carter Kulani, MSc                     
echo                                                                              
echo ================================================================================
echo %RESET%

REM ============================================================================
REM Check Admin
REM ============================================================================
echo %CYAN%[INFO]%RESET% Checking administrator privileges...
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%[!]%RESET% Not running as Administrator. Some features will be limited.
    echo %YELLOW%[!]%RESET% For full functionality, right-click and "Run as Administrator"
) else (
    echo %GREEN%[+]%RESET% Running with administrator privileges
)

REM ============================================================================
REM Check Python
REM ============================================================================
echo.
echo %CYAN%[INFO]%RESET% Checking Python installation...

python --version >nul 2>&1
if %errorLevel% neq 0 (
    python3 --version >nul 2>&1
    if %errorLevel% neq 0 (
        echo %RED%[X]%RESET% Python not found!
        echo %YELLOW%[!]%RESET% Please install Python 3.7+ from https://python.org
        echo %YELLOW%[!]%RESET% Make sure to check "Add Python to PATH" during installation.
        pause
        exit /b 1
    ) else (
        set "PYTHON_CMD=python3"
    )
) else (
    set "PYTHON_CMD=python"
)

for /f "tokens=2" %%i in ('%PYTHON_CMD% --version 2^>^&1') do set "PYTHON_VERSION=%%i"
echo %GREEN%[+]%RESET% Found Python %PYTHON_VERSION%

REM ============================================================================
REM Check pip
REM ============================================================================
%PYTHON_CMD% -m pip --version >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%[!]%RESET% pip not found. Installing...
    %PYTHON_CMD% -m ensurepip --upgrade
)

REM ============================================================================
REM Create Install Directory
REM ============================================================================
echo.
echo %CYAN%[INFO]%RESET% Creating installation directory...
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
    echo %GREEN%[+]%RESET% Created %INSTALL_DIR%
) else (
    echo %GREEN%[+]%RESET% Directory exists: %INSTALL_DIR%
)

REM ============================================================================
REM Create Virtual Environment
REM ============================================================================
echo.
echo %CYAN%[INFO]%RESET% Setting up virtual environment...

if not exist "%VENV_DIR%" (
    %PYTHON_CMD% -m venv "%VENV_DIR%"
    if %errorLevel% neq 0 (
        echo %RED%[X]%RESET% Failed to create virtual environment
        pause
        exit /b 1
    )
    echo %GREEN%[+]%RESET% Virtual environment created
) else (
    echo %GREEN%[+]%RESET% Virtual environment exists
)

call "%VENV_DIR%\Scripts\activate.bat"

REM ============================================================================
REM Upgrade pip
REM ============================================================================
echo.
echo %CYAN%[INFO]%RESET% Upgrading pip...
python -m pip install --upgrade pip setuptools wheel

REM ============================================================================
REM Install Python Dependencies
REM ============================================================================
echo.
echo %CYAN%[INFO]%RESET% Installing Python dependencies...

if exist "%SCRIPT_DIR%requirements.txt" (
    pip install -r "%SCRIPT_DIR%requirements.txt"
) else (
    echo %YELLOW%[!]%RESET% requirements.txt not found. Installing core packages...
    pip install colorama requests psutil dnspython cryptography paramiko pynput scapy flask flask-socketio flask-cors discord.py telethon slack-sdk reportlab whois qrcode pyshorteners beautifulsoup4 pyperclip python-dotenv tabulate
)

if %errorLevel% neq 0 (
    echo %YELLOW%[!]%RESET% Some packages may have failed to install
)

REM ============================================================================
REM Install Optional Windows Tools
REM ============================================================================
echo.
echo %CYAN%[INFO]%RESET% Checking for optional Windows tools...

where nmap >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%[!]%RESET% nmap not found. Install from https://nmap.org/download.html
) else (
    echo %GREEN%[+]%RESET% nmap found
)

where curl >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%[!]%RESET% curl not found. Windows 10+ should have it built-in.
) else (
    echo %GREEN%[+]%RESET% curl found
)

REM ============================================================================
REM Copy Files
REM ============================================================================
echo.
echo %CYAN%[INFO]%RESET% Installing POWER-SHARK files...

if exist "%SCRIPT_DIR%power_shark.py" (
    copy /Y "%SCRIPT_DIR%power_shark.py" "%INSTALL_DIR%\" >nul
    echo %GREEN%[+]%RESET% Copied power_shark.py
) else if exist "%SCRIPT_DIR%#!usrbinenv python3.txt" (
    copy /Y "%SCRIPT_DIR%#!usrbinenv python3.txt" "%INSTALL_DIR%\power_shark.py" >nul
    echo %GREEN%[+]%RESET% Copied power_shark.py
) else (
    echo %RED%[X]%RESET% power_shark.py not found!
)

if exist "%SCRIPT_DIR%requirements-check.py" (
    copy /Y "%SCRIPT_DIR%requirements-check.py" "%INSTALL_DIR%\" >nul
    echo %GREEN%[+]%RESET% Copied requirements-check.py
)

if exist "%SCRIPT_DIR%requirements.txt" (
    copy /Y "%SCRIPT_DIR%requirements.txt" "%INSTALL_DIR%\" >nul
    echo %GREEN%[+]%RESET% Copied requirements.txt
)

REM Create data directories
mkdir "%INSTALL_DIR%\.power_shark" 2>nul
mkdir "%INSTALL_DIR%\power_shark_reports" 2>nul

REM ============================================================================
REM Create Launcher
REM ============================================================================
echo.
echo %CYAN%[INFO]%RESET% Creating launcher...

(
echo @echo off
echo call "%VENV_DIR%\Scripts\activate.bat"
echo python "%INSTALL_DIR%\power_shark.py" %%*
) > "%INSTALL_DIR%\power-shark.bat"

echo %GREEN%[+]%RESET% Created power-shark.bat

REM ============================================================================
REM Create Desktop Shortcut
REM ============================================================================
echo.
set /p CREATE_SHORTCUT="Create desktop shortcut? (y/n): "
if /i "!CREATE_SHORTCUT!"=="y" (
    powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut([Environment]::GetFolderPath('Desktop') + '\POWER-SHARK.lnk'); $SC.TargetPath = '%INSTALL_DIR%\power-shark.bat'; $SC.WorkingDirectory = '%INSTALL_DIR%'; $SC.IconLocation = '%SystemRoot%\System32\shell32.dll,13'; $SC.Save()"
    echo %GREEN%[+]%RESET% Desktop shortcut created
)

REM ============================================================================
REM Verify Installation
REM ============================================================================
echo.
echo %CYAN%[INFO]%RESET% Verifying installation...

if exist "%INSTALL_DIR%\requirements-check.py" (
    python "%INSTALL_DIR%\requirements-check.py"
)

REM ============================================================================
REM Complete
REM ============================================================================
echo.
echo %GREEN%%BOLD%
echo ================================================================================
echo                     ✅ INSTALLATION COMPLETE!
echo ================================================================================
echo %RESET%
echo.
echo %WHITE%To run POWER-SHARK:%RESET%
echo   %CYAN%cd %INSTALL_DIR%%RESET%
echo   %CYAN%power-shark.bat%RESET%
echo.
echo %WHITE%Or double-click the desktop shortcut%RESET%
echo.
echo %YELLOW%Note: Some features require Administrator privileges%RESET%
echo %YELLOW%      Right-click power-shark.bat and select "Run as administrator"%RESET%
echo.

pause
endlocal
