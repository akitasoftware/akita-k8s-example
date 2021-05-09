FROM python:3.9.4-slim-buster

RUN groupadd --gid 1000 app \
    && useradd --uid 1000 --gid app --shell /bin/bash --create-home app
WORKDIR /home/app
COPY requirements.txt requirements.txt
COPY src/todo-service.py todo-service.py
RUN pip install -r requirements.txt

ENV FLASK_APP=todo-service.py
EXPOSE 5000
USER app
CMD flask run --host=0.0.0.0