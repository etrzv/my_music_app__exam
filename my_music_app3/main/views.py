from django.shortcuts import render, redirect

from my_music_app3.main.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, \
    DeleteProfileForm
from my_music_app3.main.models import Profile, Album


def show_home(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'add-album.html', context)


def details_album(request, pk):
    profile = Profile.objects.first()
    album = Album.objects.get(pk=pk)

    context = {
        'profile': profile,
        'album': album,
    }

    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()
    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    quantity_albums = len(albums)

    context = {
        'profile': profile,
        'albums': albums,
        'quantity_albums': quantity_albums,
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            albums.delete()
            return redirect('show home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'profile-delete.html', context)


