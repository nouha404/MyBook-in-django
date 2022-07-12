from django.db import models


# Create your models here.


class BooksModel(models.Model):
    title = models.CharField(max_length=55, verbose_name='Titre')
    description = models.TextField(verbose_name='Description')
    publier = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Livre'

    def __str__(self):
        return self.title

    @property
    def lenword(self):
        return f'{len(self.description.split())} mots'
