from django.db import models

class Budget(models.Model):
    montant_initial = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Montant initial du budget
    montant_actuel = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Montant actuel après modification

    def save(self, *args, **kwargs):
        """
        Lors de la création, définir montant_actuel à la valeur de montant_initial.
        """
        if not self.pk:  # Si le budget est nouveau
            self.montant_actuel = self.montant_initial
        super(Budget, self).save(*args, **kwargs)

    def update_amount(self, transaction):
        """
        Met à jour le montant actuel du budget en fonction de la transaction.
        :param transaction: Une instance du modèle Transaction
        """
        if transaction.type == "revenu":
            self.montant_actuel += transaction.montant
        elif transaction.type == "depense":
            self.montant_actuel -= transaction.montant
        self.save()

    def __str__(self):
        return f"Budget avec un montant actuel de {self.montant_actuel:,.2f} €"
