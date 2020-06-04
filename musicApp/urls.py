from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mPandora/', views.homeview, name='home'),
    url(r'^genre$', views.genreview, name='genre'),
    url(r'^creategenre$', views.creategenreview, name='creategenre'),
    # url(r'^accounts/login/$', views.logInView, name='login'),
    url(r'^(?P<pk>[0-9]+)$', views.ArtistView.as_view(), name='artist'),
    url(r'^createartist$', views.createartistview, name='createartist'),
    url(r'^artist/(?P<pk>[0-9]+)$', views.AlbumView.as_view(), name='album'),
    url(r'^createalbum$', views.createalbumview, name='createalbum'),
    url(r'^album/(?P<pk>[0-9]+)$', views.SongView.as_view(), name='song'),
    url(r'^createsong$', views.createsongview, name='createsong'),
    url(r'^accounts/login/$', views.loginview, name='login'),
    url(r'^success$', views.successview, name='success'),
    url(r'^logout/', views.logoutview, name='logout'),
    url(r'^genre/(?P<pk>[0-9]+)$', views.UpdateGenre.as_view(), name='update_genre'),
    url(r'^genre/(?P<pk>[0-9]+)/delete$', views.DeleteGenre.as_view(), name='delete_genre'),
    url(r'^update/(?P<pk>[0-9]+)$', views.UpdateArtist.as_view(), name='update_artist'),
    url(r'^artist/(?P<pk>[0-9]+)/delete$', views.DeleteArtist.as_view(), name='delete_artist'),
    url(r'^update_album/(?P<pk>[0-9]+)$', views.UpdateAlbum.as_view(), name='update_album'),
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.DeleteAlbum.as_view(), name='delete_album'),
    url(r'^update_song/(?P<pk>[0-9]+)$', views.UpdateSong.as_view(), name='update_song'),
    url(r'^song/(?P<pk>[0-9]+)/delete$', views.DeleteSong.as_view(), name='delete_song'),
]
