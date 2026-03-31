FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

ENV DEBUG=False
ENV HOST_IP=0.0.0.0

EXPOSE 5000

CMD ["python", "app.py"]