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
        user = get_user_model().objects.create_user(
            username='tester',
            email='tester@example.com',
            password='unused',
        )
        Word.objects.create(user=user, italian_word='ciao', translate_word='привет')
        self.client.force_login(user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ciao')
        self.assertContains(response, 'привет')
        self.assertContains(response, 'data-action="learned"')
        self.assertNotContains(response, 'btn-learned is-learned')

    def test_learned_word_button_is_marked_when_already_learned(self):
        user = get_user_model().objects.create_user(
            username='tester',
            email='tester@example.com',
            password='unused',
        )
        Word.objects.create(
            user=user,
            italian_word='ciao',
            translate_word='привет',
            is_learned=True,
        )
        self.client.force_login(user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'btn-learned is-learned')
        self.assertContains(response, 'Marked as learned')


class LearnedWordViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@example.com',
            password='unused',
        )
        self.word = Word.objects.create(
            user=self.user,
            italian_word='ciao',
            translate_word='привет',
        )
        self.client.force_login(self.user)

    def test_mark_as_learned_toggles_and_keeps_word(self):
        url = reverse('learned_word', args=[self.word.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok', 'is_learned': True})
        self.word.refresh_from_db()
        self.assertTrue(self.word.is_learned)
        self.assertTrue(Word.objects.filter(id=self.word.id).exists())

    def test_mark_as_learned_can_be_unmarked(self):
        self.word.is_learned = True
        self.word.save()
        url = reverse('learned_word', args=[self.word.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok', 'is_learned': False})
        self.word.refresh_from_db()
        self.assertFalse(self.word.is_learned)

