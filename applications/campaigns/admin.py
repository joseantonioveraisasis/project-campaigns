from django.contrib import admin
from .models import LkClasificacionCampanias,DwCampanias

# Register your models here.



class ListaCampanias(admin.ModelAdmin):
    list_display = (
        'id_campania',
        'nombre_campania',
        'fecha_creacion',
        'fecha_envio',
        'id_clasificacion'
    )
    search_fields  = ('nombre_campania',)

class ListaClasificacion(admin.ModelAdmin):
    list_display = (
        'id_clasificacion',
        'nombre_clasificacion'
    )
admin.site.register(DwCampanias, ListaCampanias)
admin.site.register(LkClasificacionCampanias,ListaClasificacion)