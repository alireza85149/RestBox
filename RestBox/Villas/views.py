from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Villa
from .forms import VillaForm

@login_required
def create_villa(request):
    if request.user.role != 'host':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('users:index')
    
    if request.method == 'POST':
        form = VillaForm(request.POST)
        if form.is_valid():
            villa = form.save(commit=False)
            villa.host = request.user
            villa.save()
            messages.success(request, 'Villa created successfully!')
            return redirect('villas:villa_detail', villa_id=villa.id)
        else:
            messages.error(request, 'Error creating villa. Please check the information.')
    else:
        form = VillaForm()
    
    return render(request, 'villas/create_villa.html', {'form': form})

@login_required
def my_villas(request):
    villas = Villa.objects.filter(host=request.user)
    return render(request, 'villas/my_villas.html', {'villas': villas})

def villa_detail(request, villa_id):
    villa = get_object_or_404(Villa, id=villa_id)
    return render(request, 'villas/villa_detail.html', {'villa': villa})

@login_required
def edit_villa(request, villa_id):
    villa = get_object_or_404(Villa, id=villa_id)
    
    if request.user != villa.host:
        messages.error(request, 'You do not have permission to edit this villa.')
        return redirect('villas:my_villas')
    
    if request.method == 'POST':
        form = VillaForm(request.POST, instance=villa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Villa updated successfully!')
            return redirect('villas:villa_detail', villa_id=villa.id)
    else:
        form = VillaForm(instance=villa)
    
    return render(request, 'villas/edit_villa.html', {'form': form, 'villa': villa})

@login_required
def delete_villa(request, villa_id):
    villa = get_object_or_404(Villa, id=villa_id)
    
    if request.user != villa.host:
        messages.error(request, 'You do not have permission to delete this villa.')
        return redirect('villas:my_villas')
    
    if request.method == 'POST':
        villa.delete()
        messages.success(request, 'Villa deleted successfully!')
        return redirect('villas:my_villas')
    
    return render(request, 'villas/delete_villa.html', {'villa': villa})