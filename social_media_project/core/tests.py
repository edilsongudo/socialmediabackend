from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from .models import Post


User = get_user_model()
c = Client()


class UserTestCast(TestCase):

    def setUp(self):

        self.user_1 = User.objects.create(
            username='user1',
            email='user1@mail.com',
            password='password123')

        self.user_2 = User.objects.create(
            username='user2',
            email='user2@mail.com',
            password='password123')

        self.post1 = Post.objects.create(
            title="Post 1 Title",
            content="Post 1 Content",
            author=self.user_1
        )

        self.post2 = Post.objects.create(
            title="Post 2 Title",
            content="Post 2 Content",
            author=self.user_2
        )


    def test_users_exist(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)
        self.assertNotEqual(user_count, 0)


    def test_posts_exist(self):
        post_count = Post.objects.all().count()
        self.assertEqual(post_count, 2)
        self.assertNotEqual(post_count, 0)


    def test_signup_endpoint(self):
        signup_url = '/accounts/register/'
        data = {"username": "user3", "email": "", "password": "password123"}
        response = self.client.post(signup_url, data, follow=True)
        self.assertEqual(response.status_code, 200)


