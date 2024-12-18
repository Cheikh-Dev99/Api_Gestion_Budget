# budgetsApp/views/connexion_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from knox.models import AuthToken
from ..serializers.connexion_serializer import ConnexionUtilisateurSerializer


class ConnexionUtilisateurView(APIView):
    def post(self, request):
        serializer = ConnexionUtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            utilisateur = serializer.validated_data["utilisateur"]
            token = AuthToken.objects.create(user=utilisateur)[1]
            return Response({
                "message": "Connexion réussie",
                "utilisateur": {
                    "id": utilisateur.id,
                    "prenom": utilisateur.prenom,
                    "nom": utilisateur.nom,
                    "email": utilisateur.email,
                    "telephone": utilisateur.telephone,
                },
                "token": token,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
