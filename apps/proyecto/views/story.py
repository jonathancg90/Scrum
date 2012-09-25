from apps.proyecto.forms import StoryForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from apps.proyecto.models import UserStory, Sprint
from apps.proyecto.views.views import LoginRequired
from django.http import HttpResponseRedirect

class storylist(LoginRequired,ListView):
    model = UserStory
    template_name = 'story/list.html'
    paginate_by = 5
    
    def get_queryset(self):
        sprint_id = self.kwargs.get('pk', 0)
        qs = UserStory.objects.filter(sprint_id = sprint_id)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super(storylist,
            self).get_context_data(**kwargs)

        context['sprint'] = get_object_or_404(
            Sprint, id=self.kwargs.get('pk', 0))
        return context
    
class newStory(LoginRequired,CreateView):
    model = UserStory
    template_name = 'story/create.html'
    form_class = StoryForm
    
    def get_context_data(self, **kwargs):
        context = super(newStory,
            self).get_context_data(**kwargs)

        context['sprint'] = get_object_or_404(
            Sprint, id=self.kwargs.get('pk', 0))
        return context
    
    def get_success_url(self):
        return reverse('Lista_story_view',kwargs={'pk':self.object.sprint.id})
    
    def form_valid(self,form):
        story = form.save(commit=False)
        story.sprint=  get_object_or_404(Sprint, id=self.kwargs.get('pk', 0))
        story.save()
        self.object= story
        return HttpResponseRedirect(self.get_success_url())
    
    
class editStory(LoginRequired,UpdateView):
    model = UserStory
    template_name = 'story/update.html'
    form_class = StoryForm
    context_object_name = 'story'

    def get_success_url(self):
        return reverse('Lista_story_view',kwargs={'pk':self.object.sprint.id})
    
class delStory(DeleteView):
    model = UserStory
    template_name = 'story/delete.html'
    context_object_name = 'story'
    
    def get_success_url(self):
        return reverse('Lista_story_view',kwargs={'pk':self.object.sprint.id})