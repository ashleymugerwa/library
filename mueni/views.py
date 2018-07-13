from django.views.decorators.csrf import csrf_exempt


from mueni.processors import Processors


class CashDigital(object):
    @csrf_exempt
    def add_book(self, request):

        try:

            payload = {
                'title': request.POST.get('title'),
                'author': request.POST.get('author'),
                'category': request.POST.get('category'),
                'edition': request.POST.get('edition'),
                'isbn': request.POST.get('isbn'),
            }
            book = Processors().add_book(payload)
            if book == 'success':
                return 'Book added successfully'
            else:
                return 'Book not added'
        except Exception as e:
            return 'Exception encountered: %s', e

    @csrf_exempt
    def register_member(self, request):

        try:

            payload = {
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'admission_date': request.POST.get('admission_date'),
                'date_of_birth': request.POST.get('date_of_birth'),
            }
            member = Processors().register_member(payload)
            if member == 'success':
                return 'Member  added'
            else:
                return 'Member not added'
        except Exception as e:
            return 'Exception encountered: %s', e

    @csrf_exempt
    def borrow_book(self, request):

        try:

            payload = {
                'member': request.POST.get('member'),
                'returned': False,
                'book': request.POST.get('book'),
                'expected_return_date': request.POST.get('expected_return_date'),
            }
            library_record = Processors().borrow_book(payload)
            if library_record == 'success':
                return 'Book borrowed'
            else:
                return 'Book not borrowed'
        except Exception as e:
            return 'Exception encountered: %s', e

    @csrf_exempt
    def remove_book(self, request):

        try:
            book_id = request.POST.get('book_id')
            library_record = Processors().remove_book(book_id)
            if library_record == 'success':
                return 'Book removed'
            else:
                return 'Book not removed'
        except Exception as e:
            return 'Exception encountered: %s', e

    @csrf_exempt
    def deactivate_member(self, request):

        try:
            member_id = request.POST.get('member_id')
            library_record = Processors().deactivate_member(member_id)
            if library_record == 'success':
                return 'Member Deactivated'
            else:
                return 'Member Activated'
        except Exception as e:
            return 'Exception encountered: %s', e

    @csrf_exempt
    def return_book(self, request):

        try:
            book_id = request.POST.get('book_id')
            library_record = Processors().return_book(book_id)
            if library_record == 'success':
                return 'Book returned'
            else:
                return 'Book not returned'
        except Exception as e:
            return 'Exception encountered: %s', e
