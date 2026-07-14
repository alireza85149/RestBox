from django.urls import path
from . import views

app_name = 'Villas'

urlpatterns = [
    path('host_dashboard/', views.host_dashboard, name='host_dashboard'),
    path('create_villa/', views.create_villa, name='create_villa'),
    path('show_my-villas/', views.show_my_villas, name='show_my_villas')
]