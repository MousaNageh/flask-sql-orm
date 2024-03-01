FROM python:3.11-alpine3.17

WORKDIR /app 

COPY requirements.txt .

RUN apk update

RUN apk add --update --no-cache \
    postgresql-client \
    bash && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    gcc \
    musl-dev \
    python3-dev \
    postgresql \
    postgresql-dev \
    openssl-dev \
    linux-headers && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    apk del .tmp-build-deps

ENV PATH="/py/bin:$PATH"


COPY . . 
