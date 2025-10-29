# Flask Calculator App

## Overview
A simple web-based calculator built with Flask that performs basic arithmetic operations (addition, subtraction, multiplication, division). The app features a clean, responsive UI and is configured for deployment on Render.

## Project Architecture
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Production Server**: Gunicorn
- **Deployment Target**: Render

## Recent Changes
- **2025-10-29**: Initial project setup
  - Created Flask application with calculator logic
  - Built responsive web interface with gradient design
  - Implemented error handling for division by zero and invalid inputs
  - Configured for Render deployment with Gunicorn

## File Structure
```
.
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Calculator UI template
├── static/
│   └── style.css       # Styling for the calculator
├── requirements.txt    # Python dependencies
└── replit.md          # Project documentation
```

## Features
- Basic arithmetic operations (add, subtract, multiply, divide)
- Error handling for division by zero
- Input validation
- Responsive design
- Clean, modern UI with gradient background
- Enter key support for calculations

## Running Locally
The app runs on port 5000 and binds to 0.0.0.0 for accessibility in cloud environments.

## Deployment on Render
The app is configured to run with Gunicorn for production deployment. Use the following start command on Render:
```
gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
```
