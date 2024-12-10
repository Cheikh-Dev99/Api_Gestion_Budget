from django.db import models
from .models import User

class Budget(models.Model):
    user = models.OneToOneField(User, )