from .method import Method

from ..enums import EventType

from pydantic.networks import AnyHttpUrl


class SetWebHookMethod(Method):
    """
    https://developers.viber.com/docs/api/rest-bot-api/#setting-a-webhook
    """

    url: AnyHttpUrl
    event_types: list[EventType] | None = None
    send_name: bool
    send_photo: bool
