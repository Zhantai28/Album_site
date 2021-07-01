from django import forms
from django.urls.base import is_valid_path
from django.views import generic
from django.urls import reverse_lazy
from .models import Album, Song
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "all_albums"

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
    context_object_name = 'album'


class AlbumCreate(generic.CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(generic.UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(generic.DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(generic.View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process from data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normilazed) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
