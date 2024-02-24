FROM python:3

WORKDIR/code

COPY ./pyproject.toml /code/

RUN poetry install

RUN poetry shell

COPY . .

#CMD["python", "manage.py", "runserver"]
