# syntax=docker/dockerfile:1
FROM bitnami/minideb:latest

RUN apt-get update
RUN apt-get -y install python3

# "CMD" is like "exec", it's the final command for the container on "run"
CMD ["python3", "--version"]

