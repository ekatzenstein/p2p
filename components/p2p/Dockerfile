FROM node:10-alpine as js_builder

WORKDIR /usr/src/app

COPY js/package.json ./
RUN npm install

COPY js/ ./

RUN npm run build


FROM python:3.6-alpine as py_builder

RUN pip install wheel

COPY . .

COPY --from=js_builder /usr/src/app/build/index.js ./pandastoproduction/static/index.js

VOLUME ["/dist"]

CMD ["python", "setup.py", "bdist_wheel"]
