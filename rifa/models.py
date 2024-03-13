from django.db import models

# Create your models here.


class Sorteio(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    numero_rifa = models.IntegerField()
    aprovado = models.BooleanField(default=False)


    def __str__(self):
        return self.nome
    
class RifaTexto(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto