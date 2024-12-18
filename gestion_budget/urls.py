# gestion_budget/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('budgetsApp.urls')),
    path('api/utilisateurs/', include('budgetsApp.urls')),
    # URLs pour l'authentification google
    path('accounts/', include('allauth.urls')),
]
