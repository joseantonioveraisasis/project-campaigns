from django.contrib import admin

from .models import LkClasificacionCampanias,DwCampanias,PgStatActivity

# Register your models here.



class ListaCampanias(admin.ModelAdmin):
    list_display = (
        'id_campania',
        'nombre_campania',
        'fecha_creacion',
        'fecha_envio',
        'id_clasificacion',
        'tracked'
    )
    search_fields  = ('nombre_campania',)

class ListaClasificacion(admin.ModelAdmin):
    list_display = (
        'id_clasificacion',
        'nombre_clasificacion'
    )

class ListActivity(admin.ModelAdmin):
    list_display = (
        'pid',
        'query_start',
        'state_change',
        'state',
        'query'
    )
admin.site.register(DwCampanias, ListaCampanias)
admin.site.register(LkClasificacionCampanias,ListaClasificacion)
admin.site.register(PgStatActivity, ListActivity)