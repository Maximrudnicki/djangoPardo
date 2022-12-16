from django.shortcuts import render
from .models import WordSet


def index(request):
    word_sets = WordSet.objects.all()

    context = {
        'word_sets': word_sets
    }

    return render(request, 'index.html', context)
