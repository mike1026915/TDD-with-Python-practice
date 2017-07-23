import os
import uuid
from django.db import models
from django.utils import timezone

class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=36, default=uuid.uuid4)


class ListUser(models.Model):
    email = models.EmailField(primary_key=True)
    last_login = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    def is_authenticated(self):
        return True