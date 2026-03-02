from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Priority(models.TextChoices):
    NONE = 'NONE', 'Sem prioridade'
    LOW = 'LOW', 'Baixa'
    MEDIUM = 'MEDIUM', 'Média'
    HIGH = 'HIGH', 'Alta'


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_data = models.DateField()

    priority = models.CharField(
        max_length=15,
        choices=Priority.choices,
        default=Priority.NONE
    )

    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-created_at']
    
    def clean(self):
        if self.due_data < timezone.now().date():
            raise ValidationError('A data da tarefa não pode ser anterior ao dia atual.')
        
    def is_overdue(self):
        return (not self.completed and self.due_data < timezone.now().date())
    
    def __str__(self):
        return self.title
