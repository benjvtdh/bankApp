from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'core/index.html')

from django.shortcuts import render


def index(request):
    return render(request,'core/index.html')