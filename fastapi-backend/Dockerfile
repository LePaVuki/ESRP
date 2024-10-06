# Using a base image of slim and pyhon
FROM python@sha256:dbdf1a8e375131679547183a70bdb4f9c512946a4ae42de172d59b151c3da5b7 AS fastapi

# Setup an app user so the container doesn't run as the root user
RUN useradd -ms /bin/bash apiuser
USER apiuser
WORKDIR /src

# Install the application dependencies
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt --upgrade --no-cache-dir
# apt-get -y update && \
# apt-get install python3 postgresql-libs && \
# apt-get install --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
# apt-get --purge del .build-deps && \
# apt-get clean

# Copy in the source code
COPY ./src src

# CMD "python", "app/database.py"