"""
ASGI config for hello_world project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path
from app.simple_app.consumers import EchoConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello_world.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    re_path("^ws/echo/$", EchoConsumer.as_asgi()),
                ]
            )
        ),
    }
)
