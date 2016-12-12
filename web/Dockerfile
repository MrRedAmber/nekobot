FROM python:2.7.12-onbuild

MAINTAINER kadenlnelson@gmail.com

CMD [ "gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]