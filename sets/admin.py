from django.contrib import admin

from .models import WordSet


class WordSetAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(WordSet, WordSetAdmin)
