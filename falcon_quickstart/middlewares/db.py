from falcon import Request, Response

from falcon_quickstart.models import Session


class DBSessionMiddleware:
    def __init__(self, s: Session):
        self.session_cls = s

    def process_request(self, req: Request, _resp: Response):
        # Not using process_resource here because sink handler needs session, too
        req.context.session = self.session_cls()

    def process_response(
        self, req: Request, _resp: Response, _resource: object, _req_succeeded
    ):
        if hasattr(req.context, "session"):
            req.context.session.close()
