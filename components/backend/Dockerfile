FROM python:3.6-alpine

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
