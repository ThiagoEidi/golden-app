import factory
from faker import Faker

from app.models import User

faker = Faker()


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: faker.user_name())
    email = factory.LazyAttribute(lambda _: faker.email())
    senha = factory.LazyAttribute(lambda _: faker.password())
