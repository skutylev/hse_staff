from django.db import models
from django.contrib.auth.models import User


KINDS_OF_EVENTS = (
    ('1', 'Отпуск'),
    ('2', 'Отгул'),
    ('3', 'Командировка'),
    ('4', 'Больничный'),
    ('5', 'Другое'),
)


class Event(models.Model):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    kind = models.CharField(choices=KINDS_OF_EVENTS, max_length=20, null=True)
    user = models.ForeignKey(User)
    ews_id = models.CharField(max_length=100, null=True)
