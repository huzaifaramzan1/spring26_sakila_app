# 1. Use a slim base image to reduce size
FROM python:3.9-slim

# Add labels for metadata
LABEL maintainer="Your Name"
LABEL version="1.0"
LABEL description="Optimized Sakila Flask Application"

# Set working directory
WORKDIR /app

# 2. Leverage layer caching: Copy only requirements first
# (Note: Create a requirements.txt file in your repo if you don't have one)
COPY requirements.txt .

# 3. Install dependencies in a single layer
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the application code
COPY . .

# 5. Create a non-root user for security and switch to it
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# 6. Expose ONLY the Flask port
EXPOSE 5000

# 7. Add a healthcheck to ensure the container is actually running
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Start the application
CMD ["python", "app.py"]