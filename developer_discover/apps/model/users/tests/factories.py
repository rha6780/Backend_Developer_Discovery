from faker import Faker
import factory

from django.contrib.auth import get_user_model

fake = Faker("ko_KR")

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(fake.name)
    email = factory.Faker("email")

    class Meta:
        model = User
        django_get_or_create = ("email",)
