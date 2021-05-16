from django.shortcuts import render
from .models import Album


# Create your views here.
def accueil(request):
    """ Afficher tous les articles de notre blog """
    albums = Album.objects.all()  # Nous sélectionnons toutes les instances de la classe Album
    return render(request, 'disks/accueil.html', {'albums': albums})