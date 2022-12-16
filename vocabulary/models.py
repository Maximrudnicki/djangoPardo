from django.db import models


class EnglishWord(models.Model):
    eng = models.CharField(max_length=255)
    rus = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.eng} - {self.rus}"


class ListOfWordSets(models.Model):
    name_of_word_set = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.name_of_word_set}"
