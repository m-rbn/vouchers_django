'''This module contains the  Voucher model used by the vouchers app'''
from django.db import models

# Voucher code
class Voucher(models.Model):
    '''
    Voucher is a model with four fields containing attributes of a voucher code.

    Fields:
        code_field: Voucher code to be inputted
        discount_field: How much discount to give.
                        If whole number, RM (value) off.
                        If float, (value)% off.
        usage_no_field: How many times the voucher code has been used.
        usage_limit_field: How many time the voucher code can be used.

    Methods:
        self.validate: validate method to check validity of voucher code.
                       Returns the validity status of the code.
        self.discount_rate: discount_rate method to return discount value string.
        self.accept: accept method to accept value voucher code and modify the usage_no_field.

    '''
    objects = models.Manager()
    code_field = models.CharField(max_length=5)
    discount_field = models.FloatField()
    usage_no_field = models.IntegerField(default=0)
    usage_limit_field = models.IntegerField(default=3)


    def __str__(self):
        code_str = str(self.code_field)
        return code_str

    def validate(self):
        '''Validate method to check validity of boucher code'''
        if self.usage_no_field >= self.usage_limit_field:
            return 'Invalid'
        return 'Valid'

    def discount_rate(self):
        '''Method to return discount value string'''
        if self.validate() == 'Valid':
            if float(self.discount_field).is_integer() is True:
                rm_str = 'RM'+str(int(self.discount_field))+' off'
                return rm_str
            pct_str = str(int(self.discount_field*100))+'% off'
            return pct_str
        return 'N/A'

    def accept(self):
        '''Method to show whether voucher is accepted or not'''
        if self.validate() == 'Valid':
            self.usage_no_field += 1
            self.save()
            n_left = str(self.usage_limit_field-self.usage_no_field)
            accept_str = '* Voucher accepted. Can be reused '+ n_left + ' more times.'
            return accept_str
        not_accept_str = '* Voucher not accepted. Exceeded voucher usage limits.'
        return not_accept_str
