import datetime
import factory
from .users import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    """
    Notes:
        유저가 작성한 작성물에 대한 Test 코드용 Factory 입니다.
    """

    id = factory.sequence(lambda x: x + 1)
    title = factory.Faker("sentence")
    content = factory.Faker("sentence")
    user = factory.SubFactory(UserFactory)
    thumbnail = factory.django.ImageField(filename="example.jpg")
    created_at = datetime.datetime.now
    updated_at = datetime.datetime.now

    class Meta:
        model = "posts.Post"
        django_get_or_create = ("id",)
