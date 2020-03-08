import pytest
import factory.fuzzy

from pytest_factoryboy import register

from .factories import (
    PostFactory,
    UserFactory,
)

register(PostFactory)
register(UserFactory)

@pytest.fixture()
def post(post_factory):
    return post_factory()

@pytest.fixture()
def user(user_factory):
    return user_factory()

@pytest.fixture()
def post_form_short_text():
    return {'body': factory.fuzzy.FuzzyText(length=5).fuzz()}

@pytest.fixture()
def post_form_long_text():
    return {'body': factory.fuzzy.FuzzyText(length=50).fuzz()}
