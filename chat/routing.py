from django.urls import path, re_path
from .consumers import *

websocket_urlpatterns = [
    path('ws/notification/<str:room_name>/', ChatConsumer.as_asgi()),

]