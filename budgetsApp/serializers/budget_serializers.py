# budgetsApp/serializers/budget_serializers.py
from rest_framework import serializers
from ..models.budget_models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'utilisateur', 'valeur_initiale',
                  'valeur_actuelle', 'date_ajout']
        read_only_fields = ('utilisateur', 'valeur_actuelle')

    def create(self, validated_data):
        validated_data['valeur_actuelle'] = validated_data['valeur_initiale']
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # On ignore la mise à jour de 'valeur_actuelle' car elle dépend des transactions
        validated_data.pop('valeur_actuelle', None)
        # On peut aussi vérifier si la valeur_initiale a été modifiée et, si oui, mettre à jour valeur_actuelle
        if 'valeur_initiale' in validated_data:
            instance.valeur_actuelle = validated_data['valeur_initiale']
        return super().update(instance, validated_data)

    def validate(self, data):
        if data.get('valeur_initiale') <= 0:
            raise serializers.ValidationError(
                "La valeur initiale du budget doit être positive.")
        return data
