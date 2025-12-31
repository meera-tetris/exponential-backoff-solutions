# 1. Use Python base image
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy project files into container
COPY . .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Run the program
CMD ["python", "main.py"]
