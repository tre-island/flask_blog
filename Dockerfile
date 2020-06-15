FROM python:latest

RUN apt update; mkdir -p /app
COPY . /app
WORKDIR "/app"
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

