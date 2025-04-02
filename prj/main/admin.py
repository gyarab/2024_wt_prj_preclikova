from django.contrib import admin
from.models import Book, Author, Genre, Reader, ReadingRecord

class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author", "description", "genre"]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name","birth_year","description"]

class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ReaderAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ReadingRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "date_add", "state",
                    "date_start", 
                    "date_end", "text", "rating" ]

# Register your models here.

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(ReadingRecord, ReadingRecordAdmin)