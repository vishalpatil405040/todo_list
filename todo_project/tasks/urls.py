from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),              # Read (list all)
    path('add/', views.task_create, name='task-create'),      # Create
    path('<int:pk>/edit/', views.task_update, name='task-update'),  # Update
    path('<int:pk>/delete/', views.task_delete, name='task-delete'),  # Delete
]