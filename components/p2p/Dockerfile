FROM python:3.6-alpine as builder

RUN pip install wheel

COPY . .

VOLUME ["/dist"]

CMD ["python", "setup.py", "bdist_wheel"]
