# noio
Self hostable app for sending notices via telegram. 

## Installation
```shell
pip install -r requirements/bot_requirements.txt
pip install -r requirements/api_requirements.txt
```

## Setup
* **Setup .env file**
```shell
cp ./.env.example ./.env
```
* **Run telegram bot**
```shell
python noiobot.py bot
```
* **Run telegram tasks handler**
```shell
python noiobot.py tasks
```
```http
GET http://localhost:8080
```
* **Run Noio REST API**
```shell
uvicorn noioapi:api --reload
```
```http
GET http://localhost:8000/docs
```

## Setup into docker
* **Setup .env file**
```shell
cp ./.env.example ./.env
```
Run docker containers
```shell
docker-compose up -d --build
```
* **Run Noio REST API**
```http
GET http://localhost:8000
```