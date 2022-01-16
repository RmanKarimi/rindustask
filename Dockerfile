FROM ubuntu:bionic
ENV LANG C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3.7-dev python3-pip libpq-dev curl \
  && apt-get clean all \
  && rm -rf /var/lib/apt/lists/*
WORKDIR /opt/webapp
COPY . .
RUN pip3 install -U pip \
    && pip3 install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
