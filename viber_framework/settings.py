from pydantic_settings.main import (
    BaseSettings,
    SettingsConfigDict
)

from pydantic.main import BaseModel


class ViberBotSettings(BaseModel):
    API_TOKEN: str
    BASE_URL: str
    WEBHOOK_PATH: str

    @property
    def webhook_url(self) -> str:
        return f"{self.BASE_URL}{self.WEBHOOK_PATH}"


class HttpServerSettings(BaseSettings):
    HOSTNAME: str
    PORT: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='__',
        case_sensitive=True,
        extra='ignore'
    )

    HTTP_SERVER: HttpServerSettings
    VIBER_BOT: ViberBotSettings


settings = Settings()
