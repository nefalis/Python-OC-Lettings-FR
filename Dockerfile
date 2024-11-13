# Using a Python Alpine base image
FROM python:3.10-alpine

# Set working directory in container
WORKDIR /oc-lettings

# Copy the rest of the application into the container
COPY . .

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
RUN mkdir -p /oc-lettings/staticfiles /oc-lettings/logs && \
    touch /oc-lettings/logs/django_debug.log && \
    chown -R appuser /oc-lettings/staticfiles /oc-lettings/logs && \
    chmod -R 755 /oc-lettings/staticfiles /oc-lettings/logs

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
