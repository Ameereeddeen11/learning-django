from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi this is site Carshop")
