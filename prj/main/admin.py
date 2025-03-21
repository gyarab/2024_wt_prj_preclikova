from django.contrib import admin
from.models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author", "description"]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name","birth_year","description"]

# Register your models here.

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)