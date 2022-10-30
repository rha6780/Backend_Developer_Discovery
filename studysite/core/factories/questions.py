import factory

from django.core.files.base import ContentFile

class QuestionFactory(factory.django.DjangoModelFactory):
    """
    Notes:
        Question은 사용자에게 질문하는 부분에 해당하며, 질문당 다수의 Answer 연결된 구조이다. 카테고리별로 그룹화가 가능하다.
    TODO List:
        * answer 개수에 따라서 answer_count가 변경되는 코드가 필요하다.
    """
    id = factory.sequence(lambda n: n + 1)
    content = factory.Faker("sentence")
    category = ['test']
    image = factory.LazyAttribute(
            lambda _: ContentFile(
                factory.django.ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'example.jpg'
            )
        )
    answer_count = 0

    class Meta:
        model = "Question"
        django_get_or_create = ("id",)

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        created_at = kwargs.pop("created_at", None)
        obj = super()._create(target_class, *args, **kwargs)
        if created_at is not None:
            obj.created_at = created_at
            obj.save()
        return obj