from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Villa
from django.db import IntegrityError
from users.models import UserProfile
import jdatetime

def host_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('users:user_login', role='host')
    return render(request, 'Villas/host_dashboard.html')

def create_villa(request):
    error = None
    if request.method == 'GET':
        return render(request, "Villas/create_villa.html")
    else:
        session_user_id = request.session.get('user_id')
        
        if not session_user_id:
            error = 'Please login first.'
            return render(request, 'Villas/create_villa.html', {'error': error})
        
        city = request.POST.get('city')
        title = request.POST.get('title')
        address = request.POST.get('address')
        capacity = request.POST.get('capacity')
        price_per_night = request.POST.get('price_per_night')
        amenities = {
            'wifi': request.POST.get('amenities_wifi') == 'true',
            'parking': request.POST.get('amenities_parking') == 'true',
            'pool': request.POST.get('amenities_pool') == 'true',
        }
        try:
            host = UserProfile.objects.get(user_id=session_user_id)
            villa = Villa.objects.create(
                host_id=host,
                city=city,
                title=title,
                address=address,
                capacity=capacity,
                price_per_night=price_per_night,
                amenities=amenities
            )
            return redirect(reverse('availability:update_availability', kwargs={"villa_id":villa.villa_id}))
        except UserProfile.DoesNotExist:
            error = 'User not found. Please login again.'
            return render(request, 'Villas/create_villa.html', {'error': error})
        except IntegrityError:
            error = 'This villa has already been added.'
            return render(request, 'Villas/create_villa.html', {'error': error})

def show_my_villas(request):
    user_id = request.session.get('user_id')
    villas = Villa.objects.filter(host_id_id=user_id)
    
    return render(request, 'Villas/my_villas.html', {
        'villas': villas,
        'total': villas.count()
    })

def edit_villa(request, villa_id):
    user_id = request.session.get('user_id')
    villa = get_object_or_404(Villa, villa_id=villa_id, host_id_id=user_id)
    
    if request.method == 'POST':
        villa.title = request.POST.get('title')
        villa.city = request.POST.get('city')
        villa.address = request.POST.get('address')
        villa.capacity = request.POST.get('capacity')
        villa.price_per_night = request.POST.get('price_per_night')
        villa.amenities = request.POST.get('amenities')
        
        try:
            villa.save()
            return redirect('Villas:show_my_villas')
        except IntegrityError:
            error = 'This address already exists.'
            return render(request, 'Villas/edit_villa.html', {
                'villa': villa,
                'error': error
            })
    
    return render(request, 'Villas/edit_villa.html', {'villa': villa})

def delete_villa(request, villa_id):
    user_id = request.session.get('user_id')
    villa = get_object_or_404(Villa, villa_id=villa_id, host_id_id=user_id)
    
    if request.method == 'POST':
        villa.delete()
        return redirect('Villas:show_my_villas')
    
    return render(request, 'Villas/delete_villa.html', {'villa': villa})