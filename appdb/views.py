from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello! Home")

def test(request):
    return HttpResponse("Hello! Test")

def index(request):
    return render(request, 'appdb/index.html')