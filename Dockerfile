FROM python:3.10

RUN apt update

RUN mkdir "backend"

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY backend/poetry.lock ./
COPY backend/pyproject.toml ./

RUN python -m pip install --upgrade pip && \
    pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root

COPY backend/src ./src
COPY ./commands ./commands

RUN chmod +x commands/*.sh

CMD ["bash", "commands/start_server.sh"]