from django.contrib import admin
from .models import tipo_poliza, registro

# Register your models here.

class tipo_polizaAdmin(admin.ModelAdmin):
    
    readonly_fields=('created','updated')

class registroAdmin(admin.ModelAdmin):
    
    readonly_fields=('created','updated')

admin.site.register(tipo_poliza, tipo_polizaAdmin)
admin.site.register(registro, registroAdmin)