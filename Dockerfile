FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /food
COPY requirements.txt /food/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /food
