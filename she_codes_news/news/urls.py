from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/',views.AddStoryView.as_view(),name='newStory'),
    path('search-results/',views.SearchResultsView.as_view(),name='searchResults'),
    path('update-news/<int:pk>',views.UpdateNewsView.as_view(),name='updateNews'),
    path('delete-news/<int:pk>',views.DeleteNewsView.as_view(),name='deleteNews'),
    path('favorite/<int:user_id>',views.FavoriteNewsView.as_view(), name="favoriteNews"),
]