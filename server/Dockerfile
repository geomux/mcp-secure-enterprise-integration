# Dockerfile creating the image for the MCP server

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9000

CMD ["python", "server.py"]

