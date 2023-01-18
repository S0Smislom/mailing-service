from ..tasks import send_message
from ..models import Message
from app_client.services.client_service import filter_clients
from django.utils import timezone
from .message_service import update_message_status
from ..constants import MESSAGE_STATUS_CHOICE



class MailingService:
    """Класс для создания рассылок"""

    def _create_message(self, client, mailing):
        """Создает сообщение в БД"""
        return Message.objects.create(client=client, mailing=mailing)

    def __send_message(self, message):
        """Создает задачу на отправку сообщения"""
        return send_message.s(
            message.pk,
            message.client.pk,
            message.client.phone,
            message.mailing.text)

    def _send_message(self, message):
        """Проверяет начало задачи и отправлет задачу"""
        if message.mailing.start_date > timezone.now():
            self.__send_message(message).apply_async(
                eta=message.mailing.start_date)
            return
        self.__send_message(message).apply_async()


    def start_mailing(self, mailing):
        """Запускает процесс рассылки сообщений"""
        if mailing.end_date and mailing.end_date < timezone.now():
            return
        clients = filter_clients(mailing.filters)
        for client in clients:
            message = self._create_message(client, mailing)
            self._send_message(message)
            update_message_status(message, MESSAGE_STATUS_CHOICE[1][0])
