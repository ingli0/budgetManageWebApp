from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .utils import token_generator

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.request_password_reset_url = reverse('request-password')
 
    
    def test_login_view(self):
        username = 'testuser'
        password = 'testpassword'
        user = User.objects.create_user(username=username, password=password)

        response = self.client.post(self.login_url, {'username': username, 'password': password})
        self.assertEqual(response.status_code, 302, "Login with valid credentials failed")   
        self.assertTrue('_auth_user_id' in self.client.session, "User is not logged in after successful login")   
 
        
    def test_logout_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302, "Logout failed")   
        self.assertFalse('_auth_user_id' in self.client.session, "User is still logged in after logout")  


    def test_request_password_reset_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        response = self.client.post(self.request_password_reset_url, {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200, "Request password reset with existing email failed")   

        response = self.client.post(self.request_password_reset_url, {'email': 'nonexistent@example.com'})
        self.assertEqual(response.status_code, 200, "Request password reset with non-existing email failed")  
        

        

    def test_registration_view(self):
             
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
            
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200, "Registration with valid data succed")   
        existing_user = User.objects.create_user(username='existinguser', email='existing@example.com', password='existingpassword')
        response = self.client.post(self.register_url, {'username': 'existinguser', 'email': 'existing@example.com', 'password': 'existingpassword'})
        self.assertNotEqual(response.status_code, 400, "Registration with existing username failed")  
 
