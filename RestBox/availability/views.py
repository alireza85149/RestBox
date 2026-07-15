from django.shortcuts import render, get_object_or_404, redirect
from .models import Availability
from Villas.models import Villa
import jdatetime
# Create your views here.
def availability(request, villa_id):
    villa = get_object_or_404(Villa, villa_id=villa_id)
    dates = villa.availabilities.all().order_by("date")
    return render(request, 'availability/availability.html', {'villa': villa, 'dates': dates})
def update_availability(request, villa_id):
    if villa.host_id != request.session.get('user_id'):
        return render(request, 'availability/error.html')
    if request.method == 'POST':
        villa = get_object_or_404(Villa , villa_id = villa_id)
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        j_days = {1: 31, 2: 31, 3: 31, 4: 31, 5: 31, 6: 31, 7: 30, 8: 30, 9: 30, 10: 30, 11: 30, 12: 29}
        if month == 12 and jdatetime.date(year, 12, 1).isleap():
            days = 30
        else:
            days = j_days[month]
        for i in range(1, days+1):
            status = request.POST.get(f'{i}')
            if status is None:
                continue
            jdate = jdatetime.date(year=year, month=month, day=i)
            date = jdate.togregorian()
            d, created = Availability.objects.get_or_create(villa= villa, date= date)
            d.status = status
            d.save()
        return redirect('availability:update_availability', villa_id=villa_id )
    return render(request, 'availability/update_availability.html', {
            "villa": villa,
            "current_year": jdatetime.date.today().year,
            "current_month": jdatetime.date.today().month,
            "days" : range(1, j_days[jdatetime.date.today().month]+1)
    })
        


