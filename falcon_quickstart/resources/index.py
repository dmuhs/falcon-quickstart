from pathlib import Path

import falcon
from falcon import Request, Response


class IndexResource:
    # noinspection PyMethodMayBeStatic
    def on_get(self, _req: Request, resp: Response):
        p = Path(__file__).parent.parent / "static/index.html"
        resp.stream = p.open("rb")
        resp.content_type = "text/html"
        resp.status = falcon.HTTP_200
