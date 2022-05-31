import json

from rest_framework.test import APITestCase, APIClient

from api.models import Blog, Post
from user.models import User


class TestPost(APITestCase):
    def test_post_create(self):
        client = APIClient()
        user = User.objects.create(username='Antonio', password='super_secret')
        client.force_authenticate(user=user)
        self.assertEqual(Post.objects.all().count(), 0)
        response = client.post('/api/post/', {
            'title': 'New post',
            'text': 'This is a post text!'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.all().count(), 1)

    def test_post_title_is_required(self):
        client = APIClient()
        user = User.objects.create(username='Antonio', password='super_secret')
        client.force_authenticate(user=user)
        response = client.post('/api/post/', {
            'text': 'This is a post text!'
        })
        self.assertEqual(json.loads(response.content), {'title': ['This field is required.']})

    def test_post_text_length(self):
        client = APIClient()
        user = User.objects.create(username='Antonio', password='super_secret')
        client.force_authenticate(user=user)
        response = client.post('/api/post/', {
            'title': 'Long text post!',
            'text': 'O' * 140
        })
        self.assertEqual(response.status_code, 201)
        response = client.post('/api/post/', {
            'title': 'Long text post!',
            'text': 'O' * 141
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {'text': ['Ensure this field has no more than 140 characters.']})

    def test_user_cant_add_post_to_stranger_blog(self):
        client = APIClient()
        user = User.objects.create(username='Antonio', password='super_secret')
        stranger = User.objects.create(username='Stranger', password='super_secret')
        client.force_authenticate(user=user)
        self.assertEqual(Blog.objects.get(author=stranger).posts.count(), 0)

        response = client.post('/api/post/', {
            'title': 'Long text post!',
            'text': 'O' * 40,
            'blog': stranger.id
        })
        self.assertEqual(Blog.objects.get(author=stranger).posts.count(), 0)
        self.assertEqual(Blog.objects.get(author=user).posts.count(), 1)

        content = json.loads(response.content)
        self.assertEqual(content['blog'], user.id)

    def test_mark_post_read(self):
        client = APIClient()
        user = User.objects.create(username='Antonio', password='super_secret')
        stranger = User.objects.create(username='Stranger', password='super_secret')

        client.force_authenticate(user=user)
        response = client.post('/api/post/', {
            'title': 'Long text post!',
            'text': 'post text',
        })

        post_id = Post.objects.get().id
        client.force_authenticate(user=stranger)

        self.assertEqual(stranger.read_posts.count(), 0)
        response = client.post(f'/api/post/{post_id}/read/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(stranger.read_posts.count(), 1)
