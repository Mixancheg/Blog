from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>Блог Михаила Егошина</title><h1>Михаил Егошин</h1></html>')