import factory
from .users import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    """
    Notes:
        유저가 작성한 작성물에 대한 Test 코드용 Factory 입니다.
    """

    title = factory.Faker("sentence")
    content = factory.Faker("sentence")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = "posts.Post"
        django_get_or_create = ("id",)
