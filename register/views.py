from django.shortcuts import render, redirect
from django.contrib import messages
from .form import RegistrationForm



def register (request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, f'Account Created Successfully')
        return redirect("estateapp-home")
    else:
        form = RegistrationForm()
    return render(request, 'register/form.html', {'form': form})
