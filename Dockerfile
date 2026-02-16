FROM python:slim AS builder
WORKDIR /app2
COPY . /app2
RUN chmod +x app.py
CMD ["python", "app.py"]