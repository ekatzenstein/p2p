FROM python:3.6-alpine

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apk add --update \
    build-base \
    postgresql-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV SQLLITE_DIR=/sqllite-db/

EXPOSE 5000
CMD ["python", "-B", "src/app.py"]
