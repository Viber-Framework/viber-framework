from enum import StrEnum


class ActionType(StrEnum):
    OPEN_URL = "open-url"
    REPLY = "reply"
    LOCATION_PICKER = "location-picker"
    SHARE_PHONE = "share-phone"
    NONE = "none"
