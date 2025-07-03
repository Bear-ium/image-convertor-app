@echo off
setlocal

set "PYTHON_EXE=python3.12"
set "VENVDIR=venv"
set "VENV_PATH=%CD%\%VENVDIR%"
set "ACTIVATE_PATH=%VENV_PATH%\Scripts\activate.bat"
set "REQPATH=%CD%\requirements.txt"

:: Check if python3.12 is available
"%PYTHON_EXE%" --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: python3.12 not found in PATH.
    pause
    exit /b 1
)

:: Create venv if it doesn't exist
if NOT EXIST "%ACTIVATE_PATH%" (
    echo Creating virtual environment with python3.12...
    "%PYTHON_EXE%" -m venv "%VENV_PATH%"
) else (
    echo Virtual environment already exists.
)

:: Activate the virtual environment
call "%ACTIVATE_PATH%"

:: Install requirements
if EXIST "%REQPATH%" (
    echo Installing requirements...
    pip install --upgrade pip >nul
    pip install -r "%REQPATH%"
) else (
    echo No requirements.txt found.
)

:: Launch the app
echo.
echo Launching the image converter app...
python main.py

:: Leave terminal open
echo.
echo App closed. You may now use the Python shell or exit.
cmd /k
