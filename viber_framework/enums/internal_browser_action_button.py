from enum import StrEnum


class InternalBrowserActionButton(StrEnum):
    FORWARD = "forward"
    SEND = "send"
    OPEN_EXTERNALLY = "open-externally"
    SEND_TO_BOT = "send-to-bot"
    NONE = "none"
