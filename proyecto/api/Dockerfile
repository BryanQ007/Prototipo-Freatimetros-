FROM python:3.11.3-slim-buster

WORKDIR /api

COPY ../api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "server.py"]

