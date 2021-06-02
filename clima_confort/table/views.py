from django.shortcuts import render, HttpResponse

# Create your views here.


def table(request):
    
    return render(request, "table/table.html")

def formulario(request):
    
    return render(request, "table/formulario.html")
     