from django.conf import settings
from urllib.parse import parse_qs
from asgiref.sync import sync_to_async
from django.db import close_old_connections

from jwt import decode as jwt_decode
from channels.security.websocket import WebsocketDenier
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from core.models import User


class TokenAuthMiddleware:
    """
    Custom token auth middleware
    """

    def __init__(self, application):
        self.application = application

    async def __call__(self, scope, receive, send):
        close_old_connections()

        denier = WebsocketDenier()
        try:
            token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]
        except KeyError:
            return await denier(scope, receive, send)

        try:
            # This will automatically validate the token and raise an error if token is invalid
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            print(e)
            return await denier(scope, receive, send)
        else:
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])

            try:
                user = await sync_to_async(User.objects.get)(id=decoded_data["user_id"])
            except User.DoesNotExist:
                return await denier(scope, receive, send)

        scope["user"] = user
        return await self.application(scope, receive, send)