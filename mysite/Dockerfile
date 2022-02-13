FROM python:3.9-slim

# installing need python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -U pip==22.0.3 setuptools==51.0.0 \
        && pip install --no-cache-dir -r /app/requirements.txt

# copy codes to container
WORKDIR /app
COPY . /app

ENV PYTHONIOENCODING utf8
