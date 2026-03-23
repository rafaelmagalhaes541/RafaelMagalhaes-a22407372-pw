from django.db import models

# Create your models here.
class Escola(models.Model):
    nome = models.CharField(max_length = 100)
    agrupamento = models.CharField(max_length = 150)

    def __str__(self):
        return f'Escola {self.nome} do agrupamento {self.agrupamento}'
