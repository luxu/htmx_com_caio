from django.urls import path

from . import views, views_htmx

urlpatterns = [
    path('', views.index, name='index'),
    path('list_songs/', views.list_songs, name='list_songs'),
    path('list_artists/', views.list_artists, name='list_artists'),
]

htmx_urlpatterns = [
    # SONG
    path('check_song/', views_htmx.check_song, name='check_song'),
    path('save_song/', views_htmx.save_song, name='save_song'),
    path('delete_song/<int:id>', views_htmx.delete_song, name='delete_song'),
    # ARTIST
    path('check_artist/', views_htmx.check_artist, name='check_artist'),
    path('save_artist/', views_htmx.save_artist, name='save_artist'),
    path('delete_artist/<int:id>', views_htmx.delete_artist, name='delete_artist'),
]

urlpatterns += htmx_urlpatterns
