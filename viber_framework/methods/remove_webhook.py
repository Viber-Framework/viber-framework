from .method import Method

from pydantic.types import constr


class RemoveWebHookMethod(Method):
    """
    https://developers.viber.com/docs/api/rest-bot-api/#setting-a-webhook
    """

    url: constr = ""
