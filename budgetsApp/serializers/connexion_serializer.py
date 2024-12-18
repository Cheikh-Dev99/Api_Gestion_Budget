# budgetsApp/serializers/connexion_serializer.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class ConnexionUtilisateurSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        utilisateur = authenticate(email=email, password=password)

        if utilisateur is None:
            raise AuthenticationFailed(
                "Identifiants invalides, veuillez réessayer.")

        if not utilisateur.is_active:
            raise AuthenticationFailed("Ce compte est inactif.")

        data["utilisateur"] = utilisateur
        return data
