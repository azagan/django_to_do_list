from rest_framework import serializers
from to_do_list.models import Tasks, Subtasks


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class SubtaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtasks
        fields = '__all__'
