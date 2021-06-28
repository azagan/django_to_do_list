from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView
from .forms import TaskForm, SubtaskForm

from .models import Tasks, Subtasks



class TaskCreateView(CreateView):
    template_name = 'to_do_list/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('to_do_list:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskEditView(UpdateView):
    template_name = 'to_do_list/task_form.html'
    model = Tasks
    form_class = TaskForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtasks'] = Subtasks.objects.all()
        return context


class SubTaskEditView(UpdateView):
    template_name = 'to_do_list/subtask_form.html'
    model = Subtasks
    form_class = SubtaskForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def index(request):
    tasks = Tasks.objects.all()

    form = SubtaskForm()

    if request.method == 'POST' and not request.is_ajax():
        form = SubtaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    if request.method == 'POST' and request.is_ajax():
        sub_id = request.POST.get('getdata', None)
        subtask = Subtasks.objects.get(id=sub_id)
        subtask.delete()

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'to_do_list/index.html', context=context)
