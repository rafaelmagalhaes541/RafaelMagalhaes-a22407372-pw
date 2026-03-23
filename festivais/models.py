from django.db import models

# Create your models here.
class Festival(models.Model):
    nome = models.CharField(max_length = 100)
    tipo = models.CharField(max_length = 25)

    def __str__(self):
        return f'Festival: {self.nome} Tipo: {self.tipo}'