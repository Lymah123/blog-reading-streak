# Use a specific version of the Python image for consistency
FROM python:3.12-slim

# Set environment variables to avoid Python writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Install system dependencies (optional, based on your needs)
# Example: libpq-dev, build-essential, etc. (remove this if not needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies in a separate layer to leverage Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your application runs on
EXPOSE 5000

# Define the default command to run your application
CMD ["python", "app.py"]
