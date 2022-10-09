FROM python:3.10.7-alpine3.15
WORKDIR /api/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add postgresql-dev gcc python3-dev musl-dev

ADD . . /api/

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /api/entrypoint.sh
RUN chmod +x /api/entrypoint.sh

COPY . .

ENTRYPOINT ["/api/entrypoint.sh"]