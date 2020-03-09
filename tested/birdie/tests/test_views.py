import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from .. import views
from .. import models

class TestHomeView:
    def test_anonymous(self):
        '''HomeView should be accessable by anyone.'''
        req = RequestFactory().get('/')
        resp = views.HomeView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'


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

    pytestmark = pytest.mark.django_db
    def test_superuser(self, user_factory):
       '''check that authenticated user is able to access the view by getting 200 as response status code'''
       user = user_factory()
       req = RequestFactory().get('/')
       req.user = user  # manually attach the user variable to the request
       resp = views.AdminView.as_view()(req)
       assert resp.status_code == 200, 'Should be callable by the superuser'


class TestPostUpdateView:
    """So, the view needs to be callable, i.e. it must support a get request so we can get the form
    Then the view must also support a POST request so we can do an update"""
    pytestmark = pytest.mark.django_db
    def test_get(self, post_factory):
        ''' testing get request for the form'''
        # the way update view works is that to get the form, you need to provide the primary key
        # so lets create the post first. This is the post that we will update through the form
        post_created = post_factory()
        req = RequestFactory().get('/')
        # this is how you pass kwargs to a RequestFactory object
        resp = views.PostUpdateView.as_view()(req, pk=post_created.pk)
        assert resp.status_code == 200, 'Should be callable by anyone'

    pytestmark = pytest.mark.django_db
    def test_post(self, post_factory, post_form_message):
        post_created = post_factory()
        data = post_form_message
        req = RequestFactory().post('/', data=data)
        resp = views.PostUpdateView.as_view()(req, pk=post_created.pk)
        # django update views by design redirect you to a success url is POST was successful
        assert resp.status_code == 302, 'Should redirect to success view'

        #modified_post = models.Post.objects.filter(pk=post_created.pk)
        post_created.refresh_from_db()
        assert post_created.body == post_form_message.get('body', object())  # object() isn't equal to anything else
