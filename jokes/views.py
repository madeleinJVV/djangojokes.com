from django.views.generic import CreateView, ListView, DetailView,  UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Joke

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question','answer']

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

