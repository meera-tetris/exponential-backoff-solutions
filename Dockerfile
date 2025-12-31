FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sakshi_backoff.py .

CMD ["python", "sakshi_backoff.py"]
