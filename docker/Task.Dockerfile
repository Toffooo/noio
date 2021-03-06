FROM python:3.8

COPY ./ /app
WORKDIR app

RUN pip install --upgrade pip && pip install --upgrade pip
RUN pip install -r ./requirements/bot_requirements.txt

CMD python noiobot.py tasks
