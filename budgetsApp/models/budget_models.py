# budgetsApp/models/budget_models.py
from django.db import models
from django.conf import settings
from decimal import Decimal


class Budget(models.Model):
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    valeur_initiale = models.DecimalField(max_digits=10, decimal_places=2)
    valeur_actuelle = models.DecimalField(max_digits=10, decimal_places=2)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.valeur_initiale <= 0:
                raise ValueError("La valeur initiale doit être positive.")
            self.valeur_actuelle = self.valeur_initiale
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Budget de {self.utilisateur}"

    def update_valeur_actuelle(self, montant, type_transaction):
        if montant <= 0:
            raise ValueError("Le montant de la transaction doit être positif.")

        if type_transaction == 'revenu':
            # Si c'est un revenu, on ajoute simplement au budget
            self.valeur_actuelle += montant
        elif type_transaction == 'depense':
            # Si c'est une dépense, on soustrait du budget
            self.valeur_actuelle -= montant

        self.save()
