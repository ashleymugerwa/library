from __future__ import unicode_literals
import pytest

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestModelTwo(object):
    def test_students_model(self):
        obj = mixer.blend('stude.Student')
        assert obj is not None, 'should return name'
        assert obj.__str__() == '%s' % obj.name, "should return the name of the stude"
