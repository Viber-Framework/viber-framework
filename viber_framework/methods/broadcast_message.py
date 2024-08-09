from .send_message import SendMessageMethod

from pydantic.fields import Field


class BroadcastMessageMethod(SendMessageMethod):
    """
    https://developers.viber.com/docs/api/rest-bot-api/#get-online
    """

    broadcast_list: list[str] = Field(min_length=1, max_length=300)
