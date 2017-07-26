from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.authentication import PasswordlessAuthenticationBackend
from accounts.models import ListUser, Token

class AuthenticateTest(TestCase):

    def setUp(self):
        self.backend = PasswordlessAuthenticationBackend()
        self.email = 'other@user.com'
        self.another_email = "a@b.com"
        self.user = ListUser(email=self.email)
        self.user.username = 'otheruser'
        self.user.save()
        self.uid = "123456"
        self.token = Token.objects.create(email=self.email, uid=self.uid)
        self.another_uid="123"
        self.token_without_user = Token.objects.create(email=self.another_email, uid=self.another_uid)


    def test_return_none_when_token_not_found(self):
        self.assertEqual(self.backend.authenticate('not exist'), None)

    def test_find_user_and_token(self):
        self.assertEqual(self.backend.authenticate(self.uid), self.user)   

    def test_create_user_if_necessary_for_valid_token(self):
        found_user = self.backend.authenticate(self.another_uid)
        new_user = ListUser.objects.get(email=self.another_email)
        self.assertEqual(found_user, new_user)

class GetUserTest(TestCase):

    def test_gets_user_by_email(self):
        backend = PasswordlessAuthenticationBackend()
        other_user = ListUser(email='other@user.com')
        other_user.username = 'otheruser'
        other_user.save()
        desired_user = ListUser.objects.create(email='a@b.com')
        found_user = backend.get_user('a@b.com')
        self.assertEqual(found_user, desired_user)
