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


class DwBlackListGeneral(models.Model):
    id_cliente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_black_list_general'


class DwCampaniaClienteCanal(models.Model):
    id_campania = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True)
    id = models.BigAutoField()

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
    istracked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campanias'


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


class DwProcesosEtl(models.Model):
    id_proceso = models.AutoField()
    codigo_proceso = models.CharField(max_length=20, blank=True, null=True)
    nombre_proceso = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio_proceso = models.DateTimeField(blank=True, null=True)
    fecha_fin_proceso = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_procesos_etl'


class DwTemp202206(models.Model):
    id_temp = models.BigAutoField()
    id_campania = models.BigIntegerField()
    id_cliente = models.BigIntegerField(blank=True, null=True)
    cuitcuil = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
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


class LkClasificacionTracking(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lk_clasificacion_tracking'


class PgStartActivito(models.Model):
    datid = models.TextField(blank=True, null=True)  # This field type is a guess.
    datname = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    pid = models.IntegerField(blank=True, null=True)
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
        db_table = 'pg_start_activito'
