from django.test import TestCase
from django.test import Client

# Create your tests here.

class RegistrationTestCase(TestCase):
    def setUp(self):
        c = Client()
        # I generate random strings on this website https://www.thewordfinder.com/random-word-generator
        response = c.post('/register/',{
            'username': 'portcommunion', 
            'email': 'wingrider@gmail.com', 
            'password1': 'respondBloating291', 
            'password2': 'respondBloating291'
        })
        self.assertEqual(response.status_code, 302) # successful registration redirects client

    def test_login(self):
        c = Client()

        response = c.post('/login/',{
            'username': 'portcommunion',
            'password': 'respondBoating291'
        })

        # I'm crying 
        # failed login gives a 200 response smh
        self.assertEqual(response.status_code, 200)

        response = c.post('/login/',{
            'username': 'portcommunion',
            'password': 'respondBloating291'
        })

        self.assertEqual(response.status_code, 302)

    
        


