# Using a Python Alpine base image
FROM python:3.10-alpine

# Set working directory in container
WORKDIR /oc-lettings

# Copy the rest of the application into the container
ADD . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-privileged user that the app will run under.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Switch to the non-privileged user to run the application.
USER appuser

# Expose the port on which the application will run
EXPOSE 8080

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
