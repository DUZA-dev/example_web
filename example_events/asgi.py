"""
ASGI config for example_events project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

import chat.routing as chat

from core.middleware import JWTWSMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example_events.settings')

http = get_asgi_application()

application = ProtocolTypeRouter({
    "http": http,
    "websocket": JWTWSMiddleware(URLRouter(chat.websocket_urlpatterns)),
})
