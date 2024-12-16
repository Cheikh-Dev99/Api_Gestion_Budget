from django.db import models
from decimal import Decimal

class Budget(models.Model):
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Montant initial du budget
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Montant actuel après modification

    def save(self, *args, **kwargs):
        """
        Lors de la création, définir current_amount à la valeur de initial_amount.
        """
        if not self.pk:  # Si le budget est nouveau
            self.current_amount = self.initial_amount
        # Convertir current_amount en float
        self.current_amount = float(self.current_amount)
        super(Budget, self).save(*args, **kwargs)

    def update_amount(self, transaction):
        """
        Met à jour le montant actuel du budget en fonction de la transaction.
        :param transaction: Une instance du modèle Transaction
        """
        if transaction.type == "income":
            self.current_amount += float(transaction.amount)  # Ajout d'un revenu
        elif transaction.type == "expense":
            self.current_amount -= float(transaction.amount)  # Soustraction d'une dépense
        self.save()

    def __str__(self):
        return f"Budget avec un montant actuel de {self.current_amount:,.2f}€"