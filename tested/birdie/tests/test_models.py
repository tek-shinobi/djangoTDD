import pytest

# pytestmark = pytest.mark.django_db

from .. models import Post
# @pytest.mark.django_db
# def test_creation(post_factory):
#     post_created = post_factory()
#     assert post_created.id == 1, 'Should be 1'

class TestPost:
    pytestmark = pytest.mark.django_db
    def test_creation(self, post_factory):
        post_created = post_factory()
        post = Post.objects.get(id = post_created.id)
        print(f'body:{post.body}')
        assert post.id == 1, 'Should be 1'