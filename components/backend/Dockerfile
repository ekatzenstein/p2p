FROM python:3.6-alpine

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apk add --no-cache \
		uwsgi \
        uwsgi-python3

#RUN export PATH=~/.local/bin:$PATH
#ENV PYTHONPATH "/opt/api:$PYTHONPATH"

WORKDIR /opt/api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000 5001 5002
#CMD ["uwsgi", "--ini", "/opt/api/api.ini", "--plugin", "python3"]
CMD ["python", "app.py"]
