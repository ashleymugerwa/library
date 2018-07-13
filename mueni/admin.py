from django.contrib import admin

from mueni.models import Author, Book, Category, Member, LibraryRecord, State


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

    @staticmethod
    def excerpt(obj):
        return obj.get_excerpt(20)


admin.site.register(State, StateAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_books', 'awards')
    search_fields = ('name', 'number_of_books', 'awards')

    @staticmethod
    def excerpt(obj):
        return obj.get_excerpt(20)


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'category', 'title', 'edition', 'pub_date', 'isbn')
    search_fields = ('author__name', 'category__name', 'title', 'edition', 'pub_date', 'isbn')

    @staticmethod
    def excerpt(obj):
        return obj.get_excerpt(20)


admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'state')
    search_fields = ('name', 'description')

    @staticmethod
    def excerpt(obj):
        return obj.get_excerpt(20)


admin.site.register(Category, CategoryAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'admission_number', 'date_of_birth', 'state')
    search_fields = ('first_name', 'last_name', 'admission_number', 'date_of_birth', 'state__name')

    @staticmethod
    def excerpt(obj):
        return obj.get_excerpt(20)


admin.site.register(Member, MemberAdmin)


class LibraryRecordAdmin(admin.ModelAdmin):
    list_display = ('member', 'returned', 'book', 'expected_return_date', 'return_date')
    search_fields = (
        'member__first_name', 'member__last_name', 'returned', 'book__title', 'expected_return_date',
        'return_date')

    @staticmethod
    def excerpt(obj):
        return obj.get_excerpt(20)


admin.site.register(LibraryRecord, LibraryRecordAdmin)
