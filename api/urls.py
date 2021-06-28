from django.urls import path, include, re_path

from .views import TaskListView, SubTaskListView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="TO DO LIST API",
        default_version="v0"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'api'

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('tasks/', TaskListView.as_view()),
    path('subtasks/<int:pk>/', SubTaskListView.as_view())
]
