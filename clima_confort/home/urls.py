from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.pagina, name="Home"),
    path('principal', views.pagina, name="pagina"),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('base/', views.base,  name="base"),
    path('base2/', views.base1,  name="base2"),
]

#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
