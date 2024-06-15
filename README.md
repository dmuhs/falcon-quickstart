# Falcon Quickstart Template

Quick and dirty Falcon API template. For when things need to get done *fast*. Features:

- Poetry setup
- Docker with Poetry installed
- SQLite backend with SQLAlchemy
- Small static landing page
- Rate limiter
- Size limiter
- Full loguru setup incl. gunicorn log messages

The template's purpose is to enable *fast* development of MVPs, PoCs and hackathon projects. All over

## Quickstart

Install dependencies:

```shell
poetry install
```

Run the service (listen on `127.0.0.1`):

```shell
DEVELOPMENT=true poetry run server
```

Build the image:

```shell
docker build -t falcon_quickstart:latest .
```

Run it:

```shell
docker run -p 8000:8000 falcon_quickstart
```
