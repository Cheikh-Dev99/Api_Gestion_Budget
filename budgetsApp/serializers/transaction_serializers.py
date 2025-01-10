# budgetsApp/serializers/transaction_serializers.py
from rest_framework import serializers
from ..models.transaction_models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['id', 'utilisateur', 'budget', 'type_transaction', 'montant', 'description', 'date_transaction']
        read_only_fields = ('utilisateur', 'budget')

    def validate(self, data):
        montant = data['montant']
        if montant <= 0:
            raise serializers.ValidationError(
                "Le montant de la transaction doit être positif.")

        # Tu peux ajouter une vérification spécifique pour chaque type de transaction ici si nécessaire
        if data['type_transaction'] == 'depense' and montant <= 0:
            raise serializers.ValidationError(
                "Le montant de la dépense doit être positif.")
        elif data['type_transaction'] == 'revenu' and montant <= 0:
            raise serializers.ValidationError(
                "Le montant du revenu doit être positif.")

        return data
