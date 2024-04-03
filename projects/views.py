from urllib import request
from django.shortcuts import render 
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms
from . import models
# Create your views here.
class ProjectListView(ListView):
    model = models.Project
    template_name = "projects/list.html"
    paginate_by = 3
    def get_queryset(self):
        query_set = super().get_queryset() # نقوم بجلب القيمة الافتراضية للدالة وحفظها داخل متغير
        # القيمة الافتراضية هو الاستعلام التالي
            # Project.objects.all()
        # نقوم بعدها بعمل فلترة للمشاريع باستخدام رقم المستخدم و كلمة البحث
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)



class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = "projects/create.html"
    success_url = reverse_lazy("project_list")


class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = "projects/update.html"
    def get_success_url(self):
        return reverse("project_update",args=[self.object.id])


class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name= "projects/delete.html"
    success_url = reverse_lazy("project_list")

class TaskCreateView(CreateView):
    model = models.Task
    fields = ["project", "description"]
    http_method_names= ["post"]
    def get_success_url(self):
        return reverse("project_update",args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    model = models.Task
    fields = [ "is_completed"]
    http_method_names= ["post"]
    def get_success_url(self):
        return reverse("project_update",args=[self.object.project.id])

class TaskDeleteView(DeleteView):
    model = models.Task
    def get_success_url(self):
        return reverse("project_update",args=[self.object.project.id])

