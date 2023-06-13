import factory


# get_or_create : https://stackoverflow.com/questions/17206677/why-does-factoryboy-create-a-new-object-from-subfactory-despite-factory-django-g
class UserFactory(factory.django.DjangoModelFactory):
    """
    Notes:
        유저 정보에 대한 Test 코드용 Factory 입니다.
    """

    email = factory.sequence(lambda x: f"test{x}@example.com")
    name = factory.sequence(lambda x: f"test{x}")
    password = "test_1234_test"

    class Meta:
        model = "users.User"
        django_get_or_create = ("email",)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager._create_user(*args, **kwargs)
