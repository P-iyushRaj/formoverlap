from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Patient
from .serializer import PatientSerializer

class PatientApi(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


from django.http import HttpResponse

def index(request):
    context ={ 
        "data":"Gfg is the best", 
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    } 
    return render(request, "form.html", context) 