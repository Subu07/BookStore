from django.contrib import admin

from .models import Book, Category, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Author, AuthorAdmin)
