from django.test import TestCase

from ..models import Video
from .factories import VideoFactory


class VideoModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.title = "test"
