from django.shortcuts import render

from .models import ChatRoom


def index_view(request):
    return render(request, 'index.html', {
        'rooms': ChatRoom.objects.all(),
    })


def room_view(request, room_name):
    chat_room, created = ChatRoom.objects.get_or_create(name=room_name)
    return render(request, 'chatroom.html', {
        'room': chat_room,
    })
