from django.test import TestCase
from core.models import Question
from django.contrib.auth.models import User


class TestQuestion(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='Mary', email='mary@email.com', password='passmary')
        self.question = Question.objects.create(
            user=user,
            title='This is a test question',
            body='This is a test qeustion body',
        )
    def test_questions_create(self):
        self.assertEqual(self.question.slug, 'this-is-a-test-question')