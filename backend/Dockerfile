FROM python:3.13.0rc3-slim-bullseye

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . ESRP

# Setup an app user so the container doesn't run as the root user

