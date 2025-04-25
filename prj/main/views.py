from django.shortcuts import render
from main.models import Book

# Create your views here.

def get_homepage(request): 
    context ={ 
        "svatek":"Libor",

        #SELECT * from Books;
        "books": Book.objects.all()
    }
    return render(request, "main/homepage.html", context)
   
