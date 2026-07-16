from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
import random
from django.db import transaction
# Create your views here.
def payments(request, payment_id):
    payment = get_object_or_404(Payment, payment_id=payment_id)
    return render(request, 'payments/payments.html', {'payment':payment})
@transaction.atomic
def payment_success(request, payment_id):
    if request.method != "POST":
        return redirect("reservations:guest_dashboard")
    payment = get_object_or_404(Payment, payment_id = payment_id)
    payment.status = 'success'
    payment.gateway_ref = str(random.randint(1000000, 9999999))
    payment.reservation.status = 'accepted'
    payment.reservation.save()
    payment.save()
    return render(request, 'payments/success.html',{ 'payment_id' : payment_id, 'villa' : payment.reservation.villa})
@transaction.atomic
def payment_failed(request, payment_id):
    if request.method != "POST":
        return redirect("reservations:guest_dashboard")
    payment = get_object_or_404(Payment, payment_id = payment_id)
    payment.status = 'failed'
    payment.gateway_ref = str(random.randint(1000000, 9999999))
    payment.reservation.status = 'rejected'
    payment.reservation.villa.availabilities.filter(date__gte=payment.reservation.check_in,date__lt=payment.reservation.check_out).update(status="A")
    payment.reservation.save()
    payment.save()
    return render(request, 'payments/failed.html',{ 'payment_id' : payment_id, 'villa' : payment.reservation.villa})