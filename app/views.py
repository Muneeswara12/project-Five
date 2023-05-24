from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def muni(request):
    return HttpResponse('Hiii!!! Hello!!!')

def muni1(request):
    return render(request,'muni.html')