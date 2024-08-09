from .method import Method

from pydantic.fields import Field

from ..enums import MessageType


class SendMessageMethod(Method):
    """
    https://developers.viber.com/docs/api/rest-bot-api/#send-message
    """

    receiver: int
    # subscribed valid user id
    type: MessageType
    tracking_data: str = Field(max_length=4096)
    # Allow the account to track messages and user’s replies.
    # Sent tracking_data value will be passed back with user’s reply
    min_api_version: int = Field(gt=0, default=1)
