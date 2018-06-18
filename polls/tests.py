import datetime

from django.urls import resolve
from django.test import TestCase
from django.utils import timezone

from polls.views import *


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        # Returns False for questions whose pub_date is in the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
