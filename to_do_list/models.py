from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=120, blank=False, verbose_name='Цель')
    is_active = models.BooleanField(default=True, blank=False)
    published = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Цели'
        verbose_name = 'Цель'
        ordering = ['-published']


class Subtasks(models.Model):
    goals = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='subtasks', verbose_name='Цель')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    name = models.CharField(max_length=120, db_index=True, verbose_name='Задача')
    complete = models.BooleanField(default=False, verbose_name='Выполнено')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['pk']
