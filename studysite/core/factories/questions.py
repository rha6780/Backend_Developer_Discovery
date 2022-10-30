import factory

from .questions import QuestionFactory


class QuestionFactory(factory.django.DjangoModelFactory):
    id = factory.sequence(lambda n: n + 1)
    question = factory.SubFactory(QuestionFactory)
    content = factory.Faker("sentence")

    class Meta:
        model = "questions.Answer"
        django_get_or_create = ("id",)

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        created_at = kwargs.pop("created_at", None)
        obj = super()._create(target_class, *args, **kwargs)
        if created_at is not None:
            obj.created_at = created_at
            obj.save()
        return obj