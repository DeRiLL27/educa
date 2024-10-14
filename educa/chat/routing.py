from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(f'ws/chat/room/(?P<course_id>\d+)/$',
            consumers.ChatConsumer.as_asgi()),
]