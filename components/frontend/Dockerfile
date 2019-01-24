FROM node:10-alpine as base
WORKDIR /usr/src/app

COPY package.json ./
RUN npm install

COPY . ./

EXPOSE 3000

CMD ["npm", "start"]
