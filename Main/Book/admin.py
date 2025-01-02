from django.contrib import admin
from Book.models import Book, Publisher, Author, ParentCategory, ChildCategory


@admin.register(Book)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = (
        'book_name', 'number_page', 'slug', 'discount', 'unit_price', 'part_of_book', 'about_book', 'publisher',
        'author',
        'is_available', 'created', 'parent_category')
    list_filter = ('is_available', 'unit_price', 'number_page')
    prepopulated_fields = {
        'slug': ('book_name',)
    }


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'publisher_name', 'slug', 'manager', 'about_publisher'
    )
    list_filter = ('publisher_name',)

    prepopulated_fields = {
        'slug': ('publisher_name',)
    }


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'slug', 'birthday', 'from_country', 'about_author')

    prepopulated_fields = {
        'slug': ('first_name', 'last_name')
    }
