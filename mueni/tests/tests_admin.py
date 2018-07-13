import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer

from mueni import admin, models

pytestmark = pytest.mark.django_db


class TestStateAdmin(object):
    def test_state(self):
        site = AdminSite()
        state_admin = admin.StateAdmin(models.State, site)

        obj = mixer.blend('mueni.State', name='Active')
        result = state_admin.excerpt(obj)
        expected = obj.get_excerpt(20)
        assert result == expected


class TestAuthorAdmin(object):
    def test_author(self):
        site = AdminSite()
        author_admin = admin.AuthorAdmin(models.Author, site)

        obj = mixer.blend('mueni.Author', name='Ashley')
        result = author_admin.excerpt(obj)
        expected = obj.get_excerpt(20)
        assert result == expected, 'should return an instance'


class TestBookAdmin(object):
    def test_book(self):
        site = AdminSite()
        book_admin = admin.BookAdmin(models.Book, site)

        obj = mixer.blend('mueni.Book', title='Beyond Limits')
        result = book_admin.excerpt(obj)
        expected = obj.get_excerpt(20)
        assert result == expected, 'Should return an instance'


class TestCategoryAdmin(object):
    def test_category(self):
        site = AdminSite()
        category_admin = admin.CategoryAdmin(models.Category,  site)

        obj = mixer.blend('mueni.Category', name='math')
        result = category_admin.excerpt(obj)
        expected = obj.get_excerpt(20)
        assert result == expected, (
            'should return the result')


class TestMemberAdmin(object):
    def test_member(self):
        site = AdminSite()
        member_admin = admin.MemberAdmin(models.Member,  site)

        obj = mixer.blend('mueni.Member', first_name='Maggie')
        result = member_admin.excerpt(obj)
        expected = obj.get_excerpt(20)
        assert result == expected,   (
            'should return the result')


class TestLibraryRecordAdmin(object):
    def test_library_record(self):
        site = AdminSite()
        library_record_admin = admin.LibraryRecordAdmin(models.LibraryRecord,  site)

        obj = mixer.blend('mueni.LibraryRecord', gender='Female')
        result = library_record_admin.excerpt(obj)
        expected = obj.get_excerpt(20)
        assert result == expected,   (
            'should return the result')
