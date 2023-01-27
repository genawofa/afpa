from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('joueur/<int:equipe_id>/', views.liste_joueurs, name='liste_joueur'),
    path('equipe', views.liste_equipe, name='liste_equipe'),
    path('point', views.point, name='cumul_points'),
]