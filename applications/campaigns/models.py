# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import date
from django.utils import timezone
from tabnanny import verbose
from django.db import models

#managers
from .managers import ListCampaignsManager, CreateCampaignsManager, ListCampaignsManager

from django.db.models.signals import post_save

class DwClientes(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True)
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    domic_calle = models.CharField(max_length=50, blank=True, null=True)
    domic_numero = models.CharField(max_length=20, blank=True, null=True)
    domic_piso = models.CharField(max_length=20, blank=True, null=True)
    domic_dpto = models.CharField(max_length=20, blank=True, null=True)
    domic_cp = models.CharField(max_length=20, blank=True, null=True)
    domic_tipo = models.CharField(max_length=20, blank=True, null=True)
    domic_cod_prov = models.CharField(max_length=20, blank=True, null=True)
    domic_cpacp = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    dni = models.CharField(max_length=20, blank=True, null=True)
    cuitcuil = models.CharField(max_length=20, blank=True, null=True)
    codigo_nacionalidad = models.CharField(max_length=20, blank=True, null=True)
    codigo_ocupacion = models.CharField(max_length=20, blank=True, null=True)
    codigo_estadocivil = models.CharField(max_length=20, blank=True, null=True)
    domic_localidad = models.CharField(max_length=50, blank=True, null=True)
    onboarding = models.CharField(max_length=1, blank=True, null=True)
    tipo_baja = models.CharField(max_length=10, blank=True, null=True)
    fecha_preregistro = models.DateField(blank=True, null=True)
    id_user = models.CharField(max_length=100, blank=True, null=True)
    id_btclient = models.IntegerField(blank=True, null=True)
    demograficos = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    payroll = models.CharField(max_length=1, blank=True, null=True)
    cuit_empleador = models.CharField(max_length=11, blank=True, null=True)
    payroll_fecha_alta = models.DateField(blank=True, null=True)
    domic_geo_latitud = models.FloatField(blank=True, null=True)
    domic_geo_longitud = models.FloatField(blank=True, null=True)
    domic_geo_tipo = models.CharField(max_length=2, blank=True, null=True)
    ultima_acred_pay = models.DateField(blank=True, null=True)
    ultimo_cambio_txt = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_clientes'

        
class LkClasificacionCampanias(models.Model):
    id_clasificacion = models.IntegerField(primary_key=True)
    nombre_clasificacion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lk_clasificacion_campanias'


class LkClasificacionTracking(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lk_clasificacion_tracking'


class DwCampanias(models.Model):
    id_campania = models.BigAutoField(auto_created=True, primary_key=True)
    nombre_campania = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    canales = models.CharField(max_length=255, blank=True, null=True, default='[mail]', editable=False)
    vigencia_desde = models.DateField(blank=True, null=True)
    vigencia_hasta = models.DateField(blank=True, null=True)
    fecha_envio = models.DateTimeField(blank=True, null=True, editable=False)
    id_clasificacion = models.ForeignKey(LkClasificacionCampanias, models.CASCADE, db_column='id_clasificacion', blank=True, null=True)
    tracking_id = models.ForeignKey(LkClasificacionTracking, models.CASCADE, db_column='tracking_id',blank=True, null=True)
    istracked = models.BooleanField(blank=True, null=True)

    objects_list = ListCampaignsManager()
    objects_create = CreateCampaignsManager()

    class Meta:
        managed = False
        verbose_name = 'Campañas'
        verbose_name_plural = 'Campañas'
        ordering = ['-fecha_creacion']
        db_table = 'dw_campanias'


class DwCampaniaClienteCanal(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    id_campania = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True, default='[mail]')

    class Meta:
        managed = False
        db_table = 'dw_campania_cliente_canal'


class DwCampaniaClienteCanalGrupocontrol(models.Model):
    id_campania = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campania_cliente_canal_grupocontrol'


class DwBlackListGeneral(models.Model):
    id_cliente = models.ForeignKey(DwClientes, models.CASCADE, db_column='id_cliente', related_name='black_list',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_black_list_general'


class FileCSV(models.Model):
    file = models.FileField(upload_to='')


class DwTemp202206(models.Model):
    id_temp = models.BigAutoField(auto_created=True, primary_key=True)
    id_campania = models.BigIntegerField()
    id_cliente = models.BigIntegerField(blank=True, null=True)
    cuitcuil = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    monto = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_temp_202206'


class DwProcesosEtl(models.Model):
    id_proceso = models.AutoField(auto_created=True, primary_key=True)
    codigo_proceso = models.CharField(max_length=20, blank=True, null=True)
    nombre_proceso = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio_proceso = models.DateTimeField(blank=True, null=True)
    fecha_fin_proceso = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_procesos_etl'

    
class PgStatActivity(models.Model):
    datname = models.TextField(db_collation='C', blank=True, null=True)
    pid = models.IntegerField(primary_key=True, editable=False)
    client_addr = models.GenericIPAddressField(blank=True, null=True)
    query_start = models.DateTimeField(blank=True, null=True)
    state_change = models.DateTimeField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'pg_stat_activity'





