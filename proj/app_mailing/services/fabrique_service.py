import os
import requests

FABRIQUE_TOKEN = os.getenv('FABRIQUE_TOKEN')

def send_request(msg_id, id, phone, message):
    """Отправляет запрос на API fabrique"""
    payload = {
        'id': msg_id,
        'phone': phone,
        'text': message,
    }
    headers = {
        'Authorization': f"Bearer {FABRIQUE_TOKEN}",
    }
    response = requests.post(
        f'https://probe.fbrq.cloud/v1/send/{msg_id}',
        json=payload,
        headers=headers,
    )

    if response.status_code != 200:
        raise Exception()
    return response