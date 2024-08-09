from enum import StrEnum


class MessageType(StrEnum):
    TEXT = "text"
    PICTURE = "picture"
    VIDEO = "video"
    FILE = "file"
    CONTACT = "contact"
    LOCATION = "location"
    URL = "url"
    STICKER = "sticker"
    CAROUSEL_CONTENT = "rich_media"
