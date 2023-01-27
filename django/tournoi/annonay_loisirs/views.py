from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipe,Match,Participant
# Create your views here.

def index(request):
    return HttpResponse("Bienvenus sur le site d'Annonay Loisirs !")

def liste_joueurs(request, equipe_id):
    liste_joueurs = Equipe.objects.get(id=equipe_id)
    context = {
        'liste_joueurs':liste_joueurs
    }
    return render(request,'annonay_loisirs/liste_joueurs.html',context)

def liste_equipe(request):
    liste_equipe = Equipe.objects.all()
    context = {
        'liste_equipe':liste_equipe
    }
    return render(request,'annonay_loisirs/liste_equipe.html',context)

def point(request):
    
    nombre_point=Match.objects.all()
    context = {
        'nombre_point':nombre_point
    }
    return render(request,'annonay_loisirs/cumul_points.html',context)