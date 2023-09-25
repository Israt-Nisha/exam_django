from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import FormView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import TaskModel
from . forms import TaskForm

# Create your views here.

class MyTemplateView(TemplateView):
    template_name = 'home.html'

class TaskFormView(CreateView):
    model = TaskModel
    template_name = 'store_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('showtask')
    
    
class TaskListView(ListView):
    model = TaskModel
    template_name = 'show_task.html'
    context_object_name = 'data'
    
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=False)
    
class TaskUpdateView(UpdateView):
    model = TaskModel
    template_name = 'store_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('showtask')
    
class DeleteTaskView(DeleteView):
    model = TaskModel
    template_name = 'delete.html'
    success_url = reverse_lazy('showtask')

    
    
class CompletedTasksView(ListView):
    model = TaskModel
    template_name = 'complete_task.html'
    context_object_name = 'complete_task'
    
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=True)
 
class CompleteTaskView(UpdateView):
    model = TaskModel
    fields = ['is_completed']
    template_name = 'task_com.html'
    success_url = reverse_lazy('completed_tasks') 
      

    
