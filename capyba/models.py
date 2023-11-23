from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    primeiro_nome = models.CharField(max_length=254)
    sobrenome = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return self.primeiro_nome
