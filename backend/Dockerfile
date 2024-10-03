# Using a base image of slim and pyhon
FROM python:3.13.0rc3-slim-bullseye AS fastapi

# Setup an app user so the container doesn't run as the root user
RUN useradd -ms /bin/bash apiuser
USER apiuser
WORKDIR /src

# Install the application dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy in the source code
COPY ./app app
