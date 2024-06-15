FROM python:3.11-slim

ENV POETRY_VERSION=1.7.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN python3 -m venv $POETRY_VENV
RUN $POETRY_VENV/bin/pip install -U pip setuptools
RUN $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install --only main

COPY . /app
VOLUME /app/storage

RUN groupadd -r user && useradd -r -g user user
RUN chown -R user:user /app
USER user

CMD [ "poetry", "run", "python", "-m", "falcon_quickstart.app"]
