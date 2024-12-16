from rest_framework import serializers
from ..models.budget import Budget  # Importation correcte du modèle Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ['current_amount']  # Empêche la modification directe de current_amount

