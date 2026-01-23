from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')    
    list_filter = ('published_date', 'publication_year')

admin.site.register(Books, BooksAdmin)
