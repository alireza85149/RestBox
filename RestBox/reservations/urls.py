from django.urls import path
from . import views
app_name = 'reservations'
urlpatterns = [
    path('guest_dashboard/', views.guest_dashboard, name='guest_dashboard'),
    path('villa_detail/<int:villa_id>', views.villa_detail, name='villa_detail'),
]