FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update -y && apt-get upgrade -y python-pip
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
