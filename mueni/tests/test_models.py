from __future__ import unicode_literals
import pytest

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


# Trivia : Try to test for the return
class TestState(object):
    def test_state_model(self):
        obj = mixer.blend('mueni.State', name='Kelvin')
        assert obj is not None, 'should return Kelvin'
        assert obj.name == "Kelvin", 'should be the one'


class TestAuthor(object):
    def test_authors_model(self):
        obj = mixer.blend('mueni.Author', name='Shaniqwa')
        assert obj is not None, 'should return name'
        assert obj.title == "Shaniqwa", 'Should be the one '


class TestBook(object):
    def test_book_model(self):
        obj = mixer.blend('mueni.Book', title="My Book")
        assert obj is not None, 'should return name'
        assert obj.title == "My Book", 'Should have field name title'


class TestCategory(object):
    def test_category_model(self):
        obj = mixer.blend('mueni.Category', name="math")
        assert obj is not None, 'should return math'
        assert obj.name == "math", 'should be the one'


class TestMember(object):
    def test_member_model(self):
        obj = mixer.blend('mueni.Member', first_name="Ashley")
        assert obj is not None, 'should return first_name'
        assert obj.first_name == "Ashley", 'should be correct'


class TestLibraryRecord(object):
    def test_library_record_model(self):
        import datetime
        obj = mixer.blend('mueni.LibraryRecord', return_date=datetime.datetime.now())
        assert obj is not None, 'should return returned'
        assert obj.return_date == obj.return_date, 'should be the one'
