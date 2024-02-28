FROM python:3.10-buster 
EXPOSE 500 

WORKDIR /app 

COPY requirements.txt .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --upgrade pip

RUN pip install -r  requirements.txt

COPY . . 

CMD [ "flask", "run", "--host", "0.0.0.0"]
