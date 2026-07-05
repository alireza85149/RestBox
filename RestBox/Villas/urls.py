from django.urls import path
from . import views

app_name = 'villas'

urlpatterns = [
    path('create/', views.create_villa, name='create_villa'),
    path('my-villas/', views.my_villas, name='my_villas'),
    path('<int:villa_id>/', views.villa_detail, name='villa_detail'),
    path('<int:villa_id>/edit/', views.edit_villa, name='edit_villa'),
    path('<int:villa_id>/delete/', views.delete_villa, name='delete_villa'),
]