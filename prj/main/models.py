from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)

