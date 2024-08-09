from enum import StrEnum


class ForbiddenFileFormat(StrEnum):
    """
    https://developers.viber.com/docs/api/rest-bot-api/#forbidden-file-formats
    """

    ACTION = "action"
    # Automator action, OS: Mac OS
    APK = "apk"
    # Application, OS: Android
    APP = "app"
    # Executable, OS: Mac OS
    BAT = "bat"
    # Batch file, OS: Windows
    BIN = "bin"
    # Binary executable, OS: Windows, Mac OS, Linux
    CMD = "cmd"
    # Command Script, OS: Windows

    @classmethod
    def is_forbidden(cls, file_format: str) -> bool:
        return file_format in cls._value2member_map_
