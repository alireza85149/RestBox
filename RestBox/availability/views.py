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
    j_days = {1: 31, 2: 31, 3: 31, 4: 31, 5: 31, 6: 31, 7: 30, 8: 30, 9: 30, 10: 30, 11: 30, 12: 29}
    
    villa = get_object_or_404(Villa, villa_id=villa_id)
    
    if villa.host_id_id != request.session.get('user_id'):
        return render(request, 'availability/error.html')
    
    year = int(request.GET.get('year', jdatetime.date.today().year))
    month = int(request.GET.get('month', jdatetime.date.today().month))
    
    if request.method == 'POST':
        year = int(request.POST.get('year', year))
        month = int(request.POST.get('month', month))
    
    if month == 12 and jdatetime.date(year, 12, 1).isleap():
        days = 30
    else:
        days = j_days.get(month, 31)
    
    if request.method == 'POST':
        for day in range(1, days + 1):
            status = request.POST.get(f'day_{day}')
            if status:
                jdate = jdatetime.date(year=year, month=month, day=day)
                gdate = jdate.togregorian()
                jalali_date = jdate.strftime('%Y/%m/%d')
                
                avail, created = Availability.objects.get_or_create(
                    villa=villa,
                    date=gdate,
                    defaults={
                        'status': status,
                        'jalali_date': jalali_date
                    }
                )
                if not created:
                    avail.status = status
                    avail.jalali_date = jalali_date
                    avail.save()
        
        return redirect('Villas:show_my_villas')
    
    saved_statuses = {}
    for day in range(1, days + 1):
        try:
            jdate = jdatetime.date(year=year, month=month, day=day)
            gdate = jdate.togregorian()
            avail = Availability.objects.get(villa=villa, date=gdate)
            saved_statuses[day] = avail.status
        except Availability.DoesNotExist:
            saved_statuses[day] = 'N'
    
    days_list = []
    for day in range(1, days + 1):
        days_list.append({
            'day': day,
            'status': saved_statuses[day]
        })
    
    month_names = {
        1: 'farvardin', 2: 'ordibehesht', 3: 'khordad',
        4: 'tir', 5: 'mordad', 6: 'shahrivar',
        7: 'mehr', 8: 'aban', 9: 'azar',
        10: 'dey', 11: 'bahman', 12: 'esfand'
    }
    
    return render(request, 'availability/update_availability.html', {
        'villa': villa,
        'year': year,
        'month': month,
        'month_name': month_names[month],
        'days_list': days_list,
    })