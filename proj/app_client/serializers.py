from rest_framework import serializers
from timezone_field import choices
import pytz

from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    timezone = serializers.ChoiceField(
        choices=choices.with_gmt_offset(
            pytz.all_timezones))

    class Meta:
        model = Client
        fields = '__all__'