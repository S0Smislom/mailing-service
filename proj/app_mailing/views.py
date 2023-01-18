from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import pytz
from timezone_field import choices

from .models import Mailing
from .serializers import MailingSerializer, TimeZoneSerializer
from .services.mailing_service import MailingService

# Create your views here.
class MailingViewSet(ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
    permission_classes = [IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mailing = serializer.save()
        mailing_service = MailingService()
        mailing_service.start_mailing(mailing)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TimezoneListView(APIView):

    def get(self, request):
        result = [{'value': i[0], 'with_gmt': i[1]}
                  for i in choices.with_gmt_offset(pytz.all_timezones)]
        return Response(TimeZoneSerializer(result, many=True).data)