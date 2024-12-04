# Using a Python Alpine base image
FROM python:3.10-alpine

# Set working directory in container
WORKDIR /oc-lettings

# Copy the rest of the application into the container
COPY . .

# Copy the static files into the container
COPY static /oc-lettings/static

# Install dependencies
RUN pip install -r requirements.txt

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

# Create the log file and set permissions
RUN mkdir -p /oc-lettings/staticfiles && \
    chown -R appuser:appuser /oc-lettings/staticfiles && \
    chmod -R 755 /oc-lettings/staticfiles

# Check permissions to debug
RUN ls -l /oc-lettings/staticfiles

# Switch to the non-privileged user to run the application.
USER appuser

# execute migration and create database
RUN python manage.py migrate

# allows you to take static files and put them in staticfiles
RUN python manage.py collectstatic --noinput

# Expose the port on which the application will run
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
