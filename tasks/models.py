from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='tasks')
    nome_task = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f'{self.nome_task} - {self.descricao}'
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['nome_task']