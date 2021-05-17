from django.shortcuts import render, get_list_or_404
from .models import Album, Track
from .forms import RechercheForm


# Create your views here.
def accueil(request):
    """ Afficher tous les articles de notre blog """
    form = RechercheForm(request.POST or None)

    if form.is_valid():
        recherche = form.cleaned_data["recherche"]
        albums = Album.objects.filter(title__contains=recherche)
    else:
        albums = get_list_or_404(Album) # Nous sélectionnons toutes les instances de la classe Album

    return render(request, 'disks/accueil.html', {'albums': albums})


def lire_album(request, album_id):
    """ Afficher le contenu d'un album """
    album_id=album_id
    mon_album = Album.objects.get(id=album_id)
    tracks = Track.objects.filter(album_id=album_id)
    return render(request, 'disks/lire_album.html', locals())
