from enum import IntEnum


class ResponseStatusCode(IntEnum):
    """
    https://developers.viber.com/docs/api/rest-bot-api/#error-codes
    """

    OTHER = -1

    OK = 0
    INVALID_URL = 1
    INVALID_AUTH_TOKEN = 2
