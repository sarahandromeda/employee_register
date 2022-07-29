from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from main_register.models import Employee, Department, Company
from main_register.forms import EmployeeForm, DepartmentForm, CompanyForm

# Create your views here.

def home(response):
    return render(response, 'main_register/home.html', {})

def user_home(response):
    user = response.user
    if user.is_authenticated:
        companies = user.company_set.all()
        company_form = CompanyForm()
        if response.method == 'POST':
            company_form = CompanyForm(response.POST)
            if company_form.is_valid():
                form = company_form.save(commit=False)
                form.user = user
                form.save()

                return redirect('user_home')

        values_dict = {
            'user': user, 
            'companies' : companies, 
            'company_form': company_form
            }
        return render(
            response, 
            'main_register/user_home.html', 
            values_dict
            )

    # if unauthenticated always show login request page
    else:
        return render(response,'main_register/signin.html',{})


def department_page(response, company):
    user = response.user
    if user.is_authenticated:
        company = user.company_set.get(id=company)
        departments = company.departments.all()
        department_form = DepartmentForm()
        if response.method == 'POST':
            department_form = DepartmentForm(response.POST)
            if department_form.is_valid():
                company.departments.create(
                    name = department_form.cleaned_data['name'],
                    user = user,
                )

                return redirect('department_page', company=company.id)

        values_dict = {
            'user': user, 
            'departments': departments, 
            'company': company, 
            'department_form': department_form
            }
        return render(
            response, 
            'main_register/department_page.html',
            values_dict
            )

    # if unauthenticated always show login request page
    else:
        return render(response,'main_register/signin.html',{})


def employee_page(response, company, department):
    user = response.user
    if user.is_authenticated:
        employee_form = EmployeeForm()
        department = user.department_set.get(id=department)
        employees = department.employees.all()
        if response.method == 'POST':
            employee_form = EmployeeForm(response.POST)
            if employee_form.is_valid():
                data = employee_form.cleaned_data
                # must use create to add object to related set
                department.employees.create(
                    email = data['email'],
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    phone_number = data['phone_number'],
                    start_date = data['start_date'],
                    title = data['title'],
                    is_supervisor = data['is_supervisor'],
                    user = user
                )

                return redirect(
                    'employee_page', 
                    company = company, 
                    department = department.id,
                    )

        values_dict = {
            'user': user,
            'employees': employees,
            'employee_form': employee_form,
            'department_name': department.name
            }
        return render(response, 'main_register/employee_page.html',values_dict)
    
    # if unauthenticated always show login request page
    else:
        return render(response,'main_register/signin.html',{})
