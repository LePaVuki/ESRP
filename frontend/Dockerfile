FROM python:alpine3.20

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . ESRP
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user

