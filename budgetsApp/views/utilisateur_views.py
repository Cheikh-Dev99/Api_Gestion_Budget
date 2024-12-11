# budgetsApp/views/utilisateur_views.py
from rest_framework import status, generics
from rest_framework.response import Response
from ..serializers.utilisateur_serializers import UtilisateurSerializer

class InscriptionUtilisateurView(generics.CreateAPIView):
    serializer_class = UtilisateurSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            utilisateur = serializer.save()
            return Response({
                'message': 'Utilisateur créé avec succès',
                'utilisateur': {
                    'prenom': utilisateur.prenom,
                    'nom': utilisateur.nom,
                    'telephone': utilisateur.telephone,
                    'email': utilisateur.email
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
