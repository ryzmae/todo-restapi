FROM python:3.10.9-slim-buster

WORKDIR /usr/api/api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]