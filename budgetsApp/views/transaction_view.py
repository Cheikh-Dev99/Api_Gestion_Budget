from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models.transactions import Transaction
from ..models.budget import Budget
from ..serializers.transaction_serializer import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.all()

    def create(self, request):
        """
        POST : Créer une nouvelle transaction.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.save()

        budget = transaction.budget
        if transaction.type == 'revenu':
            budget.montant_actuel += transaction.montant
        else:
            budget.montant_actuel -= transaction.montant
        budget.save()

        return Response({
            'transaction': serializer.data,
            'montant_actuel': budget.montant_actuel
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        PUT/PATCH : Modifier une transaction existante.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        ancien_montant = instance.montant
        ancien_type = instance.type

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.save()

        budget = transaction.budget
        if ancien_type == 'revenu':
            budget.montant_actuel -= ancien_montant
        else:
            budget.montant_actuel += ancien_montant

        if transaction.type == 'revenu':
            budget.montant_actuel += transaction.montant
        else:
            budget.montant_actuel -= transaction.montant

        budget.save()

        return Response({
            'transaction': serializer.data,
            'montant_actuel': budget.montant_actuel
        })

    def destroy(self, request, *args, **kwargs):
        """
        DELETE : Supprimer une transaction existante.
        """
        instance = self.get_object()
        budget = instance.budget
        if instance.type == 'revenu':
            budget.montant_actuel -= instance.montant
        else:
            budget.montant_actuel += instance.montant

        budget.save()
        self.perform_destroy(instance)

        return Response({
            'message': 'Transaction supprimée',
            'montant_actuel': budget.montant_actuel
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def summary(self, request):
        """
        GET : Résumé des transactions liées au budget.
        """
        transactions = self.get_queryset()
        total_revenu = sum(t.montant for t in transactions if t.type == 'revenu')
        total_depense = sum(t.montant for t in transactions if t.type == 'depense')

        return Response({
            'revenu_total': total_revenu,
            'depense_totale': total_depense,
            'montant_actuel': transactions.first().budget.montant_actuel if transactions else 0
        })
