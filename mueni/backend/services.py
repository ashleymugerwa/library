from mueni.models import Author, Category, Book, Member, LibraryRecord, State
import logging
lgr = logging.getLogger(__name__)


class StateService(object):
    """
    get(*args, **kwargs)
    create(**kwargs)
    filter(*args, **kwargs)
    update(key, **kwargs)
    """
    @staticmethod
    def filter_state(*args, **kwargs):
        """
        filter method for state model
        :param args:
        :param kwargs:
        :return:
        """
        try:
            record = State.objects.filter(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("State.filter error: ", e)
            return None

    @staticmethod
    def get_state(*args, **kwargs):
        try:
            record = State.objects.get(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("State.get.error: ", e)
            return None

    @staticmethod
    def create_state(**kwargs):
        try:
            record = State.objects.create(**kwargs)
            return record
        except Exception as e:
            lgr.error("State.create.error: ", e)
            return None

    def update_state(self, key, **kwargs):
        try:
            record = self.get_state(id=key)
            if record is not None:
                for attr, val in kwargs.items():
                    setattr(record, attr, val)
                record.save()
                record.refresh_from_db()
                return record
            return None
        except Exception as e:
            lgr.error("State.update.error: ", e)
            return None


class AuthorService(object):
    """
    get(*args, **kwargs)
    create(**kwargs)
    filter(*args, **kwargs)
    update(key, **kwargs)
    """
    @staticmethod
    def filter_author(*args, **kwargs):
        """
        filter method for author model
        :param args:
        :param kwargs:
        :return:
        """
        try:
            record = Author.objects.filter(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Author.filter error: ", e)
            return None

    @staticmethod
    def get_author(*args, **kwargs):
        try:
            record = Author.objects.get(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Author.get.error: ", e)
            return None

    @staticmethod
    def create_author(**kwargs):
        try:
            record = Author.objects.create(**kwargs)
            return record
        except Exception as e:
            lgr.error("Author.create.error: ", e)
            return None

    def update_author(self, key, **kwargs):
        try:
            record = self.get_author(id=key)
            if record is not None:
                for attr, val in kwargs.items():
                    setattr(record, attr, val)
                record.save()
                record.refresh_from_db()
                return record
            return None
        except Exception as e:
            lgr.error("Author.update.error: ", e)
            return None


class CategoryService(object):
    """
    get(*args, **kwargs)
    create(**kwargs)
    filter(*args, **kwargs)
    update(key, **kwargs)
    """
    @staticmethod
    def filter_category(*args, **kwargs):
        """
        filter method for category model
        :param args:
        :param kwargs:
        :return:
        """
        try:
            record = Category.objects.filter(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Category.filter error: ", e)
            return None

    @staticmethod
    def get_category(*args, **kwargs):
        try:
            record = Category.objects.get(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Category.get.error: ", e)
            return None

    @staticmethod
    def create_category(**kwargs):
        try:
            record = Category.objects.create(**kwargs)
            return record
        except Exception as e:
            lgr.error("Category.create.error: ", e)
            return None

    def update_category(self, key, **kwargs):
        try:
            record = self.get_category(id=key)
            if record is not None:
                for attr, val in kwargs.items():
                    setattr(record, attr, val)
                record.save()
                record.refresh_from_db()
                return record
            return None
        except Exception as e:
            lgr.error("Category.update.error: ", e)
            return None


class BookService(object):
    """
    get(*args, **kwargs)
    create(**kwargs)
    filter(*args, **kwargs)
    update(key, **kwargs)
    """
    @staticmethod
    def filter_book(*args, **kwargs):
        """
        filter method for book model
        :param args:
        :param kwargs:
        :return:
        """
        try:
            record = Book.objects.filter(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Book.filter error: ", e)
            return None

    @staticmethod
    def get_book(*args, **kwargs):
        try:
            record = Book.objects.get(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Book.get.error: ", e)
            return None

    @staticmethod
    def create_book(**kwargs):
        try:
            record = Book.objects.create(**kwargs)
            return record
        except Exception as e:
            lgr.error("Book.create.error: ", e)
            return None

    def update_book(self, key, **kwargs):
        try:
            record = self.get_book(id=key)
            if record is not None:
                for attr, val in kwargs.items():
                    setattr(record, attr, val)
                record.save()
                record.refresh_from_db()
                return record
            return None
        except Exception as e:
            lgr.error("Book.update.error: ", e)
            return None


class MemberService(object):
    """
    get(*args, **kwargs)
    create(**kwargs)
    filter(*args, **kwargs)
    update(key, **kwargs)
    """
    @staticmethod
    def filter_member(*args, **kwargs):
        """
        filter method for member model
        :param args:
        :param kwargs:
        :return:
        """
        try:
            record = Member.objects.filter(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Member.filter error: ", e)
            return None

    @staticmethod
    def get_member(*args, **kwargs):
        try:
            record = Member.objects.get(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Member.get.error: ", e)
            return None

    @staticmethod
    def create_member(**kwargs):
        try:
            record = Member.objects.create(**kwargs)
            return record
        except Exception as e:
            lgr.error("Member.create.error: ", e)
            return None

    def update_member(self, key, **kwargs):
        try:
            record = self.get_member(id=key)
            if record is not None:
                for attr, val in kwargs.items():
                    setattr(record, attr, val)
                record.save()
                record.refresh_from_db()
                return record
            return None
        except Exception as e:
            lgr.error("Member.update.error: ", e)
            return None


class LibraryRecordService(object):
    """
    get(*args, **kwargs)
    create(**kwargs)
    filter(*args, **kwargs)
    update(key, **kwargs)
    """
    @staticmethod
    def filter_library_record(*args, **kwargs):
        """
        filter method for library_record model
        :param args:
        :param kwargs:
        :return:
        """
        try:
            record = LibraryRecord.objects.filter(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("library_record.filter error: ", e)
            return None

    @staticmethod
    def get_library_record(*args, **kwargs):
        try:
            record = LibraryRecord.objects.get(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("library_record.get.error: ", e)
            return None

    @staticmethod
    def create_library_record(**kwargs):
        try:
            record = LibraryRecord.objects.create(**kwargs)
            return record
        except Exception as e:
            lgr.error("library_record.create.error: ", e)
            return None

    def update_library_record(self, key, **kwargs):
        try:
            record = self.get_library_record(id=key)
            if record is not None:
                for attr, val in kwargs.items():
                    setattr(record, attr, val)
                record.save()
                record.refresh_from_db()
                return record
            return None
        except Exception as e:
            lgr.error("library_record.update.error: ", e)
            return None
