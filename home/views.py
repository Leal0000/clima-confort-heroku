from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib.auth import login,  authenticate

# Create your views here.

def registro(request):

    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password= formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, "home/home.html")

    return render(request, "registration/registrar.html", data)

def home(request):

    return render(request, "home/home.html")


def base(request):
    return render(request, "home/base.html")

def base1(request):
    return render(request, "home/base2.html")

    
def pagina(request):

    return render(request, "home/home.html")

    

