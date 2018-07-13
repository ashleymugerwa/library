import datetime

import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from.. import views


class TestCashDigitalView(object):
    """
    This is a class for testing views
    """
    def set_up(self):
        # every test needs to access the request factory
        self.factory = RequestFactory()

    def test_add_book(self):
        # create an instance of a Post request
        state = mixer.blend('mueni.State', name='Available')
        author = mixer.blend('mueni.Author', name='Lucas Podowlski', state=state)
        category = mixer.blend('mueni.Category', description='Mystery')
        payload = {
            'author': author,
            'category': category,
            'title': 'Ashley In L.A',
            'edition': 'Third',
            'isbn': 'HGFF34'
        }
        import json
        payload = json.dumps(payload)
        request = self.factory.post('/mueni/add_book/', data=payload)
        response = views.CashDigital.add_book(request)
        assert response.status_code == 200

    def test_register_member(self):
        # create an instance of a Post request
        state = mixer.blend('mueni.state', name='Available')
        payload = {
            'first_name': 'Shish',
            'last_name': 'Makena',
            'admission_number': 'Twelve',
            'date_of_birth': datetime.datetime.now().date()
        }
        request = self.factory.post('mueni/register_member', data=payload)
        response = views.CashDigital.register_member()(request)
        assert response.status_code == 200

    def test_borrow_book(self):
        state = mixer.blend('mueni.state', name='Uncleared')
        member = mixer.blend('mueni.Member', name='Lucas Podowlski', state=state)
        book = mixer.blend('mueni.Book', name='Luis')
        payload = {
            'member': member,
            'book': book,
            'returned': False,
            'expected_return_date': None,
            'return_date': None
        }
        request = self.factory.post('mueni/borrow_book', data=payload)
        response = views.CashDigital.borrow_book()(request)
        assert response.status_code == 200

    def test_remove_book(self):
        # create an instance of a Get request
        request = self.factory.post('mueni/remove_book')
        response = views.CashDigital().remove_book()(request)
        assert response.status_code == 200

    def test_deactivate_member(self):
        # create an instance of a Get request
        request = self.factory.post('mueni/deactivate_member')
        response = views.CashDigital().deactivate_member()(request)
        assert response.status_code == 200

    def test_return_book(self):
        # create an instance of a Get request
        request = self.factory.post('mueni/return_book')
        response = views.CashDigital().return_book()(request)
        assert response.status_code == 200
