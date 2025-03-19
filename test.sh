#!/bin/bash
echo "Running tests..."

# Stop script if any command fails
set -e

# Run tests using pytest with coverage
pytest --disable-warnings --cov=app tests/

echo "Tests completed successfully."

