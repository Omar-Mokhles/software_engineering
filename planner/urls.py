from django.urls import path
from . import views

app_name = 'planner'

urlpatterns = [
    
    # Main Dashboard 
    path('', views.home_view, name='home_view'),

    # Subject URLs
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/new/', views.subject_create, name='subject_create'),
    path('subjects/<int:pk>/', views.subject_detail, name='subject_detail'),  
    path('subjects/<int:pk>/edit/', views.subject_update, name='subject_update'),
    path('subjects/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
    path('subjects/<int:subject_pk>/tasks/new/', views.task_create, name='task_create_in_subject'),
    
    # Task URLs
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/new/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
]