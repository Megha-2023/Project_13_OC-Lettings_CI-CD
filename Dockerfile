# Use the official Python runtime image
FROM python:3.12

# Create teg app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Install application dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy django project to the container app folder
COPY . /app/

# Expose the django port
EXPOSE 8000

# Rund django's developement server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]