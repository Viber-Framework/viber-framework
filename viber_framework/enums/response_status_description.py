from enum import StrEnum


class ResponseStatusDescription(StrEnum):
    """
    https://developers.viber.com/docs/api/rest-bot-api/#error-codes
    """
    OTHER = -1

    OK = "Success"
    INVALID_URL = "The webhook URL is not valid"
    INVALID_AUTH_TOKEN = "The authentication token is not valid"
