from django.urls import path
from . import views
app_name = 'payments'
urlpatterns = [
    path('payments/<int:payment_id>', views.payments, name='payments'),
    path('payment_success/<int:payment_id>', views.payment_success, name='payment_success'),
    path('payment_failed/<int:payment_id>', views.payment_failed, name='payment_failed'),
]