from django.contrib import admin
from .models import Tasks, Subtasks


class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'published')
    list_display_links = ('title', 'is_active')
    search_fields = ('title',)


class SubTasksAdmin(admin.ModelAdmin):
    list_display = ('goals', 'name')
    list_display_links = ('goals', 'name')
    search_fields = ('goals',)


admin.site.register(Tasks, TasksAdmin)
admin.site.register(Subtasks, SubTasksAdmin)