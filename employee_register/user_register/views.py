from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from user_register.forms import RegistrationForm

# Create your views here.

def user_register(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('user_home')
    else:
        form = RegistrationForm()

    return render(response, 'user_register/register.html', {'form': form})
