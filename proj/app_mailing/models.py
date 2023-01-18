from django.db import models
from django.utils import timezone

from .constants import MESSAGE_STATUS_CHOICE
from app_client.models import Client

# Create your models here.
class Mailing(models.Model):
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    text = models.CharField(max_length=255)
    filters = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.pk)


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=MESSAGE_STATUS_CHOICE, default=MESSAGE_STATUS_CHOICE[0][0])
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)