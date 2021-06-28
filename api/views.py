from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import TaskListSerializer, Tasks, SubtaskListSerializer, Subtasks


class TaskListView(APIView):
    def get(self, request):
        tasks = Tasks.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)


class SubTaskListView(APIView):
    def get(self, request, pk):
        subtask = Subtasks.objects.filter(goals__id=pk)
        serializer = SubtaskListSerializer(subtask, many=True)
        return Response(serializer.data)
