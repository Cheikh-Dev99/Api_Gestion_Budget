# budgetsApp/views/reinitialisation_views.py
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from ..models.utilisateur_models import Utilisateur


class DemandeReinitialisationMotDePasseView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        email = request.data.get("email")
        if not email:
            return Response({"message": "Veuillez fournir une adresse email"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            utilisateur = Utilisateur.objects.get(email=email)
            return Response({"message": "Demande de réinitialisation enregistrée"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message": "Aucun utilisateur trouvé avec cet email"}, status=status.HTTP_404_NOT_FOUND)


class ReinitialisationMotDePasseView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        email = request.data.get("email")
        nouveau_mot_de_passe = request.data.get("nouveau_mot_de_passe")

        if not email or not nouveau_mot_de_passe:
            return Response({"message": "Veuillez fournir l'email et le nouveau mot de passe"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            utilisateur = Utilisateur.objects.get(email=email)
            utilisateur.set_password(nouveau_mot_de_passe)
            utilisateur.save()
            return Response({"message": "Mot de passe réinitialisé avec succès"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message": "Aucun utilisateur trouvé avec cet email"}, status=status.HTTP_404_NOT_FOUND)
