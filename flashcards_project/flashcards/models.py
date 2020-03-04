from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Card(models.Model):
    title = models.CharField(max_length=100, default='Card Title')
    question = RichTextField()
    answer = RichTextField()
    categories = models.ManyToManyField(Category, related_name='cards')

    def __str__(self):
        return self.title


class Deck(models.Model):
    title = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card, related_name='decks')

    def __str__(self):
        return self.title


