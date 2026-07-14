from django.shortcuts import render
from .models import Reservation

# Create your views here.
def guest_dashboard(request):
    guest_id = request.session.get('user_id')
    reservs = Reservation.objects.filter(guest_id = guest_id)
    return render(request, 'reservations/guest_dashboard.html', {
        'reservs': reservs,
        'count' : reservs.count()
    })
