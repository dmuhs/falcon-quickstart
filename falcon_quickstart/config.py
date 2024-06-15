from os import environ

from falcon_quickstart.logger.gunicorn import StubbedGunicornLogger

options = {
    "bind": "127.0.0.1:8000" if environ.get("DEVELOPMENT") else "0.0.0.0:8000",
    "workers": 2,
    "threads": 2,
    "accesslog": "-",
    "errorlog": "-",
    "worker_connections": 1000,
    "reload": True,
    "logger_class": StubbedGunicornLogger,
}
