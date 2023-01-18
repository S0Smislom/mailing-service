
def update_message_status(message, status):
    """Обнавляет статус сообщения"""
    if message:
        message.status = status
        message.save()
    return message