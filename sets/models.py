from django.db import models


class WordSet(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.name}"
