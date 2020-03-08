import factory
from .. import forms


class TestPostForm:
    def test_form(self, post_form_short_text, post_form_long_text):
        form = forms.PostForm(data={})
        assert form.is_valid() is False, 'Should return False for an empty form'

        form = forms.PostForm(data=post_form_short_text)
        assert form.is_valid() is False, 'Should be invalid if too short'

        form = forms.PostForm(data=post_form_long_text)
        assert form.is_valid() is True, 'Should be valid if long enough'