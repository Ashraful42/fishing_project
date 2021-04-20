from django.http import HttpResponse
from django.shortcuts import render
from A2.models import Customer

def home(request):
   return render(request, 'home.html')

def showCustomer(request):
   return render(request, 'customers.html')
