from django.test import Client
from django.test import TestCase
from faker import Faker
from user_reminders.models import SiteUser


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()
        self.user = SiteUser.objects.create_user(username='test_user', email='test@test.com', password='test1234567',
                                                 user_chat=1236958624)

    def test_statuses(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_required(self):
        self.client.force_login(self.user)

        response = self.client.get('/users/index/')
        self.assertEqual(response.status_code, 200)

        self.assertTrue(self.user.is_authenticated)

        self.assertEqual(self.user.username, 'test_user')



    def test_logout(self):

        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 302)


