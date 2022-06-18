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
from .managers import ListCampaignsManager, CreateCampaignsManager, ListCampaignsManager,SearchCampaignsManager

from django.db.models.signals import post_save

class DwTemp202206(models.Model):
    id_temp = models.BigAutoField(auto_created=True, primary_key=True)
    id_campania = models.BigIntegerField()
    cuitcuil = models.BigIntegerField()
    monto = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_temp_202206'
        

class LkClasificacionCampanias(models.Model):
    id_clasificacion = models.IntegerField(primary_key=True)
    nombre_clasificacion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lk_clasificacion_campanias'


class DwCampanias(models.Model):
    id_campania = models.BigAutoField(auto_created=True, primary_key=True)
    nombre_campania = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    canales = models.CharField(max_length=255, blank=True, null=True, default='[mail]', editable=False)
    vigencia_desde = models.DateField(blank=True, null=True)
    vigencia_hasta = models.DateField(blank=True, null=True)
    fecha_envio = models.DateTimeField(blank=True, null=True, editable=False)
    id_clasificacion = models.ForeignKey(LkClasificacionCampanias, models.CASCADE, db_column='id_clasificacion', blank=True, null=True)
    tracking_id = models.IntegerField(blank=True, null=True)
    tracked = models.BooleanField(blank=True, null=True)

    objects_list = ListCampaignsManager()
    objects_create = CreateCampaignsManager()
    objects_search = SearchCampaignsManager()

    class Meta:
        managed = False
        verbose_name = 'Campañas'
        verbose_name_plural = 'Campañas'
        ordering = ['-fecha_creacion']
        db_table = 'dw_campanias'


class FileCSV(models.Model):
    file = models.FileField(upload_to='')


class PgStatActivity(models.Model):
    datid = models.TextField(blank=True, null=True)  # This field type is a guess.
    datname = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    pid = models.IntegerField(primary_key=True, editable=False)
    leader_pid = models.IntegerField(blank=True, null=True)
    usesysid = models.TextField(blank=True, null=True)  # This field type is a guess.
    usename = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    application_name = models.TextField(blank=True, null=True)
    client_addr = models.GenericIPAddressField(blank=True, null=True)
    client_hostname = models.TextField(blank=True, null=True)
    client_port = models.IntegerField(blank=True, null=True)
    backend_start = models.DateTimeField(blank=True, null=True)
    xact_start = models.DateTimeField(blank=True, null=True)
    query_start = models.DateTimeField(blank=True, null=True)
    state_change = models.DateTimeField(blank=True, null=True)
    wait_event_type = models.TextField(blank=True, null=True)
    wait_event = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    backend_xid = models.TextField(blank=True, null=True)  # This field type is a guess.
    backend_xmin = models.TextField(blank=True, null=True)  # This field type is a guess.
    query_id = models.BigIntegerField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    backend_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_stat_activity'





