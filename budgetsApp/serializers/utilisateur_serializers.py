# budgetsApp/serializers/utilisateur_serializers.py
from rest_framework import serializers
from ..models.utilisateur_models import Utilisateur


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['prenom', 'nom', 'telephone', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        utilisateur = Utilisateur.objects.create_user(
            prenom=validated_data['prenom'],
            nom=validated_data['nom'],
            telephone=validated_data['telephone'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return utilisateur
