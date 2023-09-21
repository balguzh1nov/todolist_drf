from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api_overview"),
    path('task-list/', views.taskList, name="task_list"),
    path('details/<str:pk>/', views.details, name="details"),
    path('create/', views.create, name="create"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),
]