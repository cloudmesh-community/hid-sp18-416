FROM node:9.11 

COPY . file-server/

WORKDIR file-server/

RUN npm install

EXPOSE 3333

CMD ["node", "index.js"]