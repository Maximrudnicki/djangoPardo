from django.forms import ModelForm
from .models import EnglishWord, ListOfWordSets


class EnglishWordForm(ModelForm):
    class Meta:
        model = EnglishWord
        fields = '__all__'


class ListOfWordSetsForm(ModelForm):
    class Meta:
        model = ListOfWordSets
        fields = '__all__'
