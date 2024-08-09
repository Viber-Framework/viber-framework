from .viber import ViberType

from pydantic.fields import Field
from pydantic.networks import AnyHttpUrl


class Sender(ViberType):
    name: str = Field(min_length=1, max_length=28)
    avatar: AnyHttpUrl | None = None
    # Avatar size should be no more than 100 kb. Recommended 720x720
