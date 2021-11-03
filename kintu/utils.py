from django.db import models
from django.contrib.auth.models import User, Group

import threading

_thread_locals = threading.local()


def set_current_user(user):
    _thread_locals.user = user


def get_current_user():
    return getattr(_thread_locals, 'user', None)


def remove_current_user():
    _thread_locals.user = None


"""
This class will be inherited by the models to automatically provide some kind of 
auth signature to every database transaction.
"""


class AuthSignature(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False,
                                   related_name='%(class)s_created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False,
                                    related_name='%(class)s_modified')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user
            if not self.id:
                self.created_by = user
        super(AuthSignature, self).save(*args, **kwargs)

    class Meta:
        abstract = True
