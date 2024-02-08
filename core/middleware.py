from django.conf import settings
from asgiref.sync import sync_to_async

from jwt import InvalidTokenError, decode as jwt_decode
from channels.security.websocket import WebsocketDenier

from core.models import User

from channels.middleware import BaseMiddleware


class JWTWSMiddleware(BaseMiddleware):
    """
    Уф, здесь работа над Websocket'ами, отрабатывается до начала
    их соединения, производится проверка на аутентифицированною

    Выступает жесткой оберткой в роутинге протоколов, для WS
    """

    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])
        denier = WebsocketDenier()

        if b"authorization" in headers:
            try:
                token = headers[b"authorization"].decode("utf-8")
                decoded_data = jwt_decode(token, settings.SECRET_KEY)

                scope['user'] = await sync_to_async(User.objects.get)(
                    id=decoded_data['user_id'],
                )
                return await super().__call__(scope, receive, send)
            except (User.DoesNotExist, InvalidTokenError):
                pass
        return await denier(scope, receive, send)
