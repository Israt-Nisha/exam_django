from django.urls import path

from . import views
urlpatterns = [
    path('', views.TemplateView.as_view(template_name='home.html')),
    path('store_task/', views.TaskFormView.as_view(), name='storetask'),
    path('show_task/', views.TaskListView.as_view(), name='showtask'),
    path('<pk>/delete/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('<pk>/edit/', views.TaskUpdateView.as_view(), name='edit_task'),
    path('completed-tasks/', views.CompletedTasksView.as_view(), name='completed_tasks'),
    path('complete/<int:pk>/', views.CompleteTaskView.as_view(), name='complete_task'),
   
  
   
    
]