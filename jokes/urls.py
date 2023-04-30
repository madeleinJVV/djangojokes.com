from django.urls import path

from .views import JokeListView, JokeDetailView, JokeCreateView, JokeUpdateView

app_name = 'jokes'
urlpatterns = [
    path('', JokeListView.as_view(), name='list'),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
    path('joke/create/', JokeCreateView.as_view(), name='create'),
    path('joke/<int:pk>/update', JokeUpdateView.as_view(), name='update'),
]