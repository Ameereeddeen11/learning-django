from unicodedata import name
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Brend(models.Model):
    brend_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_brend = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name_brend()