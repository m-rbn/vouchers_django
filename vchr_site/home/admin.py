'''This module register the Voucher model to the vouchers app'''
from django.contrib import admin
from .models import Voucher

# Register voucher model
admin.site.register(Voucher)
