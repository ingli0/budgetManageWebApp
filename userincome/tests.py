from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserIncome, Source

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.source = Source.objects.create(name='Test Source')

    

    def test_add_income_view(self):
        response = self.client.get(reverse('add-income'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'income/add_income.html')

        response = self.client.post(reverse('add-income'), {
            'amount': 100,
            'description': 'Test income',
            'income_date': '2024-02-15',
            'source': self.source.id,
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.assertTrue(UserIncome.objects.filter(owner=self.user, amount=100).exists())

    def test_income_edit_view(self):
        income = UserIncome.objects.create(owner=self.user, amount=200, description='Old description', source=self.source)
        response = self.client.get(reverse('income-edit', args=[income.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'income/edit_income.html')

        response = self.client.post(reverse('income-edit', args=[income.id]), {
            'amount': 300,
            'description': 'New description',
            'income_date': '2024-02-15',
            'source': self.source.id,
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        income.refresh_from_db()
        self.assertEqual(income.amount, 300)
        self.assertEqual(income.description, 'New description')

    def test_delete_income_view(self):
        income = UserIncome.objects.create(owner=self.user, amount=300, description='Test income', source=self.source)
        response = self.client.post(reverse('income-delete', args=[income.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.assertFalse(UserIncome.objects.filter(id=income.id).exists())

