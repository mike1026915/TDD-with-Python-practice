import sys
from accounts.models import ListUser, Token

class PasswordlessAuthenticationBackend(object):

    def authenticate(self, uid):
        try:
            token = Token.objects.get(uid=uid)
            return self.get_user(token.email)
        except Token.DoesNotExist:
            return None
        except ListUser.DoesNotExist:
            return ListUser.objects.create(email=token.email)


    def get_user(self, email):
        user = ListUser.objects.get(email=email)
        return user