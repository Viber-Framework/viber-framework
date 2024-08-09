from aiohttp.web import (
    Application,
    Request,
    Response,
    run_app,
    post
)

from .settings import settings


class HttpServer(Application):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_routes([
            post(settings.VIBER_BOT.webhook_url, self.handle_request)
        ])

    async def handle_request(self, request: Request, *args, **kwargs) -> Response:
        print(request)

    def run(self):
        run_app(
            self,
            host=settings.HTTP_SERVER.HOSTNAME,
            port=settings.HTTP_SERVER.PORT,
        )
