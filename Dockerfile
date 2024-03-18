# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies (like libpq-dev for PostgreSQL support)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*  # Clean up apt cache to reduce image size

# Copy the requirements.txt file into the container
COPY requirements.txt /usr/src/app/

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /usr/src/app/

# Expose port (typically 8000 for Django, adjust as needed)
EXPOSE 8000
