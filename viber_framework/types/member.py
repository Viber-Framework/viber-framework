from .viber import ViberType
from ..enums import Role

from pydantic.networks import AnyHttpUrl


class Member(ViberType):
    id: str
    name: str
    avatar: AnyHttpUrl
    role: Role
