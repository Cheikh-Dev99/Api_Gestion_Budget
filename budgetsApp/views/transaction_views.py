from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.transaction_models import Transaction, Budget
from ..serializers.transaction_serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ValidationError


class TransactionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Récupérer toutes les transactions associées à l'utilisateur connecté
        transactions = Transaction.objects.filter(utilisateur=request.user)

        # Sérialiser les données
        serializer = TransactionSerializer(transactions, many=True)

        # Retourner les transactions au format JSON
        return Response(serializer.data)

    def post(self, request):
        try:
            # Vérification de l'existence du budget
            budget = Budget.objects.get(utilisateur=request.user)
        except Budget.DoesNotExist:
            return Response(
                {"detail": "Aucun budget trouvé pour cet utilisateur."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Création de la transaction avec le sérialiseur
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Sauvegarde de la transaction
                transaction = serializer.save(
                    utilisateur=request.user, budget=budget)
                return Response(
                    TransactionSerializer(transaction).data,
                    status=status.HTTP_201_CREATED
                )
            except ValidationError as e:
                # Gérer l'erreur de validation et renvoyer un statut 400
                return Response(
                    {"detail": str(e.message)},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Si le sérialiseur n'est pas valide, on renvoie les erreurs
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
