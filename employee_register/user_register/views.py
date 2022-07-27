from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from user_register.forms import RegistrationForm

# Create your views here.

def user_register(response):
    form = RegistrationForm(response.POST)
    if response.method == 'POST':
        if form.is_valid():
            form.save()
        reversed_url = reverse('user_home')
        print(reversed_url)
        return HttpResponseRedirect(reversed_url)
    else:
        form = RegistrationForm()
    return render(response, 'user_register/register.html', {'form': form})
