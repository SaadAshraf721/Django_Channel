from django.urls import path
from .consumers import MySync

websockets_urlpattrens = [
    path('ws/sc/', MySync.as_asgi())
]