from django.test import TestCase
from django.utils import timezone
from .models import Client
from .services import client_service

# Create your tests here.



class ClientAPITest(TestCase):

    def setUp(self):
        self.test_client = Client.objects.create(
            phone='79629999999',
            operator_code='962',
            tag='hello',
            timezone=timezone.get_default_timezone(),
        )

    def test_client_get_all_clients(self):
        response = self.client.get('/api/v1/client/')
        self.assertTrue(isinstance(response.data, list))

    def test_create_client(self):
        payload = {
            'phone':'79139999999',
            'operator_code': '913',
            'tag': 'hello',
            'timezone': timezone.get_default_timezone_name(),
        }
        response = self.client.post('/api/v1/client/', data=payload, content_type='application/json')
        self.assertTrue(response.status_code == 201)
        self.assertEqual(payload.get('phone'), response.data.get('phone'))

    def test_update_client(self):
        payload = {
            'phone':'79139999999',
            'operator_code': '913',
            'tag': 'h',
            'timezone': timezone.get_default_timezone_name(),
        }
        response = self.client.put(f'/api/v1/client/{self.test_client.pk}/', data=payload, content_type='application/json')
        self.assertTrue(response.status_code == 200)
        self.assertNotEqual(response.data.get('tag'), self.test_client.tag)

    def test_delete_client(self):
        response = self.client.delete(f'/api/v1/client/{self.test_client.pk}/')
        self.assertTrue(response.status_code == 204)

class ClientServiceTests(TestCase):
    filters_str = 'tag=h;operator_code=913'
    filters = {
        'tag': 'h',
        'operator_code': '913',
    }

    def setUp(self):
        Client.objects.create(
            phone='79629999999',
            operator_code='962',
            tag='hello',
            timezone=timezone.get_default_timezone(),
        )
        Client.objects.create(
            phone='79889999999',
            operator_code='988',
            tag='hello',
            timezone=timezone.get_default_timezone(),
        )
        Client.objects.create(
            phone='79139999999',
            operator_code='913',
            tag='h',
            timezone=timezone.get_default_timezone(),
        )

    def test_get_filters(self):
        res_filters = client_service.get_filters(self.filters_str)
        self.assertTrue(isinstance(res_filters, dict))
        self.assertEqual(res_filters, self.filters)

    def test_filter_clients(self):
        clients = client_service.filter_clients(self.filters_str)
        self.assertTrue(clients.count() == 1)

    def test_filter_clients_without_filters(self):
        clients = client_service.filter_clients()
        self.assertTrue(clients.count() == 3)
