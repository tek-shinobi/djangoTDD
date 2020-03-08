import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from .. import views
class TestHomeView:
    def test_anonymous(self):
        '''HomeView should be accessable by anyone.'''
        req = RequestFactory().get('/')
        resp = views.HomeView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'

pytestmark = pytest.mark.django_db
class TestAdminView:
    def test_anonymous(self):
        '''check that anonymous user gets redirected to login oage'''
        req = RequestFactory().get('/')
        req.user = AnonymousUser()  # manually attach AnonymousUser
        resp = views.AdminView.as_view()(req)
        # for checking, I can directly check the status_code as 302 but this is not good as the redirect might
        # also happen due to some actual logic in the view.
        # Better way: I know that a view protected by login_required decorator redirects to '/accounts/login/?next='
        # (default value of redirect). So I check if the word 'login' is present in resp.url
        assert 'login' in resp.url

    def test_superuser(self, user_factory):
       '''check that authenticated user is able to access the view by getting 200 as response status code'''
       user = user_factory()
       req = RequestFactory().get('/')
       req.user = user  # manually attach the user variable to the request
       resp = views.AdminView.as_view()(req)
       assert resp.status_code == 200, 'Should be callable by the superuser'