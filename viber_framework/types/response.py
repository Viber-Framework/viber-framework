from pydantic import BaseModel


class Response(BaseModel):
    status: int
    status_message: str
    message_token: int
    chat_hostname: str
    billing_status: int
