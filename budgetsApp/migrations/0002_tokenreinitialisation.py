# Generated by Django 5.1.4 on 2024-12-12 20:09

import budgetsApp.models.reinitialisation_models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenReinitialisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('expire_a', models.DateTimeField(default=budgetsApp.models.reinitialisation_models.default_expiration_time)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]