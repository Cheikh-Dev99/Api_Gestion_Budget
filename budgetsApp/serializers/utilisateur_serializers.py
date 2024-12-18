# budgetsApp/serializers/utilisateur_serializers.py
from rest_framework import serializers
from ..models.utilisateur_models import Utilisateur
from django.contrib.auth import get_user_model

Utilisateur = get_user_model()

class InscriptionUtilisateurSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = Utilisateur
        fields = ['prenom', 'nom', 'telephone', 'email', 'password']

    def create(self, validated_data):
        utilisateur = Utilisateur.objects.creer_utilisateur(
            prenom=validated_data['prenom'],
            nom=validated_data['nom'],
            telephone=validated_data['telephone'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return utilisateur
