from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):

    return render(request, "home/home.html")


def base(request):
    return render(request, "home/base.html")

def base1(request):
    return render(request, "home/base2.html")

    
@login_required
def pagina(request):

    return render(request, "home/home.html")

