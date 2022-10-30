from rest_framework import status
from django.test import TestCase
from django.urls import reverse

from core.factories.questions import QuestionFactory

class QuestionListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.LIST_SIZE = 10
        QuestionFactory.create_batch(cls.LIST_SIZE)

    def tset_single_item_response(self):
        question = QuestionFactory.create
        response = self.client.get(reverse("question_item", kwargs={'id': 1}))
        print(reverse("question", kwargs={'id': question.id}))
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
