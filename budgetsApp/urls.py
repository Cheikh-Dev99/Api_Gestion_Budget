from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.budget_view import BudgetViewSet  
from .views.transaction_view import TransactionViewSet  

# Créer un routeur et enregistrer le viewset
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'budgets', BudgetViewSet, basename='budget')


urlpatterns = [
    path('', include(router.urls)),
]
