from rest_framework.test import APITestCase, APIClient

from api.models import Blog
from user.models import User


class TestBlog(APITestCase):
    def test_blog_is_created_on_user_create(self):
        self.assertEqual(Blog.objects.all().count(), 0)
        user = User.objects.create(username='Antonio1', password='super_secret')
        self.assertEqual(Blog.objects.all().count(), 1)

        user_blog = Blog.objects.get()
        self.assertEqual(user_blog.author, user)

        User.objects.create(username='Antonio2', password='super_secret')
        self.assertEqual(Blog.objects.all().count(), 2)

    def test_blog_cannot_be_created_from_api(self):
        client = APIClient()
        user = User.objects.create(username='Antonio', password='super_secret')
        client.force_authenticate(user=user)
        response = client.post('/api/blog/', {}, format='json')
        self.assertEqual(response.status_code, 405)

    def test_follow_and_unfollow_blog(self):
        client = APIClient()
        user1 = User.objects.create(username='Antonio1', password='super_secret')
        user2 = User.objects.create(username='Antonio2', password='super_secret')
        user2_blog = Blog.objects.get(author=user2)
        client.force_authenticate(user=user1)
        self.assertEqual(user1.followed_blogs.count(), 0)
        response = client.post(f'/api/blog/{user2_blog.author.id}/follow/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user1.followed_blogs.count(), 1)
        response = client.post(f'/api/blog/{user2_blog.author.id}/unfollow/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user1.followed_blogs.count(), 0)
