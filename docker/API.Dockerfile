FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./ /app

EXPOSE 8000

RUN pip install --upgrade pip && pip install --upgrade pip
RUN pip install -r ./requirements/api_requirements.txt

CMD uvicorn noioapi:api --host 0.0.0.0 --port 8000
