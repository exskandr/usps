# syntax=docker/dockerfile:1
FROM python:alpine
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]