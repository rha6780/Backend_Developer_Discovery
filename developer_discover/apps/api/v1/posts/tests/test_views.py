import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from core.factories.posts import PostFactory

from .....model.posts.models import Post


class PostListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.url = reverse("posts-list")

    def test_post_data_is_not_exist(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["count"], 0)
        self.assertEqual(res.data["results"], [])

    def test_post_data_is_exist(self):
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

    def test_post_data_with_many_data(self):
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
