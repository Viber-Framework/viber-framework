from .http_server import HttpServer

from .enums import EventType


class Bot(HttpServer):

    async def on_ready(self, *args, **kwargs) -> None:
        pass

    async def on_quit(self, *args, **kwargs) -> None:
        pass

    async def _set_webhook(
            self,
            webhook_url: str,
            event_types: list[EventType] | None = None,
            send_name: bool = True,
            send_photo: bool = False
    ):
        pass

    async def _remove_webhook(self):
        pass

    async def run_bot(self):
        self.run()
