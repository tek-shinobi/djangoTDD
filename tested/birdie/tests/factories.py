import factory
from faker import Factory as FakerFactory

from .. models import Post

faker = FakerFactory.create()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    body = factory.LazyAttribute(lambda x: faker.text())

