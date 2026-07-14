from django.shortcuts import render
from .models import reservations

# Create your views here.
def guest_dashboard(request):
    guest_id = request.session.get('user_id')
    reservs = reservations.objects.filter(guest_id = guest_id)
    return render(request, 'reservations/guest_dashboard.html', {
        'reservs': reservs,
        'count' : reservs.count()
    })
