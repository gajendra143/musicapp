from django import forms
from .models import Genre, Artist, Album, Song
from django.contrib.auth import authenticate


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['artist_genre']


class LogIn(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if 'username' and 'password':
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User doesn't exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("User inactive")
        return super(LogIn, self).clean(*args, **kwargs)


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
