# syntax=docker/dockerfile:1
FROM bitnami/minideb:latest

# "CMD" is like "exec", it's the final command for the container on "run"
CMD ["python3", "--version"]

