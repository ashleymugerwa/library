from mueni.backend.services import MemberService, BookService, LibraryRecordService, StateService


class Processors(object):
    @staticmethod
    def register_member(payload):
        first_name = payload.get('first_name')
        last_name = payload.get('last_name')
        admission_date = payload.get('admission_date')
        date_of_birth = payload.get('date_of_birth')
        if first_name != '' and last_name != '' and admission_date != '' and date_of_birth != '':
            state = StateService().get_state(name='Active')
            member = MemberService().create_member(
                first_name=first_name,
                last_name=last_name,
                admission_number=admission_date,
                date_of_birth=date_of_birth,
                state=state
            )
            if member is not None:
                return 'success'
            return 'failed'

    @staticmethod
    def deactivate_member(member_id):
        member = MemberService().get_member(id=member_id)
        if member is not None:
            state = StateService().get_state(name='Disabled')
            deactivate = MemberService().update_member(
                member.id, state=state
            )
            if deactivate is not None:
                return 'success'
        return 'failed'

    @staticmethod
    def return_book(book_id):
        book = BookService().get_book(id=book_id)
        if book is not None:
            state = StateService().get_state(name='Available')
            result = BookService().update_book(
               book.id, state=state
            )
            if result is not None:
                return 'success'
        return 'failed'

    @staticmethod
    def add_book(payload):
        author = payload.get('author')
        category = payload.get('category')
        title = payload.get('title')
        edition = payload.get('edition')
        isbn = payload.get('isbn')
        if author != '' and category != '' and title != '' and edition != '' and isbn != '':
            state = StateService().get_state(name='Available')
            book = BookService().create_book(
                author=author,
                category=category,
                title=title,
                edition=edition,
                isbn=isbn,
                state=state
            )
            if book is not None:
                return 'success'
        return 'failed'

    @staticmethod
    def borrow_book(payload):
        member_id = payload.get('member_id')
        returned = payload.get(False)
        book_id = payload.get('book_id')
        expected_return_date = payload.get('expected_return_date')
        if member_id != '' and returned != '' and expected_return_date != '' and book_id != '':
            state = StateService().get_state(name='Uncleared')
            library_record = LibraryRecordService().create_library_record(
                member_id=member_id,
                returned=returned,
                book_id=book_id,
                expeced_return_date=expected_return_date,
                state=state
            )
            if library_record is not None:
                return 'success'
        return 'failed'

    @staticmethod
    def remove_book(book_id):
        book = BookService().get_book(id=book_id)
        if book is not None:
            state = StateService().get_state(name='Unavailable')
            result = BookService().update_book(
                book.id, state=state
            )
            if result is not None:
                return 'success'
        return 'failed'

