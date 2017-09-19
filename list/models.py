from django.db import models

class Lista(models.Model):
    STATUS = (
        ('P', 'Pendente'),
        ('F', 'Feita'),
        ('E', 'Excluida'),
    )
    descricao_tarefa = models.CharField(max_length=1000)
    ordem_tarefa = models.IntegerField()
    status_tarefa = models.CharField(max_length=1, choices=STATUS, default='P')