from django.contrib import admin
from .models import Mailing, Message

# Register your models here.
admin.site.register(Mailing)
admin.site.register(Message)