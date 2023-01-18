from app_mailing.constants import MESSAGE_STATUS_CHOICE
from app_mailing.models import Message


def get_messages_by_status(mailing):
    """Сортирует сообщения конкретной рассылки по статусам"""
    messages_by_status = []
    for status in MESSAGE_STATUS_CHOICE:
        message_list = Message.objects.filter(
            status=status[0], mailing=mailing)
        count = message_list.count()
        messages_by_status.append({
            'count': count,
            'status': status[0],
            'items': message_list,
        })
    return messages_by_status

def get_mailing_statistics(mailing):
    """Возвращает конкретную рассылку"""
    messages_by_status = get_messages_by_status(mailing)
    return {**mailing.__dict__, 'messages': messages_by_status}

def get_mailings_statistics(mailings):
    """Возвращает общую статистику по рассылкам"""
    return [get_mailing_statistics(mailing) for mailing in mailings]