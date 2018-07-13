from.. import forms


class TestPostForm:
    def test_form(self):
        form = forms.PostForm(data={})
        assert form.is_valid() is False,   'should be invalid if no data is given'

        form = forms.PostForm(data={'name': 'Hello'})
        assert form.is_valid() is False,   'should be invalid if too short'
        assert 'name' in form.errors,  'should return name field error'

        form = forms.PostForm(data={'name': 'Hello World!!!!!'})
        assert form.is_valid() is True,  'should be valid if long enough'