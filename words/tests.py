from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Word


class HomeViewTests(TestCase):
    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_login_page_offers_google_only(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Войти через Google')
        self.assertContains(response, '/accounts/google/login/')
        self.assertNotContains(response, 'password')
        self.assertNotContains(response, 'type="email"')

    def test_authenticated_user_sees_words(self):
        Word.objects.create(italian_word='ciao', translate_word='привет')
        user = get_user_model().objects.create_user(
            username='tester',
            email='tester@example.com',
            password='unused',
        )
        self.client.force_login(user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ciao')
        self.assertContains(response, 'привет')

