from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from .models import Villa
from django.db import IntegrityError
from users.models import UserProfile

def host_dashboard(request):
    return render(request, 'villas\host_dashboard.html')

def create_villa(request):
    error = None
    if request.method == 'GET':
        return render(request, "villas\create_villa.html")
    else:
        host_id = request.session.get('user_id')
        city = request.POST.get('city')
        title = request.POST.get('title')
        address = request.POST.get('address')
        capacity = request.POST.get('capacity')
        price_per_night = request.POST.get('price_per_night')
        amenities = request.POST.get('amenities')
        try:
            host = UserProfile.objects.get(id=host_id)
            villa = Villa.objects.create(
                host = host,
                city = city,
                title = title,
                address = address,
                capacity = capacity,
                price_per_night = price_per_night,
                amenities = amenities
            )
            return redirect('villas:host_dashboard')
        except IntegrityError:
            error = 'This villa has already been added.'
            return render(request, 'villas\create_villa.html', {'error': error})


def show_my_villas(request):
    host_id = request.session.get('user_id')
    villas = Villa.objects.filter(host_id=host_id)
    
    return render(request, 'villas/my_villas.html', {
        'villas': villas,
        'total': villas.count()
    })
