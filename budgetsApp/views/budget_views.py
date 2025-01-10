# budgetsApp/views/budget_views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.budget_models import Budget
from ..serializers.budget_serializers import BudgetSerializer
from rest_framework.permissions import IsAuthenticated


class BudgetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            budget = Budget.objects.get(utilisateur=request.user)
            serializer = BudgetSerializer(budget)
            return Response(serializer.data)
        except Budget.DoesNotExist:
            return Response({"detail": "Aucun budget trouvé pour cet utilisateur."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        # Vérifie si l'utilisateur a déjà un budget
        if Budget.objects.filter(utilisateur=request.user).exists():
            return Response({"detail": "Vous avez déjà un budget."}, status=status.HTTP_400_BAD_REQUEST)

        # Créer un budget
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            budget = serializer.save(utilisateur=request.user)
            # Assurer que la valeur actuelle est bien définie
            budget.valeur_actuelle = budget.valeur_initiale
            budget.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            budget = Budget.objects.get(utilisateur=request.user)
        except Budget.DoesNotExist:
            return Response({"detail": "Aucun budget trouvé."}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data.pop('valeur_actuelle', None)

        serializer = BudgetSerializer(budget, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            budget = Budget.objects.get(utilisateur=request.user)
            budget.delete()
            return Response({"detail": "Budget supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)
        except Budget.DoesNotExist:
            return Response({"detail": "Aucun budget trouvé."}, status=status.HTTP_404_NOT_FOUND)
