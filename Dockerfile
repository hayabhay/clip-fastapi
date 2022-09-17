# Start with official python base image
FROM python:3.10-slim

RUN apt-get update && \
    apt-get upgrade -y

# Set working directory to app
WORKDIR /api

# Copy base & prod requirements
COPY ./requirements /requirements

# Pip install requirements
RUN pip install --upgrade pip
# For CPU only
RUN pip install --no-cache-dir --upgrade -r /requirements/requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Copy app
COPY ./api /api

# For faster model load time, prevent redownload of models everytime a container is started
# by directly adding model weights into the docker image.
# By default, clip downloads models to ~/.cache/clip and this is overridden in the code to read from a `models` directory in the app
COPY ./models /models

# Run uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
