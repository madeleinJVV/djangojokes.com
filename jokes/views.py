from django.views.generic import CreateView, ListView, DetailView,  UpdateView

from .models import Joke

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question','answer']

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

