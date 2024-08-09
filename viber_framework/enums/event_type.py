from enum import StrEnum


class EventType(StrEnum):
    WEBHOOK = "webhook"
    SUBSCRIBED = "subscribed"
    UNSUBSCRIBED = "unsubscribed"
    CONVERSATION_STARTED = "conversation_started"
    DELIVERED = "delivered"
    FAILED = "failed"
    MESSAGE = "message"
    SEEN = "seen"
