from rest_framework import serializers
from ..models.budget import Budget  # Importation correcte du modèle Budget


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ['montant_actuel']  # Empêche la modification directe du montant actuel
 # Empêche la modification directe de current_amount

