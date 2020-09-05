from django.shortcuts import render
from . models import Song 

def songs(request):
    song = Song.objects.all()
    return render(request,'songs.html',{'song':song})


def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()

    return render(request,'songpost.html',{'song':song})