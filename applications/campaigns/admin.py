from django.contrib import admin

from .models import LkClasificacionCampanias,DwCampanias,PgStatActivity,DwBlackListGeneral

# Register your models here.



class ListaCampanias(admin.ModelAdmin):
    list_display = (
        'id_campania',
        'nombre_campania',
        'fecha_creacion',
        'fecha_envio',
        'id_clasificacion',
        'istracked'
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
class ListBlack(admin.ModelAdmin):
        list_display = (
        'id',
        'id_cliente'
    )
admin.site.register(DwCampanias, ListaCampanias)
admin.site.register(LkClasificacionCampanias,ListaClasificacion)
admin.site.register(PgStatActivity, ListActivity)
admin.site.register(DwBlackListGeneral, ListBlack)