FROM node:16.16-alpine
WORKDIR /app
RUN chown -R node:node /app
COPY --chown=node:node ./grpc-server-node /app/src
COPY --chown=node:node ./pb /app/pb
USER node
ENTRYPOINT ["npm", "start"]
