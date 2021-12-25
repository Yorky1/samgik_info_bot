# syntax=docker/dockerfile:1

FROM python:3.8.10

RUN mkdir app

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "run.py"]
