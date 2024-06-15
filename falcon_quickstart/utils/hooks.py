import falcon


def limit_size(limit):
    def hook(req, _resp, _resource, _params):
        length = req.content_length
        if length is not None and length > limit:
            msg = (
                "The size of the request is too large. The body must not "
                f"exceed {limit} bytes in length."
            )
            raise falcon.HTTPPayloadTooLarge(
                title="Request body is too large", description=msg
            )

    return hook
