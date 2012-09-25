from apps.proyecto.forms import SprintForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from apps.proyecto.models import Sprint, Project
from apps.proyecto.views.views import LoginRequired
from django.http import HttpResponseRedirect

class sprintlist(LoginRequired,ListView):
    model = Sprint
    template_name = 'sprint/list.html'
    paginate_by = 5

    def get_queryset(self):
        project_id = self.kwargs.get('pk', 0)
        qs = Sprint.objects.filter(project_id = project_id)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super(sprintlist,
            self).get_context_data(**kwargs)

        context['project'] = get_object_or_404(
            Project, id=self.kwargs.get('pk', 0))
        return context
    
    
class newSprint(LoginRequired,CreateView):
    model = Sprint
    template_name = 'sprint/create.html'
    form_class = SprintForm
    
    def get_context_data(self, **kwargs):
        context = super(newSprint,
            self).get_context_data(**kwargs)

        context['project'] = get_object_or_404(
            Project, id=self.kwargs.get('pk', 0))
        return context
    
    def get_success_url(self):
        return reverse('Lista_sprint_view',kwargs={'pk':self.object.project.id})
    
    def form_valid(self,form):
        sprint = form.save(commit=False)
        sprint.project=  get_object_or_404(Project, id=self.kwargs.get('pk', 0))
        sprint.save()
        self.object= sprint
        return HttpResponseRedirect(self.get_success_url())
    
    
class editSprint(LoginRequired,UpdateView):
    model = Sprint
    template_name = 'sprint/update.html'
    form_class = SprintForm
    context_object_name = 'sprint'

    def get_success_url(self):
        return reverse('Lista_sprint_view',kwargs={'pk':self.object.project.id})
    
    
class delSprint(DeleteView):
    model = Sprint
    template_name = 'sprint/delete.html'
    context_object_name = 'sprint'
    
    def get_success_url(self):
        return reverse('Lista_sprint_view',kwargs={'pk':self.object.project.id})