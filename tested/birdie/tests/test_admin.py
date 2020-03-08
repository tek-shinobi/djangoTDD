import pytest
from django.contrib.admin.sites import AdminSite

from ..models import Post
from .. import admin

pytestmark = pytest.mark.django_db

class TestPostAdmin:
    def test_excerpt(self, post_factory):
        post_created = post_factory()
        admin_site = AdminSite()
        post_admin = admin.PostAdmin(model=Post, admin_site=admin_site)
        result = post_admin.excerpt(post_created)
        assert result == post_created.body[:5], 'Should return first five letters'
