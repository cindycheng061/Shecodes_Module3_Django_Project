from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.db.models import F

# the main page
class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_stories'] = NewsStory.objects.all()[:4]
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        # print(NewsStory.objects.all()[:4])
        return context
# the Story page
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

# creat a new story, the page with form, able to add a new story
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




