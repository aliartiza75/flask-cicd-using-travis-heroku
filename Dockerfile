FROM ubuntu:16.04
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

LABEL "DESCRIPTIONS"="Dockerfile for the get name api"


# copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# app directory for application containing code files
WORKDIR /usr/src/getname
COPY . .

CMD export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && python3 app.py

