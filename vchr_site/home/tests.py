'''This module contains tests for home app'''
from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    '''
    Tests:
        test_home_status_code: Checks for succesful http request.
        test_view_url_name: Checks for succesful http request when using url name>
        test_view_correct_template: Check if correct template is used.

    '''

    def test_home_status_code(self):
        '''Checks for succesful http request'''

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_name(self):
        '''Checks for successful http request when using url name'''

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        '''Check if correct template is used'''

        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/home_navigate.html')
