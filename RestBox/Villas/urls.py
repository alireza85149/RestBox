from django.urls import path
from . import views

app_name = 'Villas'

urlpatterns = [
    path('host_dashboard/', views.host_dashboard, name='host_dashboard'),
    path('create_villa/', views.create_villa, name='create_villa'),
    path('show_my_villas/', views.show_my_villas, name='show_my_villas'),
    path('edit_villa/<int:villa_id>', views.edit_villa, name='edit_villa'),
    path('delete_villa/<int:villa_id>', views.delete_villa, name='delete_villa')
]