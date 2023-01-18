from celery import shared_task
from .models import Message
from .constants import MESSAGE_STATUS_CHOICE
from .services import message_service, fabrique_service


@shared_task(bind=True, throws=(Exception,), autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 10})
def send_message(self, msg_id, id, phone, message):
    """Отправляет сообщение на api fabrique"""
    try:
        response = fabrique_service.send_request(msg_id, id, phone, message)
    except Exception as e:
        raise Exception()
    
    message_service.update_message_status(Message.objects.get(pk=msg_id), MESSAGE_STATUS_CHOICE[2][0])
    return response.json()


    