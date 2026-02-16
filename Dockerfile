FROM python:slim AS builder
WORKDIR /DProject2
COPY . /DProject2
COPY . .
ENTRYPOINT ["python", "lab.py"]