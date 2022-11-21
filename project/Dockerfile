FROM python:3.9-alpine

WORKDIR /src
ENV PYTHONUNBUFFERED 1
COPY . /src/
RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt