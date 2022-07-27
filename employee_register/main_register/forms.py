from django.forms import ModelForm
from main_register.models import Employee, Department, Company

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['user']

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        exclude = ['user', 'employees']

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['user', 'departments']