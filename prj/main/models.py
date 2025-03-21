from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, default="")
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Book <{self.id}> {self.name}"
        
class Author(models.Model):
   name = models.CharField(max_length=300)
   birth_year = models.IntegerField(blank=True, null=True)
   description = models.TextField(blank=True, default="")

   def __str__(self):
        return f"Author <{self.id}> {self.name}"
    
   