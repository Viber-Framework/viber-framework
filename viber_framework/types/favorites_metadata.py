from .viber import ViberType

from typing import Literal

from pydantic.networks import AnyHttpUrl


class FavoritesMetadata(ViberType):
    type: Literal['gif'] | Literal['link'] | Literal['video']
    url: AnyHttpUrl
    title: str | None = None
    thumbnail: AnyHttpUrl | None = None
    domain: str | None = None
    width: int | None = None
    height: int | None = None
    alternative_url: AnyHttpUrl | None = None
    alternative_text: str | None = None


