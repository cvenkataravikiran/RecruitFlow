@echo off
REM RecruitFlow Quick Start Script for Windows

echo ========================================
echo RecruitFlow - Quick Start
echo ========================================
echo.

REM Check if setup has been run
if not exist "db.sqlite3" (
    echo First time setup detected...
    echo Running setup script...
    python setup.py
    if errorlevel 1 (
        echo.
        echo Setup failed! Please check the errors above.
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo Starting RecruitFlow Server...
echo ========================================
echo.
echo Server will be available at: http://localhost:8000
echo Admin panel at: http://localhost:8000/admin
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

pause
