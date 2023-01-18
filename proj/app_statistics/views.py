from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import GeneralStatsSerializer, DetailStatsSerializer
from app_mailing.models import Mailing
from .services.statistics_service import get_mailings_statistics, get_messages_by_status, get_mailing_statistics
from .tasks import send_mail

class GetSerializerClassMixin:

    def get_serializer(self):
        return self.serializer_class()


class GeneralStatsView(APIView, GetSerializerClassMixin):

    permission_classes = [IsAuthenticated,]
    serializer_class = GeneralStatsSerializer

    def get(self, request):
        mailings = Mailing.objects.all().order_by('-start_date')
        stats = get_mailings_statistics(mailings)
        general_stats = GeneralStatsSerializer(stats, many=True)
        return Response(general_stats.data)


class DetailStatsView(APIView, GetSerializerClassMixin):

    serializer_class = DetailStatsSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request, id):
        mailing = get_object_or_404(Mailing, pk=id)
        stats = get_mailing_statistics(mailing)
        result = DetailStatsSerializer(stats)
        return Response(result.data)

class StatsTest(APIView):
    def get(self, request):
        send_mail.delay()
        return Response(True)