from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Brend
# Create your views here.


def index(response):
    return HttpResponse("<h1>Amiriddin</h1>")