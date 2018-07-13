import datetime

import pytest
from mixer.backend.django import mixer

from mueni.backend.services import AuthorService, CategoryService, BookService, MemberService, LibraryRecordService, \
    StateService


pytestmark = pytest.mark.django_db


class TestStateService(object):
    def test_filter_state(self):
        obj = mixer.cycle(2).blend('mueni.State', name='Fredrick Hernandez', description='suspended')
        result = StateService().filter_state(name='Fredrick Hernandez')
        assert len(result) == len(obj), 'Should return two records with name Fredrick Hernandez'

    def test_get_state(self):
        obj = mixer.blend('mueni.State', name='Ashley', description='suspended')
        result = StateService().get_state(description=obj.description)
        assert result is not None

    def test_create_state(self):
        payload = {
            'name': 'Fredrick Hernandez',
            'description': 'suspended'
        }
        result = StateService().create_state(**payload)
        assert result is not None

    def test_update_state(self):
        obj = mixer.blend('mueni.State', name='Ashley', description='suspended')
        result = StateService().update_state(obj.id, name='Smith')
        assert result is not None, 'should change Ashley into Smith'


class TestAuthorService(object):
    def test_filter_author(self):
        obj = mixer.cycle(2).blend('mueni.Author', name='Fredrick Hernandez', number_of_books=50, awards=21)
        result = AuthorService().filter_author(name='Fredrick Hernandez')
        assert len(result) == len(obj), 'Should return two records with name Fredrick Hernandez'

    def test_get_author(self):
        obj = mixer.blend('mueni.Author', name='Ashley', number_of_books=30, awards=29)
        result = AuthorService().get_author(number_of_books=obj.number_of_books)
        assert result is not None

    def test_create_author(self):
        payload = {
            'name': 'Fredrick Hernandez',
            'number_of_books': 23,
            'awards': 12
        }
        result = AuthorService().create_author(**payload)
        assert result is not None

    def test_update_author(self):
        obj = mixer.blend('mueni.Author', name='Ashley', number_of_books=30, awards=29)
        result = AuthorService().update_author(obj.id, number_of_books=45)
        assert result is not None, 'should change 30 into 45'


class TestCategoryService(object):
    def test_filter_category(self):
        obj = mixer.cycle(2).blend('mueni.Category', name='Fredrick Hernandez', description='math')
        result = CategoryService().filter_category(name='Fredrick Hernandez')
        assert len(result) == len(obj), 'Should return two records with name Fredrick Hernandez'

    def test_get_category(self):
        obj = mixer.blend('mueni.Category', name='Ashley', description='math')
        result = CategoryService().get_category(description=obj.description)
        assert result is not None

    def test_create_category(self):
        mpay = {
            'name': 'Ashley',
            'description': 'math'
        }
        result = CategoryService().create_category(**mpay)
        assert result is not None

    def test_update_category(self):
        obj = mixer.blend('mueni.Category', name='Ashley', description='math')
        result = CategoryService().update_category(obj.id, description='horror')
        assert result is not None,  'should  change math into horror'


class TestBookService(object):
    def test_filter_book(self):
        author = mixer.blend('mueni.Author', name='Lucas Podowlski')
        category = mixer.blend('mueni.Category', name='Luis')
        obj = mixer.cycle(2).blend('mueni.Book', author=author, category=category, edition='Third')
        result = BookService().filter_book(edition='Third')
        assert len(result) == len(obj), 'Should return two records with edition Third'

    def test_get_book(self):
        author = mixer.blend('mueni.Author', name='Lucas Podowlski')
        category = mixer.blend('mueni.Category', name='Luis')
        obj = mixer.blend('mueni.Book', author=author, category=category, edition='Third')
        result = BookService().get_book(edition=obj.edition)
        assert result is not None

    def test_create_book(self):
        author = mixer.blend('mueni.Author', name='Lucas Podowlski')
        category = mixer.blend('mueni.Category', name='Luis')
        mpay = {
            'author': author,
            'category': category,
            'edition': 'Third',
            'title': 'Alice In Wonderland',
            'pub_date': datetime.datetime.now(),
            'isbn': 'sewqf3r2'
        }
        result = BookService().create_book(**mpay)
        assert result is not None

    def test_update_book(self):
        author = mixer.blend('mueni.Author', name='Lucas Podowlski')
        category = mixer.blend('mueni.Category', name='Luis')
        obj = mixer.blend('mueni.Book', author=author, category=category, edition='Third')
        result = BookService().update_book(obj.id, edition='Fourth')
        assert result is not None, 'should change Third into Fourth'


class TestMemberService(object):
    def test_filter_member(self):
        obj = mixer.cycle(2).blend('mueni.Member', first_name='Fredrick', last_name='Mueni')
        result = MemberService().filter_member(first_name='Fredrick')
        assert len(result) == len(obj), 'Should return two records with Fredrick'

    def test_get_member(self):
        obj = mixer.blend('mueni.Member', first_name='Fredrick', last_name='Mueni')
        result = MemberService().get_member(first_name=obj.first_name)
        assert result is not None

    def test_create_member(self):
        state = mixer.blend('mueni.State', name='Lucas Podowlski')
        mpay = {
            'state': state,
            'first_name': 'Fredrick',
            'last_name': 'Mueni',
            'admission_number': 'Twenty one',
            'date_of_birth': datetime.datetime.now()

        }
        result = MemberService().create_member(**mpay)
        assert result is not None

    def test_update_member(self):
        obj = mixer.blend('mueni.Member', first_name='Fredrick', last_name='Mueni',)
        result = MemberService().update_member(obj.id, first_name='riri')
        assert result is not None


class TestLibraryRecordService(object):
    def test_filter_library_record(self):
        member = mixer.blend('mueni.Member', first_name='Lucas')
        book = mixer.blend('mueni.Book', title='Alice')
        obj = mixer.cycle(2).blend('mueni.LibraryRecord',  member=member,  book=book)
        result = LibraryRecordService().filter_library_record(member=member)
        assert len(result) == len(obj), 'Should return two records with member'

    def test_get_library_record(self):
        member = mixer.blend('mueni.Member', first_name='Lucas')
        book = mixer.blend('mueni.Book', title='Alice')
        obj = mixer.blend('mueni.LibraryRecord', member=member, book=book)
        result = LibraryRecordService().get_library_record(member=obj.member)
        assert result is not None

    def test_create_library_record(self):
        member = mixer.blend('mueni.Member', first_name='Lucas')
        book = mixer.blend('mueni.Book', title='Alice')
        data = {
            'member': member,
            'book': book,
            'returned': True,
            'expected_return_date': datetime.datetime.now(),
            'return_date': datetime.datetime.now()
        }
        result = LibraryRecordService().create_library_record(**data)
        assert result is not None

    def test_update_library_record(self):
        member = mixer.blend('mueni.Member', first_name='Lucas')
        book = mixer.blend('mueni.Book', title='Alice In Kisumu')
        obj = mixer.blend('mueni.LibraryRecord', member=member, book=book)
        result = LibraryRecordService().update_library_record(obj.id, book__title='Sang In Nai')
        assert result is not None
