from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from core.factories.users import UserFactory
from core.factories.posts import PostFactory
from core.factories.comments import CommentFactory
from apps.model.comments.models import Comment


class CommentListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.post = PostFactory()
        cls.url = reverse("posts:comments:list", kwargs={"post_id": cls.post.id})

    def test_post_of_comment_list(self):
        comments = CommentFactory.create_batch(10, post=self.post)

        res = self.client.get(self.url)

        results = res.data["results"]
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        for i in range(10):
            self.assertEqual(results[i]["id"], comments[i].id)
            self.assertEqual(results[i]["content"], comments[i].content)
            self.assertEqual(results[i]["author"], {"id": comments[i].user_id, "name": comments[i].user.name})
            self.assertEqual(results[i]["created_at"], comments[i].created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            self.assertEqual(results[i]["updated_at"], comments[i].updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

    def test_comment_not_include_in_post(self):
        comment = CommentFactory()

        res = self.client.get(self.url)

        result = res.data["results"]
        self.assertEqual(result, [])
        self.assertNotEqual(comment.post_id, self.post.id)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class CommentViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = PostFactory()

    def test_valid_content_create(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        user = UserFactory()
        url = reverse("posts:comments:create", kwargs={"post_id": self.post.id})
        request = request_factory.post(url, {"content": "test-content"}, format="json")
        refresh = RefreshToken.for_user(user)

        before_count = Comment.objects.count()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.post(url, {"content": "test-content"}, format="json")
        after_count = Comment.objects.count()
        force_authenticate(request, user=user)

        self.assertEqual(after_count, before_count + 1)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_invalid_content_not_created(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        user = UserFactory()
        url = reverse("posts:comments:create", kwargs={"post_id": self.post.id})
        request = request_factory.post(url, {"content": ""}, format="json")
        refresh = RefreshToken.for_user(user)

        before_count = Comment.objects.count()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.post(url, {"content": ""}, format="json")
        after_count = Comment.objects.count()
        force_authenticate(request, user=user)

        self.assertEqual(after_count, before_count)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_data(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        user = UserFactory()
        comment = CommentFactory(content="test-1234", user=user)
        url = reverse("posts:comments:action", kwargs={"post_id": self.post.id, "pk": comment.id})
        request = request_factory.patch(url, {"content": "test 1234"}, format="json")
        refresh = RefreshToken.for_user(user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.patch(url, {"content": "test 1234"}, format="json")
        force_authenticate(request, user=user)
        comment.refresh_from_db()

        self.assertEqual(comment.content, "test 1234")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_invalid_data(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        user = UserFactory()
        comment = CommentFactory(content="", user=user)
        url = reverse("posts:comments:action", kwargs={"post_id": self.post.id, "pk": comment.id})
        request = request_factory.patch(url, {"content": "test 1234"}, format="json")
        refresh = RefreshToken.for_user(user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.patch(url, {"content": ""}, format="json")
        force_authenticate(request, user=user)
        comment.refresh_from_db()

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_comment(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        user = UserFactory()
        comment = CommentFactory(user=user)
        url = reverse("posts:comments:action", kwargs={"post_id": self.post.id, "pk": comment.id})
        request = request_factory.delete(url, format="json")
        refresh = RefreshToken.for_user(user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.delete(url, format="json")
        force_authenticate(request, user=user)
        comment.refresh_from_db()

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
