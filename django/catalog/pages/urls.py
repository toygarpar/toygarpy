from django.urls import path
from . import views  #views dosyasına geçiş yapmak için

# http://127.0.0.1:8000

urlpatterns =[
    path("", views.index, name="index"),
    path("about", views.about, name="about"),


]