from decimal import Decimal
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.transactions import Transaction
from rest_framework.decorators import action  # Importation du décorateur action
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

        # Réajustement du budget lié à la transaction
        budget = transaction.budget
        if transaction.type == 'income':
            budget.current_amount += float(transaction.amount)  # Convertir en float
        else:
            budget.current_amount -= float(transaction.amount)  # Convertir en float
        budget.save()

        return Response({
            'transaction': serializer.data,
            'current_budget': budget.current_amount
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        PUT/PATCH : Mise à jour d'une transaction existante.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        old_amount = instance.amount
        old_type = instance.type

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.save()

        # Convertir old_amount et current_amount en float
        old_amount = float(old_amount)
        budget = transaction.budget
        budget.current_amount = float(budget.current_amount)

        if old_type == 'income':
            budget.current_amount -= old_amount  # Soustraction de l'ancien montant
        else:
            budget.current_amount += old_amount  # Ajout de l'ancien montant

        if transaction.type == 'income':
            budget.current_amount += float(transaction.amount)  # Ajout du nouveau montant
        else:
            budget.current_amount -= float(transaction.amount)  # Soustraction du nouveau montant

        budget.save()

        return Response({
            'transaction': serializer.data,
            'current_budget': budget.current_amount
        })

    def destroy(self, request, *args, **kwargs):
        """
        DELETE : Supprimer une transaction existante.
        """
        instance = self.get_object()

        # Réajustement du budget lors de la suppression
        budget = instance.budget
        if instance.type == 'income':
            budget.current_amount -= float(instance.amount)  # Convertir en float
        else:
            budget.current_amount += float(instance.amount)  # Convertir en float

        budget.save()

        self.perform_destroy(instance)

        return Response({
            'message': 'Transaction supprimée',
            'current_budget': budget.current_amount
        }, status=status.HTTP_200_OK)


    @action(detail=False, methods=['GET'])
    def summary(self, request):
        """
        GET : Résumé des transactions liées au budget.
        """
        transactions = self.get_queryset()
        income_total = sum(t.amount for t in transactions if t.type == 'income')
        expense_total = sum(t.amount for t in transactions if t.type == 'expense')

        return Response({
            'total_income': income_total,
            'total_expense': expense_total,
            'current_budget': transactions.first().budget.current_amount if transactions else 0
        })
