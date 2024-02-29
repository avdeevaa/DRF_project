FROM python:3

WORKDIR/code

COPY ./pyproject.toml /code/

RUN poetry install && poetry shell

COPY . .

#CMD["python", "manage.py", "runserver"]
