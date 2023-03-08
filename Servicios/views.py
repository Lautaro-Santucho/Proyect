from django.shortcuts import render
from Servicios.models import Servicios

# Create your views here.

def servicios(request):
    servicios= Servicios.objects.all()
    return render(request, "Servicios/servicios.html", {"servicios": servicios})