# budgetsApp/urls.py
from django.urls import path
from .views.reinitialiser import send_test_email
from .views.utilisateur_views import InscriptionUtilisateurView
from .views.connexion_views import ConnexionUtilisateurView
from .views.deconnexion_views import DeconnexionUtilisateurView

urlpatterns = [
    path('send-test-email/', send_test_email, name='send_test_email'),
    path('inscription/', InscriptionUtilisateurView.as_view(), name='inscription'),
    path('connexion/', ConnexionUtilisateurView.as_view(), name='connexion'),
    path('deconnexion/', DeconnexionUtilisateurView.as_view(), name='deconnexion'),
]
