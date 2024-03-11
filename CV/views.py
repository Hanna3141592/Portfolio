
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def CV(request):
    
    return render(request, "resume.html")
# Create your views here.
