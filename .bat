@echo off
setlocal

:: Set project path and log file location
set PROJECT_DIR=set_your_project_dir
set LOG_FILE=%PROJECT_DIR%\logs\email_log.txt

:: Create logs folder if it doesn't exist
if not exist "%PROJECT_DIR%\logs" (
    mkdir "%PROJECT_DIR%\logs"
)

:: Go to project directory
cd /d "%PROJECT_DIR%"

:: Activate virtual environment and run script
(
    call your_venv_name\Scripts\activate.bat
    echo [%date% %time%] --- Script started ---
    python main.py
    echo [%date% %time%] --- Script finished successfully ---
) >> "%LOG_FILE%" 2>&1

endlocal
