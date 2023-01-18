import os
import urllib
import requests

from . import user_service


def get_oauth_link():
    """Возвращает ссылку яндекса с параметрами"""
    url = 'https://oauth.yandex.ru/authorize'
    params = {
        'response_type': 'code',
        'client_id': os.getenv('YANDEX_CLIENT_ID'),
    }
    return f'{url}?{urllib.parse.urlencode(params)}'


def get_yandex_access_token(auth_code: str):
    """Обменивает код на токен"""
    params = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'client_id': os.getenv('YANDEX_CLIENT_ID'),
        'client_secret': os.getenv('YANDEX_CLIENT_SECRET'),
    }
    try:
        r = requests.post(f'https://oauth.yandex.ru/token', data=params)
        return r.json()
    except Exception as e:
        raise Exception({'message': 'Could not get token', 'details': e.args})

def get_yandex_user_info(access_token: str):
    """Возвращает информацию пользователя"""
    params = {
        'oauth_token': access_token,
        # 'jwt_secret': os.getenv("YANDEX_JWT_SECRET")
    }
    try:
        r = requests.get('https://login.yandex.ru/info?format=json', params=params)
        # Get params from response
        response_data = r.json()
        return response_data
    except Exception as e:
        raise Exception({'message': 'Could not get token', 'details': e.args})


def tune_user_info(user_info):
    """Адаптирует данные пользователя"""
    user_data = {}
    user_data['first_name'] = user_info.get('first_name')
    user_data['last_name'] = user_info.get('last_name')
    user_data['email'] = user_info['default_email']
    return user_data


def authenticate(code):
    """Авторизует пользователя"""
    access_token = get_yandex_access_token(code)
    user_info = get_yandex_user_info(access_token.get('access_token'))
    tuned_user_info = tune_user_info(user_info)
    user = user_service.get_user_by_email(tuned_user_info.get('email'))
    if not user:
        user = user_service.create_user(tuned_user_info)
    return user
