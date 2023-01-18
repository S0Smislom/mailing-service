from ..models import Client

def get_filters(filters_str:str):
    """Форматирует фильтры"""
    filters_list = filters_str.split(';')
    res = {}
    for filter in filters_list:
        k,v = filter.split('=')
        res[k] = v
    return res

def filter_clients(filters=None):
    """Возвращает список клиентов"""
    if filters:
        return Client.objects.filter(**get_filters(filters))
    return Client.objects.all()