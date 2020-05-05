from django.test import TestCase
from .models import Question
import datetime
from django.utils import timezone
from django.urls import reverse

# Create your tests here.


class QuestionModelTestCases(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_past_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Creates a question with the given text and pub_date as time now added by the number of days given
    :param question_text:
    :param days:
    :return:
    """
    time = timezone.now() + timezone.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTestCases(TestCase):
    def test_no_questions(self):
        """
        If no questions exists, return a message stating the same
        :return:
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with pub_date in the past should be shown
        :return:
        """
        create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question>'])

    def test_future_question(self):
        """
        Future question shouldn't be displayed
        :return:
        """
        create_question(question_text="Future Question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_future_question(self):
        """
        When both past and future questions are there, the view needs to show the past question and not the future one.
        :return:
        """
        create_question(question_text="Past Question", days=-30)
        create_question(question_text="Future Question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question>'])

    def test_two_past_question(self):
        """
        If two past questions are present, both should be displayed
        :return:
        """
        create_question(question_text="Past Question 1", days=-30)
        create_question(question_text="Past Question 2", days=-20)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question 2>',
                                                                            '<Question: Past Question 1>'])



