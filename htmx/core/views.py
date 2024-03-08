from django.shortcuts import render
from .models import Song, Artist


def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def list_songs(request):
    template_name = 'core/list_songs.html'
    context = {
        'songs': Song.objects.all().order_by('-pk')[:5],
        'artists': Artist.objects.all().order_by('-pk')[:15]
    }
    return render(request, template_name, context)


def list_artists(request):
    template_name = 'core/list_artists.html'
    context = {
        'artists': Artist.objects.all().order_by('-pk')[:5]
    }
    return render(request, template_name, context)