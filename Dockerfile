FROM gradle:7.6.0-jdk17-alpine

WORKDIR /usr/src
COPY . .

RUN gradle compileJava --no-daemon 

VOLUME /usr/src

EXPOSE 8090/tcp