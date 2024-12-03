# Dockerfile to run a Svelte app (in dev mode)

FROM alpine
RUN apk update
RUN apk add nodejs npm

# Copy over the application files necessary to build
WORKDIR /app
COPY package*.json .
COPY *config.js .
COPY src src
COPY static static

# Install dependencies
RUN npm install

# Build the application
RUN npm run build

# Run the application on port 3000
EXPOSE 3000
ENV HOST=0.0.0.0
CMD [ "node", "build" ]

