#Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY src/ .

ENTRYPOINT ["python", "cli_tool.py"]
