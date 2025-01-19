# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential iputils-ping

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME=World

# Add entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Run the application
CMD ["poetry", "run", "start"]