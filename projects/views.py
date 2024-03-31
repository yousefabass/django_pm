from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from . import models, forms
from . import models
# Create your views here.
class ProjectListView(ListView):
    model = models.Project
    template_name = "projects/list.html"


class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = "projects/create.html"
    success_url = reverse_lazy("project_list")