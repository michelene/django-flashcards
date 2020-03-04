from django.db import models
from django.conf import settings
from mdeditor.fields import MDTextField


class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Card(models.Model):
    question = MDTextField()
    answer = MDTextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='categories')
    # I want a Card to be able to have multiple Categories. How can I do this?

    def __str__(self):
        return self.question
