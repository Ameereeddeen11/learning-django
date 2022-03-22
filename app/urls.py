from multiprocessing.spawn import import_main_path
from nturl2path import url2pathname
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]