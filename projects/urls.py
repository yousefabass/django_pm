from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.ProjectListView.as_view(), name= "project_list"),
    path("projects/create", views.ProjectCreateView.as_view(), name= "project_create"),
    path('projects/edit/<int:pk>', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='project_delete'),

    path("tasks/create", views.TaskCreateView.as_view(), name= "task_create"),
    path("tasks/edit/<int:pk>", views.TaskUpdateView.as_view(), name= "task_update"),
    path("tasks/delete/<int:pk>", views.TaskDeleteView.as_view(), name= "task_delete"),

]
