from rest_framework import serializers
from app_mailing.serializers import MailingSerializer, MessageSerializer


class MessageByStatusSerializer(serializers.Serializer):
    status = serializers.CharField()
    count = serializers.IntegerField()


class FullMessageByStatusSerializer(MessageByStatusSerializer):
    items = MessageSerializer(many=True)


class GeneralStatsSerializer(MailingSerializer):
    messages = MessageByStatusSerializer(many=True)


class DetailStatsSerializer(MailingSerializer):
    messages = FullMessageByStatusSerializer(many=True)


class TimeZoneSerializer(serializers.Serializer):
    value = serializers.CharField()
    with_gmt = serializers.CharField()
