from .viber import ViberType


class User(ViberType):
    id: str
    name: str
    avatar: str
    country: str
    language: str
    primary_device_os: str
    api_version: int
    viber_version: str
    mcc: int
    mnc: int
    device_type: str


class UserOnlineStatus(ViberType):
    id: str
    online_status: int
    online_status_message: str
