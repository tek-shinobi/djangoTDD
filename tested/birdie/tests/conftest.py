import pytest
from pytest_factoryboy import register

from .factories import PostFactory

register(PostFactory)

@pytest.fixture()
def post(post_factory):
    return post_factory()

