from django.forms import ModelForm
from .models import Tasks, Subtasks


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ('title',)
        labels = {'title': 'Цель'}


class SubtaskForm(ModelForm):
    class Meta:
        model = Subtasks
        fields = ('name', 'description', 'goals', 'complete')
