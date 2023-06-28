import datetime
import factory
from .users import UserFactory
from .posts import PostFactory


class CommentFactory(factory.django.DjangoModelFactory):
    """
    Notes:
        유저가 작성한 댓글에 대한 Test 코드용 Factory 입니다.
    """

    id = factory.sequence(lambda x: x + 1)
    content = factory.Faker("sentence")
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    created_at = datetime.datetime.now
    updated_at = datetime.datetime.now

    class Meta:
        model = "comments.Comment"
        django_get_or_create = ("id",)
