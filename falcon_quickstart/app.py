from pathlib import Path

import falcon

from falcon_quickstart.config import options
from falcon_quickstart.logger import setup_logging
from falcon_quickstart.middlewares import DBSessionMiddleware
from falcon_quickstart.models import Session
from falcon_quickstart.resources import IndexResource, rate
from falcon_quickstart.utils.error_handler import silent_handler
from falcon_quickstart.utils.gunicorn import StandaloneApplication


def main():
    setup_logging()

    res_index = IndexResource()

    application = falcon.App(
        middleware=[
            DBSessionMiddleware(Session),
            rate.middleware,
            falcon.CORSMiddleware(allow_origins="*"),
        ]
    )

    application.add_static_route(
        prefix="/",
        directory=Path(__file__).parent / "static",
        fallback_filename="index.html",
    )
    application.add_route("/index.html", res_index)
    application.set_error_serializer(silent_handler)
    StandaloneApplication(application, options).run()


if __name__ == "__main__":
    main()
