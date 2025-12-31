# Use Python 3.11 slim image as base for smaller size
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file first to leverage Docker layer caching
# This way, if only the code changes, dependencies don't need to be reinstalled
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY backoff.py .

# Run the application when container starts
CMD ["python", "backoff.py"]

