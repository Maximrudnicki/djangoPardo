from django.contrib import admin
from .models import EnglishWord, ListOfWordSets


class EnglishWordAdmin(admin.ModelAdmin):
    list_display = ('eng', 'rus')


class ListOfWordSetsAdmin(admin.ModelAdmin):
    list_display = ('name_of_word_set',)


admin.site.register(EnglishWord, EnglishWordAdmin)
admin.site.register(ListOfWordSets, ListOfWordSetsAdmin)
