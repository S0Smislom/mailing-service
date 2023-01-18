from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from app_mailing.models import Mailing
from ..serializers import GeneralStatsSerializer
from .statistics_service import get_mailings_statistics

def send_email_message(subject, html, emails):
    """Отправляет сообщение на почты"""
    from_ = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, html, from_, emails)
    msg.attach_alternative(html, "text/html")
    return msg.send()

def get_email_addresses():
    """Возвращает адреса зарегестрированных пользователей"""
    users = get_user_model().objects.all()
    return [user.email for user in users]

def get_email_template_context():
    """Возвращает данные для сообщения"""
    mailings = Mailing.objects.filter(start_date__gte = timezone.now() - timedelta(days=1))
    stats = GeneralStatsSerializer(get_mailings_statistics(mailings), many=True)
    return {
        'mailings':stats.data,
        'count': mailings.count()
    }