from django.urls import path
from .views import task_views

urlpatterns = [
    path('tasks/list/', task_views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', task_views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', task_views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/edit/', task_views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', task_views.TaskDeleteView.as_view(), name='task_delete'),
]
