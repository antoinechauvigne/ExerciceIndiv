from django.shortcuts import render
from .models import Album, Track


# Create your views here.
def accueil(request):
    """ Afficher tous les articles de notre blog """
    albums = Album.objects.all()  # Nous sélectionnons toutes les instances de la classe Album
    return render(request, 'disks/accueil.html', {'albums': albums})


def lire_album(request, album_id):
    """ Afficher le contenu d'un album """
    album_id=album_id
    mon_album = Album.objects.get(id=album_id)
    tracks = Track.objects.filter(album_id=album_id)
    return render(request, 'disks/lire_album.html', locals())
