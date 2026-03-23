from django.db import models

# Create your models here.
class Ginasio(models.Model):
    nome = models.CharField(max_length = 100)
    socios = models.IntegerField()

    def __str__(self):
        return f'Ginásio: {self.nome} Número de sócios: {self.socios}'