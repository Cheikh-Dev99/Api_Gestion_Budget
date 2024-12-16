from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models.budget import Budget
from ..serializers.budget_serializer import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les budgets des utilisateurs.
    - GET : Lister tous les budgets ou récupérer un budget spécifique.
    - POST : Créer un nouveau budget.
    - PUT/PATCH : Mettre à jour un budget existant.
    - DELETE : Supprimer un budget existant.
    """
    queryset = Budget.objects.all()  # Récupère tous les budgets
    serializer_class = BudgetSerializer

    # Si vous voulez personnaliser les réponses de la méthode GET ou POST
    def list(self, request):
        """
        Lister tous les budgets.
        """
        budgets = self.get_queryset()
        serializer = self.get_serializer(budgets, many=True)  # Sérialiser tous les budgets
        return Response(serializer.data)

    def create(self, request):
        """
        Créer un nouveau budget.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
