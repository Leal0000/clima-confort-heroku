from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.table, name="Table"),
    path('Formulario',views.formulario, name="Form"),
    path('eliminar/<id>/', views.eliminar, name="eliminar"),
    path('actualizar/<id>/', views.actualizar, name="actualizar")
]

