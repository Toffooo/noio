# noio
Self hostable app for sending notices via telegram. 

## Installation
```shell
pip install -r requirements/bot_requirements.txt
pip install -r requirements/api_requirements.txt
```

## Setup
* **Run telegram bot**
```shell
python noiobot.py bot
```
* **Run telegram task**
```shell
python noiobot.py tasks
```
* **Run sqlite web interface**
```shell
sqlite_web <sqlite_db_path>
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
```shell
docker-compose up -d --build
```
* **Link for sqlite web interface**
```http
GET http://localhost:8080
```
* **Run Noio REST API**
```http
GET http://localhost:8000
```