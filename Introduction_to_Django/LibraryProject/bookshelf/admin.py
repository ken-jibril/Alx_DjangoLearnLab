from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author', 'isbn_number')    
    list_filter = ('published_date', 'language')

admin.site.register(Books, BooksAdmin)
