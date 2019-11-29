'''This module contains tests for vouchers app'''
from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse
from vouchers.models import Voucher

class VouchersPageTests(SimpleTestCase):
    '''
    Tests:
        test_vouchers_status_code: Checks for successful http request.
        test_view_url_name: Checks for succesful http request when using url name>
        test_view_correct_template: Check if correct template is >

    '''

    def test_vouchers_status_code(self):
        '''Checks for succesful http request'''

        response = self.client.get('/vouchers/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_name(self):
        '''Checks for successful http request when using url name>'''

        response = self.client.get(reverse('vouchers'))
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        '''Check if correct template is used'''

        response = self.client.get(reverse('vouchers'))
        self.assertTemplateUsed(response, 'vouchers/vouchers.html')

class VouchersModelTests(TestCase):
    '''
    Checks each of the method in Voucher model
    Tests:
        test_str: Check for correct string representation
        test_validate_code: Check for correct string returned for validate() method
        test_discount_rate: Check for correct string returned for discount_rate() method
        test_accept: Check for correct string returned for accept() method

    '''

    def setUp(self):
        '''
        Create test objects from Voucher model.

        '''

        Voucher.objects.create(code_field='q1w2e',
                               discount_field='10',
                               usage_no_field='0',
                               usage_limit_field='3')
        Voucher.objects.create(code_field='q2w3e',
                               discount_field='0.1',
                               usage_no_field='3',
                               usage_limit_field='3')
        Voucher.objects.create(code_field='q3w4e',
                               discount_field='0.1',
                               usage_no_field='0',
                               usage_limit_field='3')

    def test_str(self):
        '''
        Check for correct string representation of object.

        '''

        str_code = Voucher.objects.get(code_field='q1w2e')
        self.assertEqual(str_code.__str__(), 'CODE :q1w2e')

    def test_validate_code(self):
        '''
        Check for correct string returned from validate() method

        '''

        valid_code = Voucher.objects.get(code_field='q1w2e')
        invalid_code = Voucher.objects.get(code_field='q2w3e')
        self.assertEqual(valid_code.validate(), 'Valid')
        self.assertEqual(invalid_code.validate(), 'Invalid')

    def test_discount_rate(self):
        '''
        Check for correct string returned from dicount_rate() method

        '''

        rm_discount = Voucher.objects.get(code_field='q1w2e')
        pct_discount = Voucher.objects.get(code_field='q3w4e')
        invalid_discount = Voucher.objects.get(code_field='q2w3e')
        self.assertEqual(rm_discount.discount_rate(), 'RM10 off')
        self.assertEqual(pct_discount.discount_rate(), '10% off')
        self.assertEqual(invalid_discount.discount_rate(), 'N/A')

    def test_accept(self):
        '''
        Check for correct string returned from accept() method

        '''

        accept_code = Voucher.objects.get(code_field='q1w2e')
        not_accept_code = Voucher.objects.get(code_field='q2w3e')
        self.assertEqual(accept_code.accept(), '* Voucher accepted. Can be reused 2 more times.')
        self.assertEqual(not_accept_code.accept(),
                         '* Voucher not accepted. Exceeded voucher usage limits.')
