# Using a Python Alpine base image
FROM python:3.10-alpine

# Set working directory in container
WORKDIR /app

# Copy the rest of the application into the container
ADD . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and switch to that user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Expose the port on which the application will run
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
