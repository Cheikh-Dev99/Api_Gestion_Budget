# budgetsApp/serializers/connexion_serializer.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.core.exceptions import ObjectDoesNotExist
from ..models.utilisateur_models import Utilisateur


class ConnexionUtilisateurSerializer(serializers.Serializer):
    identifiant = serializers.CharField()  # Email ou téléphone
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        identifiant = data.get("identifiant")
        password = data.get("password")

        # Vérifier si l'identifiant est un email ou un numéro de téléphone
        try:
            if "@" in identifiant:  # C'est probablement un email
                utilisateur = authenticate(
                    email=identifiant, password=password)
            else:  # C'est probablement un numéro de téléphone
                utilisateur = Utilisateur.objects.get(telephone=identifiant)
                if utilisateur and utilisateur.check_password(password):
                    pass
                else:
                    utilisateur = None

        except ObjectDoesNotExist:
            raise AuthenticationFailed(
                "Identifiants invalides, veuillez réessayer.")

        if utilisateur is None:
            raise AuthenticationFailed(
                "Identifiants invalides, veuillez réessayer.")

        if not utilisateur.is_active:
            raise AuthenticationFailed("Ce compte est inactif.")

        data["utilisateur"] = utilisateur
        return data
