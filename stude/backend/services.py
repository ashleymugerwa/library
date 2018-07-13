from mueni.models import Student
import logging
lgr = logging.getLogger(__name__)


class StudentService(object):
    """
    get(*args, **kwargs)
    create(**kwargs)
    filter(*args, **kwargs)
    update(key, **kwargs)
    """
    @staticmethod
    def filter_student(*args, **kwargs):
        """
        filter method for author model
        :param args:
        :param kwargs:
        :return:
        """
        try:
            record = Student.objects.filter(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Student.filter error: ", e)
            return None

    @staticmethod
    def get_student(*args, **kwargs):
        try:
            record = Student.objects.get(*args, **kwargs)
            return record
        except Exception as e:
            lgr.error("Student.get.error: ", e)
            return None

    @staticmethod
    def create_student(**kwargs):
        try:
            record = Student.objects.create(**kwargs)
            return record
        except Exception as e:
            lgr.error("Student.create.error: ", e)
            return None

    def update_student(self, key, **kwargs):
        try:
            record = self.get_student(id=key)
            if record is not None:
                for attr, val in kwargs.items():
                    setattr(record, attr, val)
                record.save()
                record.refresh_from_db()
                return record
            return None
        except Exception as e:
            lgr.error("Student.update.error: ", e)
            return None


