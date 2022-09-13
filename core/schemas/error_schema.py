from pydantic import BaseModel


class Response(BaseModel):
    error: int
    success: bool
    message: str


# TODO
class Response400(Response):
    pass


class Response404(Response):
    error = 404
    success = False
