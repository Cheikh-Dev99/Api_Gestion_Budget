from rest_framework import serializers
from ..models.transactions import Transaction  # Importation correcte du modèle Transaction

class TransactionSerializer(serializers.ModelSerializer):
        
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Transaction
        fields = '__all__'
