from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="chat_index"),
    path("<str:room_name>/", views.room, name="room")
]