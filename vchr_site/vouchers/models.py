from django.db import models

# Voucher code
class Voucher(models.Model):
    code_field =  models.IntegerField()                   #   Voucher code to be inputted
    discount_field = models.FloatField()                  #   How much discount to give
                                                    #   (if whole number, RM [value] off)
                                                    #   (if float, [value]% off)
    usage_no_field = models.IntegerField(default=0)       #   How many times it has been used
    usage_limit_field = models.IntegerField(default=3)    #   How many time it can be used

    # def __str__
    def __str__(self):
        return str(self.code_field)

    # def validate method to check validity
    def validate(self):
        if self.usage_no_field >= self.usage_limit_field:
            return 'Invalid'
        else:
            return 'Valid'

    # def method to retun discount string
    def discount_rate(self):
        if self.validate() ==  'Valid':
            if self.discount_field.is_integer() == True:
                return 'RM'+str(int(self.discount_field))+' off'
            else:
                return str(int(self.discount_field*100))+'% off'
        else:
            return 'N/A'

    # def method to show whether voucher accepted or not
    def accept(self):
        if self.validate() ==  'Valid':
            self.usage_no_field += 1
            self.save()
            return '* Voucher accepted. Can be reused '+ str(self.usage_limit_field-self.usage_no_field) + ' more times'
        else:
            return '* Voucher not accepted. Exceeded voucher usage limit.'
