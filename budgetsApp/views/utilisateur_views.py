# budgetsApp/views/utilisateur_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.utilisateur_serializers import InscriptionUtilisateurSerializer


class InscriptionUtilisateurView(APIView):
    def post(self, request):
        serializer = InscriptionUtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Inscription réussie"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
