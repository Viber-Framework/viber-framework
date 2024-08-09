from .enums import (
    ResponseStatusCode,
    ResponseStatusDescription
)


class ViberAPIException(Exception):
    error_code: ResponseStatusCode
    error_description: ResponseStatusDescription

    def __init__(
            self,
            error_code: ResponseStatusCode,
            error_description: ResponseStatusDescription
    ) -> None:
        self.error_code = error_code
        self.error_description = error_description

    def __str__(self) -> str:
        return f"{self.__class__} ({self.error_code}): {self.error_description}"
