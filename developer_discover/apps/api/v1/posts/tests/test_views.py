from imp import reload
import json

from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from core.factories.users import UserFactory

from core.factories.posts import PostFactory

from .....model.posts.models import Post
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class PostListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.url = reverse("list")

    def test_list_api_post_data_is_not_exist(self):
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["count"], 0)
        self.assertEqual(res.data["results"], [])

    def test_list_api_post_data_with_one_data(self):
        post = PostFactory()

        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["count"], 1)
        for x in res.data["results"]:
            self.assertEqual(x["id"], post.id)
            self.assertEqual(x["title"], post.title)
            self.assertEqual(x["content"], post.content)
            self.assertEqual(x["author"], {"id": post.user.id, "name": post.user.name})
            self.assertEqual(x["thumbnail"], f"http://testserver{post.thumbnail.url}")

    def test_list_api_post_data_with_many_data(self):
        PostFactory.create_batch(size=10)

        res = self.client.get(self.url)
        expected_list = Post.objects.all().order_by("-created_at")
        return_list = res.data["results"]

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        for x in range(len(return_list)):
            self.assertEqual(return_list[x]["id"], expected_list[x].id)
            self.assertEqual(return_list[x]["title"], expected_list[x].title)
            self.assertEqual(return_list[x]["content"], expected_list[x].content)
            self.assertEqual(
                return_list[x]["author"], {"id": expected_list[x].user.id, "name": expected_list[x].user.name}
            )
            self.assertEqual(return_list[x]["thumbnail"], f"http://testserver{expected_list[x].thumbnail.url}")


class PostCreateViewTestCase(TestCase):
    def test_create_api_with_user(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        user = UserFactory()
        url = reverse("create")
        request = request_factory.post(url, {"title": "test-title", "content": "test-content"}, format="json")
        refresh = RefreshToken.for_user(user)

        before_count = Post.objects.count()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.post(url, {"title": "test-title", "content": "test-content"}, format="json")
        after_count = Post.objects.count()
        force_authenticate(request, user=user)

        self.assertEqual(after_count, before_count + 1)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_api_with_not_login_user(self):
        client = APIClient()
        url = reverse("create")

        before_count = Post.objects.count()
        res = client.post(url, {"title": "test-title", "content": "test-content"}, format="json")
        after_count = Post.objects.count()

        self.assertEqual(after_count, before_count)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PostViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_detail_api_with_valid_pk(self):
        post = PostFactory()
        url = reverse("post", kwargs={"pk": post.id})

        res = self.client.get(url)

        self.assertEqual(res.data["id"], post.id)
        self.assertEqual(res.data["title"], post.title)
        self.assertEqual(res.data["content"], post.content)
        self.assertEqual(res.data["created_at"], post.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.assertEqual(res.data["updated_at"], post.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.assertEqual(res.data["user"], post.user.id)

    def test_delete_api_with_author(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        post = PostFactory()
        user = post.user
        url = reverse("post", kwargs={"pk": post.id})
        request = request_factory.delete(url)
        refresh = RefreshToken.for_user(user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.delete(url)
        force_authenticate(request, user=user)
        post.refresh_from_db()

        self.assertEqual(post.deleted_at, True)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_api_with_none_author(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        user = UserFactory()
        post = PostFactory()
        url = reverse("post", kwargs={"pk": post.id})
        request = request_factory.delete(url)
        refresh = RefreshToken.for_user(user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.delete(url)
        force_authenticate(request, user=user)
        post.refresh_from_db()

        self.assertEqual(post.deleted_at, False)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_api_with_not_login_user(self):
        client = APIClient()
        post = PostFactory()
        url = reverse("post", kwargs={"pk": post.id})

        res = client.delete(url)
        post.refresh_from_db()

        self.assertEqual(post.deleted_at, False)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_api_with_author(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        post = PostFactory()
        user = post.user
        url = reverse("post", kwargs={"pk": post.id})
        request = request_factory.patch(url)
        refresh = RefreshToken.for_user(user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.patch(url, {"content": "fixed_content"})
        force_authenticate(request, user=user)
        post.refresh_from_db()

        self.assertEqual(post.content, "fixed_content")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_patch_api_with_none_author(self):
        post = PostFactory()
        url = reverse("post", kwargs={"pk": post.id})

        res = self.client.patch(url, {"content": "fixed_content"}, content_type="application/json")
        post.refresh_from_db()

        self.assertNotEqual(post.content, "fixed_content")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_api_with_invalid_data(self):
        request_factory = APIRequestFactory()
        client = APIClient()
        post = PostFactory()
        user = post.user
        invalid_data = {"title": ""}
        url = reverse("post", kwargs={"pk": post.id})
        request = request_factory.patch(url)
        refresh = RefreshToken.for_user(user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        res = client.patch(url, invalid_data)
        force_authenticate(request, user=user)
        post.refresh_from_db()

        self.assertNotEqual(post.title, "")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
