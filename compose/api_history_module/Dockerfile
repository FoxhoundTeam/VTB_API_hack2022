FROM python:3.9-slim

ENV PYTHONPATH "${PYTHONPATH}:/"

RUN apt update && apt install -y curl

WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./api_history_module/pyproject.toml ./api_history_module/poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY ./api_history_module /app
