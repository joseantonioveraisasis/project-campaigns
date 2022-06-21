# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CampaignsFilecsv(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'campaigns_filecsv'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DwCampanias(models.Model):
    id_campania = models.BigAutoField()
    nombre_campania = models.CharField(max_length=255, blank=True, null=True)
    area_solicitud = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    canales = models.CharField(max_length=255, blank=True, null=True)
    segmentos = models.CharField(max_length=255, blank=True, null=True)
    flag_ca = models.IntegerField(blank=True, null=True)
    flag_pp = models.IntegerField(blank=True, null=True)
    flag_pf = models.IntegerField(blank=True, null=True)
    flag_pes = models.IntegerField(blank=True, null=True)
    flag_compracomercio = models.IntegerField(blank=True, null=True)
    flag_txn = models.IntegerField(blank=True, null=True)
    vigencia_desde = models.DateField(blank=True, null=True)
    vigencia_hasta = models.DateField(blank=True, null=True)
    imagen_pieza_sms = models.BinaryField(blank=True, null=True)
    imagen_pieza_mail = models.BinaryField(blank=True, null=True)
    imagen_pieza_facebook = models.BinaryField(blank=True, null=True)
    imagen_pieza_instagram = models.BinaryField(blank=True, null=True)
    imagen_pieza_otros = models.BinaryField(blank=True, null=True)
    texto_mensaje = models.TextField(blank=True, null=True)
    hook_cashback = models.CharField(max_length=255, blank=True, null=True)
    cant_leads = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_envio = models.DateTimeField(blank=True, null=True)
    asunto_newsletter = models.CharField(max_length=255, blank=True, null=True)
    respond_total = models.IntegerField(blank=True, null=True)
    respond_gc = models.IntegerField(blank=True, null=True)
    respond_read = models.IntegerField(blank=True, null=True)
    id_clasificacion = models.ForeignKey('LkClasificacionCampanias', models.DO_NOTHING, db_column='id_clasificacion', blank=True, null=True)
    tracking_id = models.IntegerField(blank=True, null=True)
    tracked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campanias'


class DwTemp202206(models.Model):
    id_temp = models.BigAutoField()
    id_campania = models.BigIntegerField()
    identificador = models.CharField(max_length=-1)
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
