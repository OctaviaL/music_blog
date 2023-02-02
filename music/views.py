from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models import Music
from music.serializers import MusicSerializer

@api_view(['GET'])
def get_hello(request):
    return Response('Hello world')

@api_view(['GET'])
def get_music(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_song(request, id):
    try:
        song = Music.objects.get(id=id)
    except Music.DoesNotExist:
        return Response('Нет такой песни!')
    serializer = MusicSerializer(song, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def set_music(request):
    print(request.data)
    serializer = MusicSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save
    return Response(serializer.data)

# DELETE, PUT, PATCH