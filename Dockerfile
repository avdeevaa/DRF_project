FROM python:3

WORKDIR/code

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install bash python3 python3-dev postresql-client && \
    rm -vrf /var/cache/apt/** && \
    curl -sSL https://install.python-poetry.org | python - && \
    poetry config virtualenvs.create false --local

COPY ./poetry.lock /code/

COPY ./pyproject.toml /code/

RUN poetry install

COPY . .

#CMD["python", "manage.py", "runserver"]
