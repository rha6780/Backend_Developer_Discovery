from django.test import TestCase
from core.factories.posts import PostFactory
from core.factories.comments import CommentFactory


class CommentModelTestCase(TestCase):
    def test_user_is_null_comments_user_set_null(self):
        post = PostFactory()
        comment = CommentFactory(post=post, user=post.user)

        post.user.delete()

        post.refresh_from_db()
        comment.refresh_from_db()
        self.assertEqual(comment.user, None)

    def test_post_is_deleted_comments_cascade(self):
        comment = CommentFactory()

        comment.post.delete()

        comment.post.refresh_from_db()
        comment.refresh_from_db()
        self.assertNotEqual(comment.deleted_at, None)
