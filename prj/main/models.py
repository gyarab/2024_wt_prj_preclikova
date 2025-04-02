from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, default="")
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey("Genre", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Book <{self.id}> {self.name}"
        
class Author(models.Model):
   name = models.CharField(max_length=300)
   birth_year = models.IntegerField(blank=True, null=True)
   description = models.TextField(blank=True, default="")

   def __str__(self):
        return f"Author <{self.id}> {self.name}"
   
class Genre(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return f"Genre <{self.id}> {self.name}"
    
class Reader(models.Model):
   name = models.CharField(max_length=300)
   
   def __str__(self):
        return f"Reader <{self.id}> {self.name}"
   
class ReadingRecord(models.Model):
    reader = models.ForeignKey("Reader", on_delete=models.CASCADE, default=1, null=False)
    book = models.ForeignKey("Book", on_delete=models.CASCADE, default=1, null=False)
    date_add = models.DateField()
    state = models.TextField(max_length=1, choices={
        "A": "Chci číst",
        "B": "Právě čtu",  
        "C": "Přečteno",   
        "D": "Nechci číst"
    })
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    text = models.TextField(blank=True, default="")
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"ReadingRecord <{self.id}>"
   