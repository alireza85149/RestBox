from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.index, name = 'index'), 
    path('role_handling/', views.role_handling, name='role_handling'),
    path('registeration/<str:role>/', views.registeration, name = 'registeration'),
    path('user_login/<str:role>/', views.login, name='user_login'),
]