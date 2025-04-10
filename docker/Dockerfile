FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH ${PYTHONPATH}/code:/code/app

ARG ENV_FILE
COPY ${ENV_FILE} .env

# Instalar Node.js LTS y npm
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD [ "uvicor", "app.main.app", "host", "0.0.0.0", "--port", "8000"]