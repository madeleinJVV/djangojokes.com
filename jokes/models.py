from django.db import models

# Create your models here.

class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.question
    
