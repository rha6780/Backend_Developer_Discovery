from django.test import TestCase
from core.factories.posts import PostFactory


class CommentModelTestCase(TestCase):
    def test_user_is_null_posts_user_set_null(self):
        post = PostFactory()

        post.user.delete()

        post.refresh_from_db()
        self.assertEqual(post.user, None)
