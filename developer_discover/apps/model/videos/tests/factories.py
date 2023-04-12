from faker import Faker
import factory

from ..models import Video

fake = Faker("ko_KR")


class VideoFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("title")

    class Meta:
        model = Video
        django_get_or_create = ("email",)
