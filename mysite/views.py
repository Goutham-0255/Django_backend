from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee


def home(request):

    Employee.objects.all()
    return render(request, 'home.html')