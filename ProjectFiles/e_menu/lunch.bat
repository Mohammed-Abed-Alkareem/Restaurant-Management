@echo off
REM Change directory to the location of the e_menu_app.py script
cd /d "%~dp0"

REM Setting the FLASK_APP environment variable
set FLASK_APP=e_menu_app.py

REM (Optional) Setting the FLASK_ENV environment variable to development for debugging purposes
set FLASK_ENV=development

REM Run the Flask application
flask run --host=0.0.0.0 --port=1111

REM Pause the command window so it doesn't close immediately
pause
