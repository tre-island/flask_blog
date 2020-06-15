FROM python:latest

RUN apt update; mkdir -p /app
COPY . /app
WORKDIR "/app"
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

