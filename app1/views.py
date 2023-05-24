from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def muni2(request):
    return HttpResponse('second app view function')

def muni3(request):
    return render(request,'muni1.html')