# Use the official Python runtime image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy django project to the container app folder
COPY . .

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the django port
EXPOSE 8000

# Rund django's developement server
CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]