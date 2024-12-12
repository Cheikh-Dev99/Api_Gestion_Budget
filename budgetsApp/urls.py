# budgetsApp/urls.py
from django.urls import path
from .views.reinitialiser import send_test_email
from .views.utilisateur_views import InscriptionUtilisateurView

urlpatterns = [
    path('send-test-email/', send_test_email, name='send_test_email'),
    path('inscription/', InscriptionUtilisateurView.as_view(), name='inscription'),
]
