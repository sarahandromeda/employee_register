from django.shortcuts import render
from main_register.models import Employee, Department, Company

# Create your views here.

def home(response):
    return render(response, 'main_register/home.html', {})

def user_home(response):
    user = response.user
    if user.is_authenticated:
        companies = user.company_set.all()
        if response.method == 'GET':
            print(dir(response.user))
        return render(
            response, 
            'main_register/user_home.html', 
            {'user': user, 'companies' : companies}
            )
    else:
        return render(
            response,
            'main_register/signin.html',
            {}
        )

def department_page(response, company):
    user = response.user
    if user.is_authenticated:
        departments = user.department_set.all()

        return render(
            response, 
            'main_register/department_page.html',
            {'user': user, 'departments': departments}
            )
    else:
        return render(
            response,
            'main_register/signin.html',
            {}
        )

def employee_page(response, company, department):
    user = response.user
    if user.is_authenticated:
        employees = user.employee_set.all()
        return render(
            response, 
            'main_register/employee_page.html',
            {'user': user, 'employees': employees}
            )
    else:
        return render(
            response,
            'main_register/signin.html',
            {}
        )
