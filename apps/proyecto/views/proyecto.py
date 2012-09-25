from apps.proyecto.forms import ProjectForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from apps.proyecto.models import Project
from apps.proyecto.views.views import LoginRequired

class proylist(LoginRequired,ListView):
    model = Project
    template_name = 'project/list.html'
    paginate_by = 5
    
class newProject(LoginRequired,CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('Lista_view')
    
class editProject(LoginRequired,UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('Lista_view')
    
class delProject(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    def get_success_url(self):
        return reverse('Lista_view')
    