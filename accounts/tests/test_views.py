from django.test import TestCase, Client
from accounts.froms import UserRegisterForm
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile


class TestRegistrationView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_GET(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.failUnless(response.context['form'], UserRegisterForm)

    def test_register_POST_valid(self):
        response = self.client.post(reverse('accounts:register'), data={
            'username':'mary',
            'email':'mary@email.com',
            'password':'marypass',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)

    def test_register_POST_invalid(self):
        response = self.client.post(reverse('accounts:register'), data={
            'username':'mary',
            'email':'invalid_email',
            'password':'marypass'
        })

        self.assertEquals(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response, 'form', field='email', errors=['Enter a valid email address.',])


class TestDashboardView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_dashboard_GET(self):
        User.objects.create_user(username='mary', email='mary@email.com', password='passmary')
        self.client.login(username='mary', password='passmary')
        response = self.client.get(reverse('accounts:dashboard', args=['mary',]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('accounts/dashboard.html')








