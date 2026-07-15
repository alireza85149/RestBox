from django.urls import path
from . import views
app_name = 'availability'
urlpatterns = [
    path('availability/<int:villa_id>', views.availability, name='avilability'),
    path('update_availability/<int:villa_id>', views.update_availability, name='update_availability'),
]