FROM python:3.7

WORKDIR /app

COPY . /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP sample

RUN flask run