from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'You have reached the dashboard page'})
        self.assertTrue(comment_form.is_valid())
