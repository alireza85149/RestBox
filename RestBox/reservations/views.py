from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from Villas.models import Villa
from users.models import UserProfile
from payments.models import Payment
from availability.models import Availability
from datetime import datetime
from django.db import transaction
from django.contrib import messages
import jdatetime

# Create your views here.
def guest_dashboard(request):
    guest_id = request.session.get('user_id')
    reservs = Reservation.objects.filter(guest_id = guest_id)
    s_city = request.GET.get('city')
    if s_city:
        jmonths={"فروردین":1, "اردیبهشت":2, "خرداد":3, "تیر":4, "مرداد":5, "شهریور":6, "مهر":7, "آبان":8, "آذر":9, "دی":10, "بهمن":11, "اسفند":12}
        ijy = int(request.GET["check_in_year"])
        ijm = (request.GET["check_in_month"])
        ijm = jmonths[ijm]
        ijd = int(request.GET["check_in_day"])
        s_check_in = jdatetime.date(ijy, ijm, ijd).togregorian()
        ojy = int(request.GET["check_out_year"])
        ojm = (request.GET["check_out_month"])
        ojm = jmonths[ojm]
        ojd = int(request.GET["check_out_day"])
        s_check_out = jdatetime.date(ojy, ojm, ojd).togregorian()
        villas = Villa.objects.filter(city__icontains = s_city)
        searched_villas = []
        for v in villas:
            availabilities = v.availabilities.filter(status = "A", date__gte= s_check_in, date__lt = s_check_out)
            if availabilities.count() == (s_check_out - s_check_in).days :
                searched_villas.append(v)
        return render(request, 'reservations/guest_dashboard.html', {
            'reservs': reservs, 
            'count': reservs.count(),
            'searched_villas' : searched_villas,
            'years': range(1405, 1506),
            'months':["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"],
            'days' : range(1, 32)
        })
    else:
        return render(request, 'reservations/guest_dashboard.html', {
            'reservs': reservs,
            'count' : reservs.count(),
            'searched_villas': Villa.objects.all(),
            'years': range(1405, 1506),
            'months':["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"],
            'days' : range(1, 32)
        })

def villa_detail(request, villa_id):
    villa = get_object_or_404(Villa, villa_id=villa_id)
    user_id = request.session.get('user_id')
    
    availabilities = villa.availabilities.all().order_by("date")
    for avail in availabilities:
        if avail.date:
            jdate = jdatetime.date.fromgregorian(date=avail.date)
            avail.jalali_date = jdate.strftime('%Y/%m/%d')
    
    if request.method == "POST":
        jmonths={"فروردین":1, "اردیبهشت":2, "خرداد":3, "تیر":4, "مرداد":5, "شهریور":6, "مهر":7, "آبان":8, "آذر":9, "دی":10, "بهمن":11, "اسفند":12}
        ijy = int(request.GET["check_in_year"])
        ijm = (request.GET["check_in_month"])
        ijm = jmonths[ijm]
        ijd = int(request.GET["check_in_day"])
        check_in = jdatetime.date(ijy, ijm, ijd).togregorian()
        ojy = int(request.GET["check_out_year"])
        ojm = (request.GET["check_out_month"])
        ojm = jmonths[ojm]
        ojd = int(request.GET["check_out_day"])
        check_out = jdatetime.date(ojy, ojm, ojd).togregorian()
        if check_out <= check_in:
            messages.error(request, "Invalid date range.")
            return redirect("reservations:villa_detail", villa_id=villa_id)
        
        with transaction.atomic():
            availabilities_check = Availability.objects.select_for_update().filter(
                villa=villa,
                date__gte=check_in,
                date__lt=check_out
            )
            
            if availabilities_check.filter(status="A").count() != (check_out - check_in).days:
                messages.error(request, "Villa is no longer available.")
                return redirect('reservations:guest_dashboard')
            nights = (check_out - check_in).days
            total_price = nights * villa.price_per_night
            reservation = Reservation.objects.create(
                villa=villa,
                guest_id=user_id,
                check_in=check_in,
                check_out=check_out,
                total_price=total_price
            )
            availabilities_check.update(status='R')
            payment = Payment.objects.create(reservation=reservation, amount=total_price)
            return redirect('payments:payments', payment.payment_id)
    
    return render(request, 'reservations/villa_detail.html', {
        'villa': villa,
        'availabilities': availabilities,
    })
