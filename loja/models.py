from django.db import models

# Create your models here.
class Loja(models.Model):
    nome = models.CharField(max_length = 100)
    localidade = models.CharField(max_length = 100)

    def __str__(self):
        return f'Loja: {self.nome} Localidade: {self.localidade}'