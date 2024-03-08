from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from htmx.core.models import Song, Artist


def check_song(request):
    template_name = 'partials/htmx_components/check_song.html'
    name = request.GET.get('nome')
    song = Song.objects.filter(name=name)
    context = {
        'song': song
    }
    return render(request, template_name, context)

def save_song(request):
    template_name = 'partials/htmx_components/list_all_songs.html'
    name = request.POST.get('nome')
    year = request.POST.get('ano')
    artist = request.POST.get('cantor')
    song = Song.objects.create(
        name=name,
        release_year=year,
        artist_id=artist
    )
    song.save()
    artists = Artist.objects.all().order_by('-pk')[:10]
    songs = Song.objects.all().order_by('-pk')[:5]
    context = {
        'songs': songs,
        'artists': artists
    }
    return render(request, template_name, context)


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_song(request, id):
    template_name = 'partials/htmx_components/list_all_songs.html'
    song = Song.objects.get(id=id)
    song.delete()
    songs = Song.objects.all().order_by('-pk')[:5]
    artists = Artist.objects.all().order_by('-pk')[:10]
    context = {
        'songs': songs,
        'artists': artists
    }
    return render(request, template_name, context)

def check_artist(request):
    template_name = 'partials/htmx_components/check_artist.html'
    name = request.GET.get('nome')
    artist = Artist.objects.filter(name=name)
    context = {
        'artist': artist
    }
    return render(request, template_name, context)


def save_artist(request):
    template_name = 'partials/htmx_components/list_all_artists.html'
    name = request.POST.get('nome')
    artist = Artist.objects.create(name=name)
    artist.save()
    artists = Artist.objects.all().order_by('-pk')[:5]
    context = {
        'artists': artists
    }
    return render(request, template_name, context)

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_artist(request, id):
    template_name = 'partials/htmx_components/list_all_artists.html'
    artist = Artist.objects.get(id=id)
    artist.delete()
    artists = Artist.objects.all().order_by('-pk')[:5]
    context = {
        'artists': artists
    }
    return render(request, template_name, context)
