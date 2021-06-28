from django.urls import path, include

from .views import index, TaskEditView, TaskDeleteView, TaskCreateView, SubTaskEditView

app_name = 'to_do_list'

urlpatterns = [
    path('', index, name='index'),
    path('update_task/<int:pk>/', TaskEditView.as_view(), name='update_task'),
    path('update_subtask/<int:pk>', SubTaskEditView.as_view(), name='update_subtask'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
    path('add', TaskCreateView.as_view(), name='add'),
]
