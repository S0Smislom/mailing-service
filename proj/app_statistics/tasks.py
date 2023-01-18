from celery import shared_task
from django.utils import timezone, dateformat
from django.template.loader import get_template

from .services import email_service


@shared_task()
def send_mail():
    """Отправляет статистику на почты зарегестрированных пользователей"""
    context = email_service.get_email_template_context()
    html = get_template('email/statistics_mail.html').render(context)
    emails = email_service.get_email_addresses()
    return email_service.send_email_message(f'Статистика от {dateformat.format(timezone.now(), "Y-m-d")}', html, emails)
