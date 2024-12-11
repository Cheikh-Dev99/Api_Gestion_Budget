# budgetsApp/models/utilisateur_models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UtilisateurManager(BaseUserManager):
    def create_user(self, prenom, nom, telephone, email, password=None):
        if not email:
            raise ValueError("L'email doit être fourni")
        utilisateur = self.model(
            email=self.normalize_email(email),
            prenom=prenom,
            nom=nom,
            telephone=telephone,
        )
        utilisateur.set_password(password)
        utilisateur.save(using=self._db)
        return utilisateur

    def create_superuser(self, prenom, nom, telephone, email, password=None):
        utilisateur = self.create_user(
            email=email,
            prenom=prenom,
            nom=nom,
            telephone=telephone,
            password=password,
        )
        utilisateur.is_admin = True
        utilisateur.save(using=self._db)
        return utilisateur

class Utilisateur(AbstractBaseUser):
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['prenom', 'nom', 'telephone']

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
