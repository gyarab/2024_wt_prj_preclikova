
from django.shortcuts import render
from main.models import Book

# Create your views here.

def get_homepage(request): 
    books = Book.objects.all().order_by("name")

    context = {  

        #SELECT * from Books;
        "books": Book.objects.all(),
    }

 #   print("HOST", request.get_host())
 #   print("URL", request.path)

    # check if search parameter is in the request
    if request.GET.get("search"):
        # filter books based on the search parameter
        print("SEARCH", request.GET.get("search"))

    return render(
        request, "main/homepage.html", context
        )
   