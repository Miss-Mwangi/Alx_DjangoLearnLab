from django.contrib import admin
from .models import Author, Book

# Register the Autor and Book models in the admin interface.
admin.site.register(Author)
admin.site.register(Book)
