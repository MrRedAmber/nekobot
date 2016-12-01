FROM python:latest

MAINTAINER kadenlnelson@gmail.com


RUN pip install -U pip wheel setuptools

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY . /opt/nekobot

WORKDIR /opt/nekobot

CMD ["python", "./app.py"]