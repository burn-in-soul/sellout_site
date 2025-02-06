FROM python:3.12.2

WORKDIR /opt/app

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.7.1

ENV PATH="$PATH:$POETRY_HOME/bin"

RUN pip install poetry

COPY . .
RUN poetry install --no-root
