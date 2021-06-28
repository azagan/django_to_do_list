from django.forms import ModelForm, CharField, Textarea
from .models import Tasks, Subtasks


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ('title',)
        labels = {'title': 'Цель'}


class SubtaskForm(ModelForm):
    description = CharField(required=False, widget=Textarea(attrs={'rows': 4, 'cols': 40}), label='Описание')

    class Meta:
        model = Subtasks
        fields = ('name', 'description', 'goals', 'complete')
