from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.user_home, name= 'user_home'),
    path('<int:company>/', views.department_page, name='department_page'),
    path('<int:company>/<int:department>/', views.employee_page, name='employee_page')
]