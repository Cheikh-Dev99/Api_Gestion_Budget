from django.db import models
from .budget import Budget  
from decimal import Decimal

class Transaction(models.Model):
    TYPES_TRANSACTION = [
        ('revenu', 'Revenu'),
        ('depense', 'Dépense'),
    ]
    id = models.AutoField(primary_key=True) 
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE, related_name='transactions')  # Associer une transaction à un budget
    montant = models.DecimalField(max_digits=10, decimal_places=2)  # Montant de la transaction
    type = models.CharField(max_length=10, choices=TYPES_TRANSACTION)  # Type de transaction (revenu ou dépense)
    description = models.TextField(blank=True, null=True)  # Description facultative
    cree_le = models.DateTimeField(auto_now_add=True)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)  # Dernière date de modification

    class Meta:
        ordering = ['-cree_le']  # Trier les transactions par date décroissante

    def __str__(self):
        return f"{self.get_type_display()} - {self.montant:,.2f} €"



    def get_absolute_url(self):
        return f"/transactions/{self.pk}/"
