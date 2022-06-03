FROM python:3.9.13

RUN apt-get update && apt-get install -y gdal-bin

RUN mkdir /api
WORKDIR /api

COPY ./requirements.txt .

RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1

COPY . .

ENTRYPOINT ["sh", "-c", "./init.sh"]