import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from..import admin
from.. import models


class TestStudentAdmin(object):
    def test_excerpt(self):
        site = AdminSite()
        student_admin = admin.StudentAdmin(models.Student,  site)

        obj = mixer.blend('stude.Student', name='Ashley sang')
        result = student_admin.excerpt(obj)
        expected = obj.get_excerpt(50)
        assert result == expected,   (
            'should return the result form excerpt()function')
