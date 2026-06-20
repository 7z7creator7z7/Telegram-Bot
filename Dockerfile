FROM python:3.9-slim
RUN apt-get update && apt-get install -y gcc python3-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --only-binary=:all: -r requirements.txt
COPY . .
CMD ["python", "telegram.py"]
