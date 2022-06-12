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
from .managers import CampaignsManager, CreateCampaignsManager,SearchCampaignsManager

from django.db.models.signals import post_save

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
    file = models.ImageField(upload_to='')

    objects_create = CreateCampaignsManager()
    objects_search = SearchCampaignsManager()

    class Meta:
        managed = False
        verbose_name = 'Campañas'
        verbose_name_plural = 'Campañas'
        ordering = ['-fecha_creacion']
        db_table = 'dw_campanias'

    def __str__(self):
        print('***********************')
        print(self.vigencia_desde)


class FileCSV(models.Model):
    file = models.FileField(upload_to='')

def optimize_image(sender, instance, **kwargs):
    print('################################')
    print(instance)

post_save.connect(optimize_image,sender=DwCampanias)




