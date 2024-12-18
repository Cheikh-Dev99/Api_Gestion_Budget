# budgetsApp/urls.py
from django.urls import path
from .views.utilisateur_views import InscriptionUtilisateurView
from .views.connexion_views import ConnexionUtilisateurView
from .views.deconnexion_views import DeconnexionUtilisateurView
from .views.reinitialisation_views import DemandeReinitialisationMotDePasseView, ReinitialisationMotDePasseAvecTokenView

urlpatterns = [
    path('inscription/', InscriptionUtilisateurView.as_view(), name='inscription'),
    path('connexion/', ConnexionUtilisateurView.as_view(), name='connexion'),
    path('deconnexion/', DeconnexionUtilisateurView.as_view(), name='deconnexion'),
    path('reinitialisation/demande/', DemandeReinitialisationMotDePasseView.as_view(), name='demande_reinitialisation'),
    path('reinitialisation/<str:token>/', ReinitialisationMotDePasseAvecTokenView.as_view(),name='reinitialisation_avec_token'),
]
