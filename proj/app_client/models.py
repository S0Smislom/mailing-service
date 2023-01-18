from django.db import models
from timezone_field import TimeZoneField


# Create your models here.
class Client(models.Model):
    phone = models.CharField(max_length=12, unique=True)
    operator_code = models.CharField(max_length=12)
    tag = models.CharField(max_length=32)
    timezone = TimeZoneField(choices_display="WITH_GMT_OFFSET")

    def __str__(self):
        return self.phone