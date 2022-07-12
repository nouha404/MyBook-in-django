from django.contrib import admin

from livre.models import BooksModel


# Register your models here.
@admin.register(BooksModel)
class MyBooks(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'publier',
        'lenword'
    )


