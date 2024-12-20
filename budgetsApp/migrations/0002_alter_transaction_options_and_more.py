# Generated by Django 5.1.4 on 2024-12-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-cree_le']},
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='created_at',
            new_name='cree_le',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='amount',
            new_name='montant',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='current_amount',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='initial_amount',
        ),
        migrations.AddField(
            model_name='budget',
            name='montant_actuel',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='montant_initial',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('revenu', 'Revenu'), ('depense', 'Dépense')], max_length=10),
        ),
    ]
