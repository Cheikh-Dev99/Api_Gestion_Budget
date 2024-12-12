# budgetsApp/views/deconnexion_views.py
from knox.views import LogoutView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class DeconnexionUtilisateurView(LogoutView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        super().post(request, format=None)
        return Response({"message": "Déconnexion réussie"}, status=status.HTTP_200_OK)
