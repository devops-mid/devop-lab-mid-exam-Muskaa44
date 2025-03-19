# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask app
EXPOSE 5000

# Set environment variable to disable buffering
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

