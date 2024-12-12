# budgetsApp/models/reinitialisation_models.py
from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from ..models.utilisateur_models import Utilisateur

def default_expiration_time():
    return now() + timedelta(hours=1)

class TokenReinitialisation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="tokens")
    token = models.CharField(max_length=255, unique=True)
    expire_a = models.DateTimeField(default=default_expiration_time)

    def est_valide(self):
        return now() < self.expire_a
