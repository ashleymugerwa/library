import pytest
import datetime

from mueni.processors import Processors
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestProcessors(object):
    def test_register_member(self):
        payload = {
            'first_name': 'Shish',
            'last_name': 'Makena',
            'admission_number': 'Twelve',
            'date_of_birth': datetime.datetime.now().date()
        }
        result = Processors.register_member(payload)
        assert result is not None

    def test_add_book(self):
        author = mixer.blend('mueni.Author', name='Lucas Podowlski')
        category = mixer.blend('mueni.Category', name='Mystery')
        payload = {
            'author': author,
            'category': category,
            'title': 'Ashley In L.A',
            'edition': 'Third',
            'isbn': 'HGFF34'
        }
        result = Processors.add_book(payload)
        assert result is not None

    def test_borrow_book(self):
        member = mixer.blend('mueni.Member', name='Lucas Podowlski')
        book = mixer.blend('mueni.Book', name='Luis')
        payload = {
            'member': member,
            'book': book,
            'returned': False,
            'expected_return_date': None,
            'return_date': None
        }
        result = Processors.borrow_book(payload)
        assert result is not None

    def test_remove_book(self):
        member = mixer.blend('mueni.Member', name='Lucas Podowlski')
        book = mixer.blend('mueni.Book', name='Luis')
        payload = {
            'member': member,
            'book': book,
            'returned': 'False',
            'expected_return_date': datetime.datetime.now().date(),
            'return_date': datetime.datetime.now().date()
        }
        result = Processors.remove_book(book_id=payload)
        assert result is not None

    def test_return_book(self):
        author = mixer.blend('mueni.Author', name='Lucas Podowlski')
        category = mixer.blend('mueni.Category', name='Luis')
        payload = {
            'author': author,
            'category': category,
            'title': 'Ashley In L.A',
            'edition': 'Third',
            'isbn': 'HGFF34'
        }
        result = Processors.return_book(book_id=payload)
        assert result is not None

    def test_deactivate_member(self):
        payload = {
             'first_name': 'Shish',
             'last_name': 'Makena',
             'admission_number': 'Twelve',
             'date_of_birth': datetime.datetime.now().date()
        }
        result = Processors.deactivate_member(member_id=payload)
        assert result is not None