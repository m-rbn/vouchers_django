from django.urls import path

from vouchers import views as vouchers_views

# define urlpatterns
urlpatterns = [
    path('vouchers/', vouchers_views.RenderForm),
    path('voucher_status/', vouchers_views.RenderForm)
]
