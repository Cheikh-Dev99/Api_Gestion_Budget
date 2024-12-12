# budgetsApp/views/reinitialisation_views.py
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from ..models.utilisateur_models import Utilisateur
from ..models.reinitialisation_models import TokenReinitialisation
from django.core.mail import send_mail
from ..utils import generer_token


class DemandeReinitialisationMotDePasseView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        email = request.data.get("email")
        if not email:
            return Response({"message": "Veuillez fournir une adresse email"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            utilisateur = Utilisateur.objects.get(email=email)

            # Génération du token
            token = generer_token()
            TokenReinitialisation.objects.create(utilisateur=utilisateur, token=token)

            # Envoi de l'email
            lien = f"http://127.0.0.1:8000/api/utilisateurs/reinitialisation/{token}/"
            send_mail(
                subject="Réinitialisation de votre mot de passe",
                message=f"Bonjour {utilisateur.prenom},\n\nUtilisez ce lien pour réinitialiser votre mot de passe : {lien}\n\nCe lien expire dans une heure.",
                from_email="cheikhahmedtidiane220@gmail.com",
                recipient_list=[email],
            )

            return Response({"message": "Un email de réinitialisation a été envoyé"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message": "Aucun utilisateur trouvé avec cet email"}, status=status.HTTP_404_NOT_FOUND)


class ReinitialisationMotDePasseAvecTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, token, format=None):
        nouveau_mot_de_passe = request.data.get("nouveau_mot_de_passe")
        if not nouveau_mot_de_passe:
            return Response({"message": "Veuillez fournir un nouveau mot de passe"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token_obj = TokenReinitialisation.objects.get(token=token)

            if not token_obj.est_valide():
                return Response({"message": "Le lien de réinitialisation a expiré"}, status=status.HTTP_400_BAD_REQUEST)

            utilisateur = token_obj.utilisateur
            utilisateur.set_password(nouveau_mot_de_passe)
            utilisateur.save()
            token_obj.delete()  # Supprime le token après utilisation

            return Response({"message": "Mot de passe réinitialisé avec succès"}, status=status.HTTP_200_OK)
        except TokenReinitialisation.DoesNotExist:
            return Response({"message": "Token invalide"}, status=status.HTTP_404_NOT_FOUND)
