# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tabnanny import verbose
from django.db import models

#managers
from .managers import CampaignsManager,SearchCampaignsManager

class LkClasificacionCampanias(models.Model):
    id_clasificacion = models.IntegerField(primary_key=True)
    nombre_clasificacion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lk_clasificacion_campanias'


class DwCampanias(models.Model):
    id_campania = models.BigAutoField(auto_created=True, primary_key=True)
    nombre_campania = models.CharField(max_length=255, blank=True, null=True)
    area_solicitud = models.CharField(max_length=100, blank=True, null=True, editable=False)
    fecha_creacion = models.DateField(blank=True, null=True)
    canales = models.CharField(max_length=255, blank=True, null=True, default='[mail]', editable=False)
    segmentos = models.CharField(max_length=255, blank=True, null=True, editable=False)
    flag_ca = models.IntegerField(blank=True, null=True, editable=False)
    flag_pp = models.IntegerField(blank=True, null=True, editable=False)
    flag_pf = models.IntegerField(blank=True, null=True, editable=False)
    flag_pes = models.IntegerField(blank=True, null=True, editable=False)
    flag_compracomercio = models.IntegerField(blank=True, null=True, editable=False)
    flag_txn = models.IntegerField(blank=True, null=True, editable=False)
    vigencia_desde = models.DateField(blank=True, null=True)
    vigencia_hasta = models.DateField(blank=True, null=True)
    imagen_pieza_sms = models.BinaryField(blank=True, null=True, editable=False)
    imagen_pieza_mail = models.BinaryField(blank=True, null=True, editable=False)
    imagen_pieza_facebook = models.BinaryField(blank=True, null=True, editable=False)
    imagen_pieza_instagram = models.BinaryField(blank=True, null=True, editable=False)
    imagen_pieza_otros = models.BinaryField(blank=True, null=True, editable=False)
    texto_mensaje = models.TextField(blank=True, null=True, editable=False)
    hook_cashback = models.CharField(max_length=255, blank=True, null=True, editable=False)
    cant_leads = models.IntegerField(blank=True, null=True, editable=False)
    observaciones = models.TextField(blank=True, null=True, editable=False)
    fecha_envio = models.DateTimeField(blank=True, null=True, editable=False)
    asunto_newsletter = models.CharField(max_length=255, blank=True, null=True, editable=False)
    respond_total = models.IntegerField(blank=True, null=True, editable=False)
    respond_gc = models.IntegerField(blank=True, null=True, editable=False)
    respond_read = models.IntegerField(blank=True, null=True, editable=False)
    #id_clasificacion = models.IntegerField(blank=True, null=True)
    id_clasificacion = models.ForeignKey(LkClasificacionCampanias, models.DO_NOTHING, db_column='id_clasificacion', blank=True, null=True)

    objects = CampaignsManager()
    objects_search = SearchCampaignsManager()

    class Meta:
        managed = False
        verbose_name = 'Campañas'
        verbose_name_plural = 'Campañas'
        ordering = ['-fecha_creacion']
        db_table = 'dw_campanias'




