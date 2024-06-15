from falcon import Request, Response


def silent_handler(_req: Request, resp: Response, _exception: Exception):
    resp.text = ""
