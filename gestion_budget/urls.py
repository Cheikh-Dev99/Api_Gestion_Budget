# gestion_budget/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('budgetsApp.urls')),
    # path('api/utilisateurs/', include('budgetsApp.urls')),
    # URLs pour l'authentification google
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
