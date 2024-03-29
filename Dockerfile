# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install pipenv
COPY ./docker/Pipfile ./docker/Pipfile.lock /app/
RUN pipenv install --system

# Copy project
COPY ./src/ /app/

# Copy entry point
COPY ./docker/entrypoint.sh /app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
