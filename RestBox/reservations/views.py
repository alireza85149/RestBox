from django.shortcuts import render, get_object_or_404
from .models import Reservation
from Villas.models import Villa
from datetime import datetime
# Create your views here.
def guest_dashboard(request):
    guest_id = request.session.get('user_id')
    reservs = Reservation.objects.filter(guest_id = guest_id)
    s_city = request.GET.get('city')
    if s_city:
        s_check_in = request.GET.get('check_in')
        s_check_out = request.GET.get('check_out')
        s_check_in = datetime.strptime(s_check_in, "%Y-%m-%d").date()
        s_check_out = datetime.strptime(s_check_out, "%Y-%m-%d").date()
        villas = Villa.objects.filter(city__icontains = s_city)
        searched_villas = []
        for v in villas:
            availabilities = v.availabilities.filter(status = "A", date__gte= s_check_in, date__ls = s_check_out)
            if availabilities.count() == (s_check_out - s_check_in).days :
                searched_villas.append(v)
        return render(request, 'reservations/guest_dashboard.html', {
            'reservs': reservs, 
            'count': reservs.count(),
            'searched_villas' : searched_villas
        })
    else:
        return render(request, 'reservations/guest_dashboard.html', {
            'reservs': reservs,
            'count' : reservs.count(),
            'searched_villas': Villa.objects.all()
        })

def villa_detail(request, villa_id):
    villa = get_object_or_404(Villa, villa_id=villa_id)
    return render(request, 'reservations/villa_detail.html', {'villa': villa})
