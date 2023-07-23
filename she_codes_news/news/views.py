from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.db.models import F

from .forms import UpdateNewsForm
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib import messages


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

class SearchResultsView(generic.ListView):
    template_name = 'news/searchResults.html'
    context_object_name = 'stories'
    def get_queryset(self):
        category = self.request.GET.get('category', '')
        if category:
            return NewsStory.objects.filter(category=category)
        


class UpdateNewsView(generic.UpdateView):
    model = NewsStory
    form_class = UpdateNewsForm
    context_object_name = 'updatenewsform'
    template_name = 'news/updateNews.html'
    success_url = reverse_lazy('news:index')
    
    def update_news(request,id):
        instance = NewsStory.objects.get(pk = id)
        if request.method == 'POST':
            form = UpdateNewsForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('news:index')
        else:
            form = UpdateNewsForm(instance=instance)
            return render(request,'news/updateNews.html',{'form':form})
        

class DeleteNewsView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteNews.html'
    success_url = reverse_lazy('news:index')
    def delete_news(request, id):
        instance = get_object_or_404(NewsStory, pk=id)
        context = {'instance': instance}    
        if request.method == 'GET':
            return render(request, 'news/deleteNews.html',context)
        elif request.method == 'POST':
            instance.delete()
            messages.success(request,  'The post has been deleted successfully.')
            return redirect('news:index')
        

# add favourite stories to user
from django.http import HttpResponseRedirect



class FavoriteNewsView(generic.ListView):
    model=NewsStory
    template_name = 'news/favoriteNews.html'
    # display user favorite News
    def get(self, request, *args, **kwargs):
        # The user_id is extracted from the URL pattern
        user_id = self.kwargs.get('user_id')
        favorite_stories = NewsStory.objects.filter(favorites=user_id)
        context = {
            'favorite_stories': favorite_stories,
        }
        return render(request, self.template_name, context)
    # use add favorite news to user,
class AddFavoriteView(generic.ListView):
    model=NewsStory
    template_name = 'news/addfavorite.html'
    def get(self, request, *args, **kwargs):
        # verify already favorited, then add favorites to user
        if self.object.favorites.filter(id=self.request.user.id ) is False: 
            self.object.favorites.add(self.request.user.id)
        return redirect('news:addFavorite', kwargs={"pk": self.request.user.id})
        
