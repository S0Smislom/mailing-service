from rest_framework import serializers
from .models import Mailing, Message
from app_client.serializers import ClientSerializer


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    client = ClientSerializer()

    class Meta:
        model = Message
        exclude = ['mailing',]


class TimeZoneSerializer(serializers.Serializer):
    value = serializers.CharField()
    with_gmt = serializers.CharField()
