from django.urls import path
from . import views

urlpatterns = [
    path('guest_dashboard/<int:guest_id>', views.guest_dashboard, name='guest_dashboard')
]