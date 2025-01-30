

class NotFoundError(Exception):
    message: str = "Internal error"

    def __init__(self, message: str | None = None) -> None:

        if message:
            self.message = message
