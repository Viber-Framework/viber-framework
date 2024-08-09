from .viber import ViberType
from .button import Button

from pydantic.fields import Field


class Keyboard(ViberType):
    default_height: bool = Field(
        alias='DefaultHeight',
        validation_alias='default_height'
    )
    bg_color: str = Field(
        alias='BgColor',
        validation_alias='bg_color',
        min_length=6,
        max_length=6
    )
    buttons: list[Button] = Field(
        alias='Buttons',
        validation_alias='buttons',
    )

