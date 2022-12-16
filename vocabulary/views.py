from django.shortcuts import render, redirect
from .models import EnglishWord, ListOfWordSets
from .forms import EnglishWordForm


def index(request):
    english_words = EnglishWord.objects.all()
    list_of_word_sets = ListOfWordSets.objects.all()
    context = {
        'english_words': english_words,
        'list_of_word_sets': list_of_word_sets
    }
    return render(request, 'index.html', context)


def add_english_word(request):
    form = EnglishWordForm()
    if request.method == 'POST':
        form = EnglishWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dictionary')

    context = {'form': form}
    return render(request, 'add_english_word.html', context)


def update_english_word(request, eng_id):
    english_word = EnglishWord.objects.get(id=eng_id)
    form = EnglishWordForm(instance=english_word)

    if request.method == 'POST':
        form = EnglishWordForm(request.POST, instance=english_word)
        if form.is_valid():
            form.save()
            return redirect('dictionary')

    context = {'form': form}
    return render(request, 'update_english_word.html', context)


def delete_english_word(request, eng_id):
    word = EnglishWord.objects.get(id=eng_id)

    if request.method == 'POST':
        word.delete()
        return redirect('dictionary')

    return render(request, 'delete_english_word.html', {'obj': word})
