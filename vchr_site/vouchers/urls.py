'''This module definws the url pattern for voucher app'''
from django.urls import path
from vouchers import views as vouchers_views

# define urlpatterns
urlpatterns = [
    path('vouchers/', vouchers_views.render_form, name='vouchers'),
    path('voucher_status/', vouchers_views.render_form, name='voucher_status')
]
