from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.budget_view import BudgetViewSet  
from .views.transaction_view import TransactionViewSet  
from .views.utilisateur_views import InscriptionUtilisateurView
from .views.connexion_views import ConnexionUtilisateurView
from .views.deconnexion_views import DeconnexionUtilisateurView
from .views.reinitialisation_views import DemandeReinitialisationMotDePasseView, ReinitialisationMotDePasseAvecTokenView


# Créer un routeur et enregistrer le viewset
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'budgets', BudgetViewSet, basename='budget')


urlpatterns = [
    path('', include(router.urls)),
    path('inscription/', InscriptionUtilisateurView.as_view(), name='inscription'),
    path('connexion/', ConnexionUtilisateurView.as_view(), name='connexion'),
    path('deconnexion/', DeconnexionUtilisateurView.as_view(), name='deconnexion'),
    path('reinitialisation/demande/', DemandeReinitialisationMotDePasseView.as_view(), name='demande_reinitialisation'),
    path('reinitialisation/<str:token>/', ReinitialisationMotDePasseAvecTokenView.as_view(),name='reinitialisation_avec_token'),
]

