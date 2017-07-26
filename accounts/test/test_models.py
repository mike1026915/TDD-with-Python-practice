from django.test import TestCase
from accounts.models import Token, ListUser

class UserModelTest(TestCase):

    def test_user_is_valid_with_email_only(self):
        user = ListUser(email='a@b.com')
        user.full_clean() # should not raise

    def test_email_is_primary_key(self):
        user = ListUser()
        self.assertFalse(hasattr(user, 'id'))

    def test_is_authenticated(self):
        user = ListUser()
        self.assertTrue(user.is_authenticated())

class TokenModelTest(TestCase):

    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email='a@b.com')
        token2 = Token.objects.create(email='a@b.com')
        self.assertNotEqual(token1.uid, token2.uid)