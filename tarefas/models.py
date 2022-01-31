from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length=40)
    prioridade = models.IntegerField()

    def __str__(self):
        return f'{self.nome} (prioridade: {self.prioridade})'
