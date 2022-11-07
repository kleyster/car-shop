FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /shop

WORKDIR /shop

ADD . /shop/

# Install any needed packages specified in requirements.txt
ADD requirements.txt /shop/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -Ur /shop/requirements.txt
