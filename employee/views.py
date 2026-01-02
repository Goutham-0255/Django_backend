from django.shortcuts import render
from .models import Employee
from django.http import Http404, HttpResponse

# Create your views here.
def employee_detail(request, pk):

    try:
        employee = Employee.objects.get(pk=pk)
        return HttpResponse(employee)

    except:
        raise Http404