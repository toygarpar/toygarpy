from django.shortcuts import render
from django.http import HttpResponse 
#http talebi yapıp request objesi oluşturmak için, talep ddoğrultusunda bir response geri gönderilecek


# Create your views here.
# http://127.0.0.1:8000/

def index(request):
    #return HttpResponse("<h1>Hello from pages app</h1>")
    return render( request, "pages/index.html")



def about(request):
    
    return render( request, "pages/about.html")
