# Using a Python Alpine base image
FROM python:3.10-alpine

# Set working directory in container
WORKDIR /oc-lettings

# Copy the rest of the application into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# # Create a non-privileged user that the app will run under.
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# # Switch to the non-privileged user to run the application.
# USER appuser

# execute les migration et cree base de donnée
RUN python manage.py migrate

# permet de prendre les fichiers statics et les mettre dans staticfiles
RUN python manage.py collectstatic --noinput

# Expose the port on which the application will run
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
