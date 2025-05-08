FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "main.py"]
