# budgetsApp/models/utilisateur_models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.db import models


class GestionnaireUtilisateur(BaseUserManager):
    def creer_utilisateur(self, prenom, nom, telephone, email, password=None):
        if not email:
            raise ValueError("L'utilisateur doit avoir une adresse email")
        email = self.normalize_email(email)
        utilisateur = self.model(
            prenom=prenom, nom=nom, telephone=telephone, email=email)
        utilisateur.set_password(password)
        utilisateur.save(using=self._db)
        return utilisateur

    def create_superuser(self, prenom, nom, telephone, email, password=None):
        utilisateur = self.creer_utilisateur(
            prenom, nom, telephone, email, password)
        utilisateur.is_staff = True
        utilisateur.is_superuser = True
        utilisateur.save(using=self._db)
        return utilisateur


class Utilisateur(AbstractBaseUser, PermissionsMixin):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = GestionnaireUtilisateur()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['prenom', 'nom', 'telephone']

    def __str__(self):
        return f"{self.prenom} {self.nom}"

