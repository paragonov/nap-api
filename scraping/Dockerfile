FROM python:3.10.7-alpine3.15
WORKDIR /scraping/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . . /scraping/

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

