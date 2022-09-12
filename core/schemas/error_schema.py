from pydantic import BaseModel


class Response(BaseModel):
    error: int
    success: bool
    message: str


class Response404(Response):
    error = 404
    success = False
