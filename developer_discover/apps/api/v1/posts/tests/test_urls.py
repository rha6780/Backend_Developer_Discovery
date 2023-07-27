from django.test.testcases import TestCase
from django.urls import reverse, resolve

from .. import views


class PostUrlsTestCase(TestCase):
    def test_post_list_is_resolved(self):
        url = reverse("posts:list")
        self.assertEquals(resolve(url).func.view_class, views.PostListView)

    def test_post_create_is_resolved(self):
        url = reverse("posts:create")
        self.assertEquals(resolve(url).func.view_class, views.PostCreateView)

    def test_post_view_is_resolved(self):
        url = reverse("posts:action", kwargs={"pk": 1})
        self.assertEquals(resolve(url).func.view_class, views.PostView)

    def test_post_like_is_resolved(self):
        url = reverse("posts:like", kwargs={"pk": 1})
        self.assertEquals(resolve(url).func.view_class, views.PostLikeView)
