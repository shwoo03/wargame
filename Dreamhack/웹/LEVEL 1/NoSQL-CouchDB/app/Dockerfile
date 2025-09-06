FROM node:lts-alpine as base

ADD ./src /src
WORKDIR /src
EXPOSE 3000

RUN apk add curl

ENV NODE_ENV=production
RUN npm install -g nodemon && npm install
CMD ["node", "bin/www"]