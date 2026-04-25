#!/bin/bash
# RecruitFlow Quick Start Script for Linux/Mac

echo "========================================"
echo "RecruitFlow - Quick Start"
echo "========================================"
echo ""

# Check if setup has been run
if [ ! -f "db.sqlite3" ]; then
    echo "First time setup detected..."
    echo "Running setup script..."
    python3 setup.py
    if [ $? -ne 0 ]; then
        echo ""
        echo "Setup failed! Please check the errors above."
        exit 1
    fi
fi

echo ""
echo "========================================"
echo "Starting RecruitFlow Server..."
echo "========================================"
echo ""
echo "Server will be available at: http://localhost:8000"
echo "Admin panel at: http://localhost:8000/admin"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 manage.py runserver
