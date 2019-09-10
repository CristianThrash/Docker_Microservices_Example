FROM python:3.7.3-alpine3.8
MAINTAINER creator.of.file@example.com
ADD requirements.txt /
RUN pip install -r /requirements.txt
RUN pip install requests
WORKDIR /code