import factory
from faker import Factory as FakerFactory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .. models import Post

faker = FakerFactory.create()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    body = factory.LazyAttribute(lambda x: faker.text())

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('admin'))  # all superusers have admin as password
    is_staff = True
    is_superuser = True

