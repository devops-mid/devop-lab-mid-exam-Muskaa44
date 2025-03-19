#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e  

echo "Activating virtual environment (if applicable)..."
source venv/bin/activate || echo "No virtual environment found, proceeding without it."

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running database migrations..."
export FLASK_APP=app  # Set Flask entry point
flask db upgrade

echo "Starting the application..."
flask run --host=0.0.0.0 --port=5000


