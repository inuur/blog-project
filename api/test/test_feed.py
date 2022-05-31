import json

from rest_framework.test import APITestCase, APIClient

from user.models import User


class TestFeed(APITestCase):
    def test_feed(self):
        client1 = APIClient()
        client2 = APIClient()
        user1 = User.objects.create(username='Antonio1', password='super_secret')
        user2 = User.objects.create(username='Antonio2', password='super_secret')
        client1.force_authenticate(user=user1)
        client2.force_authenticate(user=user2)

        client1.post(f'/api/blog/{user2.id}/follow/')
        response = client1.get('/api/feed/')
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['results']), 0)

        client2.post('/api/post/', {
            'title': 'Simple post',
            'text': 'post text',
        })

        response = client1.get('/api/feed/')
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['results']), 1)

        client2.post('/api/post/', {
            'title': 'Simple post',
            'text': 'post text',
        })

        response = client1.get('/api/feed/')
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['results']), 2)

    def test_feed_pagination(self):
        client1 = APIClient()
        client2 = APIClient()
        user1 = User.objects.create(username='Antonio1', password='super_secret')
        user2 = User.objects.create(username='Antonio2', password='super_secret')
        client1.force_authenticate(user=user1)
        client2.force_authenticate(user=user2)

        client1.post(f'/api/blog/{user2.id}/follow/')
        response = client1.get('/api/feed/')
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['results']), 0)

        for _ in range(20):
            client2.post('/api/post/', {
                'title': 'Simple post',
                'text': 'post text',
            })

        response = client1.get('/api/feed/')
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['results']), 10)

    def test_feed_pagination_page_size(self):
        client1 = APIClient()
        client2 = APIClient()
        user1 = User.objects.create(username='Antonio1', password='super_secret')
        user2 = User.objects.create(username='Antonio2', password='super_secret')
        client1.force_authenticate(user=user1)
        client2.force_authenticate(user=user2)

        client1.post(f'/api/blog/{user2.id}/follow/')
        response = client1.get('/api/feed/')
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['results']), 0)

        for _ in range(20):
            client2.post('/api/post/', {
                'title': 'Simple post',
                'text': 'post text',
            })

        response = client1.get('/api/feed/?page_size=6')
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['results']), 6)

        response = client1.get('/api/feed/?page_size=15')
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['results']), 10)
