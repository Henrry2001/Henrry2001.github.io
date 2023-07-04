from django.shortcuts import render, HttpResponse, redirect
from .models import Tienda
# Create your views here.

def Tendencia(request):

	tienda=Tienda.objects.all()

	return render(request, "ropa.html", {"tendencia": tienda})