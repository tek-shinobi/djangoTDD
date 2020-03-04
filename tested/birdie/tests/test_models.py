import pytest

# pytestmark = pytest.mark.django_db

from .. models import Post

pytestmark = pytest.mark.django_db

class TestPost:
    pytestmark = pytest.mark.django_db
    def test_creation(self, post_factory):
        post_created = post_factory()
        post = Post.objects.get(id = post_created.id)
        assert post.id == 1, 'Should be 1'

    def test_get_excerpt(self, post_factory):
        post_created = post_factory()
        post = Post.objects.get(id = post_created.id)
        assert post.get_excerpt(5) == post_created.body[:5], 'Should be first few letters of bodyf'
