from django.shortcuts import render, redirect, reverse
from .models import Genre, Artist, Album, Song
from .forms import GenreForm, ArtistForm, AlbumForm, SongForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect


def homeview(request):
    return render(request, 'musicApp/homepage.html')


def genreview(request):
    genre = Genre.objects.all()
    return render(request, 'musicApp/genrepage.html', {'genre': genre})


@login_required
def creategenreview(request):
    form = GenreForm()
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(genreview)
    return render(request, 'musicApp/creategenre.html', {'form': form})


# def logInView(request):
#     next = request.GET.get('next')
#     form = LogIn(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect(genreview)
#     context = {'form': form}
#     return render(request, "musicApp/logIn.html", context)


class ArtistView(DetailView):
    model = Genre
    template_name = 'musicApp/artistpage.html'


@login_required
def createartistview(request):
    form = ArtistForm()
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(genreview)
    return render(request, 'musicApp/createartist.html', {'form': form})


class AlbumView(DetailView):
    model = Artist
    template_name = 'musicApp/albumpage.html'


@login_required
def createalbumview(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(genreview)
    return render(request, 'musicApp/createalbum.html', {'form': form})


class UpdateAlbum(UpdateView):
    model = Album
    fields = '__all__'


class SongView(DetailView):
    model = Album
    template_name = 'musicApp/songpage.html'


@login_required
def createsongview(request):
    form = SongForm()
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(genreview)
    return render(request, 'musicApp/createsong.html', {'form': form})


def loginview(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('success'))
        else:
            context["error"] = "Provide valid credentials !"
            return render(request, 'musicApp/login.html', context)
    else:
        return render(request, 'musicApp/login.html', context)


def successview(request):
    context = {}
    context['user'] = request.user
    return render(request, 'musicApp/success.html', context)


def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class UpdateGenre(UpdateView):
    model = Genre
    fields = '__all__'
    template_name = 'musicApp/genre_form.html'


class DeleteGenre(DeleteView):
    model = Genre
    success_url = reverse_lazy('genre')


class UpdateArtist(UpdateView):
    model = Artist
    fields = '__all__'


class DeleteArtist(DeleteView):
    model = Artist
    success_url = reverse_lazy('genre')


class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('genre')


class UpdateSong(UpdateView):
    model = Song
    fields = '__all__'


class DeleteSong(DeleteView):
    model = Song
    success_url = reverse_lazy('genre')