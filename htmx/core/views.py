from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Song, Artist


def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def list_songs(request):
    template_name = 'core/list_songs.html'
    queryset = Song.objects.all().order_by('-pk')
    if order := request.GET.get('order'):
        queryset = queryset.order_by(order)
    if search := request.GET.get('search'):
        queryset = queryset.filter(name__icontains=search)
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('size', 5)
    paginator = Paginator(queryset, page_size)

    if request.GET.get('page'):
        page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_range': paginator.get_elided_page_range(
            page_number
        ),
        'artists': Artist.objects.all().order_by('-pk')[:15]
    }
    if request.headers.get('HX-Request'):
        template_name = 'partials/htmx_components/htmx_table_songs.html'
    return render(request, template_name, context)


def list_artists(request):
    template_name = 'core/list_artists.html'
    context = {
        'artists': Artist.objects.all().order_by('-pk')[:5]
    }
    return render(request, template_name, context)