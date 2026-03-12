# RPG Web App Skeleton

This Django project provides a basic skeleton for an RPG-style interface.

## Features

- Top `#sprite-container` for future character sprites
- Clickable text box that types out messages and advances on click
- Three dummy sentences included for testing

## Getting started

1. Activate the Python virtualenv (if not already):
   ```bash
   source ../.venv/bin/activate
   ```
2. Install dependencies (Django is already installed):
   ```bash
   pip install -r requirements.txt  # if you add requirements later
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Start development server:
   ```bash
   python manage.py runserver
   ```
5. Open http://127.0.0.1:8000/ in your browser.

Click the text area to cycle through the demo sentences.
