# budgetsApp/models/transaction_models.py
from django.db import models
from django.conf import settings
from django.utils import timezone
from ..models.budget_models import Budget
from decimal import Decimal
from django.core.exceptions import ValidationError


class Transaction(models.Model):
    type_transaction = models.CharField(
        max_length=10, choices=[('revenu', 'Revenu'), ('depense', 'Dépense')])
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date_transaction = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Récupération du budget lié
        budget = self.budget

        # Conversion de self.montant en Decimal si c'est un float
        if isinstance(self.montant, float):
            self.montant = Decimal(str(self.montant))

        # Vérification de la transaction (dépense ou revenu)
        if self.type_transaction == 'depense':
            # Vérifie si la dépense dépasse le budget disponible
            if budget.valeur_actuelle - self.montant < 0:
                raise ValidationError(
                    "La dépense dépasse le budget disponible. Transaction non autorisée.")

            # Vérifie si après la dépense, il reste au moins 40% du budget
            if budget.valeur_actuelle - self.montant < (Decimal(0.4) * budget.valeur_initiale):
                raise ValidationError(
                    "La dépense ne peut être effectuée car il reste moins de 40% du budget.")

            # Mise à jour de la valeur actuelle du budget
            budget.valeur_actuelle -= self.montant
        elif self.type_transaction == 'revenu':
            # Ajout du revenu au budget
            budget.valeur_actuelle += self.montant

        # Sauvegarde du budget mis à jour
        budget.save()

        # Sauvegarde de la transaction
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type_transaction.capitalize()} - {self.montant} ({self.date_transaction})"
