# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    userid = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    streetnumber = models.CharField(max_length=-1, blank=True, null=True)
    floor = models.CharField(max_length=-1, blank=True, null=True)
    apartment = models.CharField(max_length=-1, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=1100, blank=True, null=True)
    placeid = models.CharField(max_length=255, blank=True, null=True)
    addresstype = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    cpazipcode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class Appointments(models.Model):
    cardid = models.IntegerField(blank=True, null=True)
    userid = models.UUIDField(blank=True, null=True)
    trackingnumber = models.CharField(max_length=255, blank=True, null=True)
    creationdate = models.DateField(blank=True, null=True)
    eta = models.DateField(blank=True, null=True)
    currentstatus = models.IntegerField(blank=True, null=True)
    statuses = models.TextField(blank=True, null=True)  # This field type is a guess.
    addressid = models.CharField(max_length=50, blank=True, null=True)
    branchid = models.CharField(max_length=20, blank=True, null=True)
    servicetype = models.IntegerField(blank=True, null=True)
    sequencenumber = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'


class Aprobados202206(models.Model):
    cuitcuil = models.CharField(max_length=11, blank=True, null=True)
    monto = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aprobados_202206'


class Bcra3500(models.Model):
    fecha = models.DateField(primary_key=True)
    tipo_cambio = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bcra3500'


class BtClienteOnboarding(models.Model):
    onboarding_date = models.DateField(blank=True, null=True)
    id_cliente = models.BigIntegerField(blank=True, null=True)
    q_open = models.BigIntegerField(blank=True, null=True)
    q_not_open = models.BigIntegerField(blank=True, null=True)
    q_email = models.BigIntegerField(blank=True, null=True)
    open_days = models.DurationField(blank=True, null=True)
    segmento_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bt_cliente_onboarding'


class BtDetailsOnboarding(models.Model):
    send_date = models.DateField(blank=True, null=True)
    onboarding_date = models.DateField(blank=True, null=True)
    id_evento = models.SmallIntegerField(blank=True, null=True)
    id_resultado = models.SmallIntegerField(blank=True, null=True)
    q_cliente = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bt_details_onboarding'


class BtOnboarding(models.Model):
    onboarding_date = models.DateField(blank=True, null=True)
    send_date = models.DateField(blank=True, null=True)
    open_date = models.DateField(blank=True, null=True)
    id_evento = models.SmallIntegerField(blank=True, null=True)
    id_resultado = models.SmallIntegerField(blank=True, null=True)
    q_email = models.BigIntegerField(blank=True, null=True)
    open_days = models.DurationField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bt_onboarding'


class Btsic00(models.Model):
    btsic00id = models.DecimalField(max_digits=10, decimal_places=0)
    btsic00emp = models.SmallIntegerField(blank=True, null=True)
    btsic00cta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'btsic00'


class BusinessDecidirInformation(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    business_id = models.TextField(blank=True, null=True)
    site_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_decidir_information'


class BusinessPrismaEstablishmentInformation(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    merchant_id = models.BigIntegerField(blank=True, null=True)
    net_establishment_id = models.BigIntegerField(blank=True, null=True)
    establishment_type = models.TextField(blank=True, null=True)
    payment_method = models.BigIntegerField(blank=True, null=True)
    virtual_terminals = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_prisma_establishment_information'


class BusinessPrismaMerchantInformation(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    business_id = models.TextField(blank=True, null=True)
    application_id = models.TextField(blank=True, null=True)
    message_state_id = models.TextField(blank=True, null=True)
    net_merchant_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_prisma_merchant_information'


class BusinessPrismaTerminalInformation(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    merchant_id = models.BigIntegerField(blank=True, null=True)
    terminal_number = models.TextField(blank=True, null=True)
    plan_type_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_prisma_terminal_information'


class BusinessTaxCondition(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    business_id = models.TextField(blank=True, null=True)
    iva_condition = models.TextField(blank=True, null=True)
    gross_income_register_number = models.TextField(blank=True, null=True)
    gross_income_category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_tax_condition'


class Businesses(models.Model):
    id = models.TextField(blank=True, null=True)
    user_id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    avatar_id = models.TextField(blank=True, null=True)
    business_category = models.IntegerField(blank=True, null=True)
    has_pos_terminal = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'businesses'


class BusinessesAddresses(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    business_id = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    street_number = models.TextField(blank=True, null=True)
    floor = models.TextField(blank=True, null=True)
    apartment = models.TextField(blank=True, null=True)
    zip_code = models.TextField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    address_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'businesses_addresses'


class Companies(models.Model):
    id = models.UUIDField()
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    alias = models.CharField(max_length=-1, blank=True, null=True)
    coverid = models.UUIDField(blank=True, null=True)
    modidate = models.DateField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    hidetouser = models.BooleanField(blank=True, null=True)
    locations = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Deletedusers(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    reviewfields = models.TextField(blank=True, null=True)
    btclientid = models.CharField(max_length=255, blank=True, null=True)
    supportid = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.CharField(max_length=255, blank=True, null=True)
    iid = models.CharField(max_length=255, blank=True, null=True)
    phrase = models.CharField(max_length=255, blank=True, null=True)
    btclientnumber = models.CharField(max_length=255, blank=True, null=True)
    internationaldefaultaccount = models.CharField(max_length=255, blank=True, null=True)
    settings = models.CharField(max_length=255, blank=True, null=True)
    activatedat = models.CharField(max_length=255, blank=True, null=True)
    sponsorid = models.CharField(max_length=255, blank=True, null=True)
    limited = models.CharField(max_length=255, blank=True, null=True)
    netidtype = models.CharField(max_length=255, blank=True, null=True)
    netenabled = models.CharField(max_length=255, blank=True, null=True)
    salt = models.TextField(blank=True, null=True)
    preregisterdate = models.CharField(max_length=255, blank=True, null=True)
    netenableddate = models.CharField(max_length=255, blank=True, null=True)
    lastsessiondate = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deletedusers'


class DlEvaluations(models.Model):
    id = models.CharField(max_length=-1, blank=True, null=True)
    userid = models.CharField(max_length=-1, blank=True, null=True)
    cuit = models.CharField(max_length=-1, blank=True, null=True)
    score = models.CharField(max_length=-1, blank=True, null=True)
    risklevel = models.CharField(max_length=-1, blank=True, null=True)
    riskscore = models.CharField(max_length=-1, blank=True, null=True)
    incomelevel = models.CharField(max_length=-1, blank=True, null=True)
    computedincome = models.CharField(max_length=-1, blank=True, null=True)
    interestrateslateregularloan = models.CharField(max_length=-1, blank=True, null=True)
    duedate = models.DateTimeField(blank=True, null=True)
    creationdate = models.DateTimeField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    isoriginal = models.BooleanField(blank=True, null=True)
    confirmed = models.BooleanField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=-1, blank=True, null=True)
    interestrateslatepatear = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dl_evaluations'


class DlFuenteComisiones(models.Model):
    hrubro = models.BigIntegerField(blank=True, null=True)
    hcmod = models.IntegerField(blank=True, null=True)
    htran = models.IntegerField(blank=True, null=True)
    hnrel = models.IntegerField(blank=True, null=True)
    hfcon = models.DateTimeField(blank=True, null=True)
    hfval = models.DateTimeField(blank=True, null=True)
    hcord = models.IntegerField(blank=True, null=True)
    hcta = models.IntegerField(blank=True, null=True)
    hmda = models.IntegerField(blank=True, null=True)
    hcimp1 = models.FloatField(blank=True, null=True)
    hcodmo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dl_fuente_comisiones'


class DlInteresesAcumulados(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    id_producto = models.IntegerField(blank=True, null=True)
    producto = models.CharField(max_length=-1, blank=True, null=True)
    moneda = models.CharField(max_length=-1, blank=True, null=True)
    intereses = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dl_intereses_acumulados'


class DlMensualFsh021Resumen(models.Model):
    sbfech = models.DateField(blank=True, null=True)
    sbmod = models.IntegerField(blank=True, null=True)
    sbmda = models.IntegerField(blank=True, null=True)
    sbcta = models.IntegerField(blank=True, null=True)
    sbsdo_eop = models.FloatField(blank=True, null=True)
    sbsdo_avg = models.FloatField(blank=True, null=True)
    sbccre = models.IntegerField(blank=True, null=True)
    sbcdeb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dl_mensual_fsh021_resumen'


class DlMovimientosDetalle(models.Model):
    fecha = models.DateField(blank=True, null=True)
    fecha_valor = models.DateField(blank=True, null=True)
    hcmod = models.IntegerField(blank=True, null=True)
    hcmod_name = models.CharField(max_length=-1, blank=True, null=True)
    htran = models.IntegerField(blank=True, null=True)
    htran_name = models.CharField(max_length=-1, blank=True, null=True)
    id_transaccion = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    hcord = models.IntegerField(blank=True, null=True)
    hcord_name = models.CharField(max_length=-1, blank=True, null=True)
    hcmcod = models.IntegerField(blank=True, null=True)
    tipo_transac = models.CharField(max_length=-1, blank=True, null=True)
    hcord_tipo = models.CharField(max_length=-1, blank=True, null=True)
    hcsubo = models.IntegerField(blank=True, null=True)
    htoper = models.IntegerField(blank=True, null=True)
    hrubro = models.FloatField(blank=True, null=True)
    rubro = models.CharField(max_length=-1, blank=True, null=True)
    moneda = models.CharField(max_length=-1, blank=True, null=True)
    tipocambio = models.FloatField(blank=True, null=True)
    hctcbi1 = models.FloatField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    hcodmo = models.IntegerField(blank=True, null=True)
    hcref = models.CharField(max_length=-1, blank=True, null=True)
    rubro_comercio = models.CharField(max_length=-1, blank=True, null=True)
    id_comercio = models.CharField(max_length=-1, blank=True, null=True)
    nombre_comercio = models.CharField(max_length=-1, blank=True, null=True)
    cuil_transf_entrante = models.CharField(max_length=-1, blank=True, null=True)
    banco_transf_entrante = models.CharField(max_length=-1, blank=True, null=True)
    cuil_transf_saliente = models.CharField(max_length=-1, blank=True, null=True)
    banco_transf_saliente = models.CharField(max_length=-1, blank=True, null=True)
    pes = models.CharField(max_length=-1, blank=True, null=True)
    pes_descripcion = models.CharField(max_length=-1, blank=True, null=True)
    id_rubro_consumo = models.IntegerField(blank=True, null=True)
    rubro_consumo = models.CharField(max_length=40, blank=True, null=True)
    fecha_hora_consumo = models.DateTimeField(blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dl_movimientos_detalle'


class DlMovimientosDetallePr(models.Model):
    fecha = models.DateField(blank=True, null=True)
    fecha_valor = models.DateField(blank=True, null=True)
    hcmod = models.IntegerField(blank=True, null=True)
    hcmod_name = models.CharField(max_length=-1, blank=True, null=True)
    htran = models.IntegerField(blank=True, null=True)
    htran_name = models.CharField(max_length=-1, blank=True, null=True)
    id_transaccion = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    hcord = models.IntegerField(blank=True, null=True)
    hcord_name = models.CharField(max_length=-1, blank=True, null=True)
    hcmcod = models.IntegerField(blank=True, null=True)
    tipo_transac = models.CharField(max_length=-1, blank=True, null=True)
    hcord_tipo = models.CharField(max_length=-1, blank=True, null=True)
    hcsubo = models.IntegerField(blank=True, null=True)
    htoper = models.IntegerField(blank=True, null=True)
    hrubro = models.FloatField(blank=True, null=True)
    rubro = models.CharField(max_length=-1, blank=True, null=True)
    moneda = models.CharField(max_length=-1, blank=True, null=True)
    tipocambio = models.FloatField(blank=True, null=True)
    hctcbi1 = models.FloatField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    hcodmo = models.IntegerField(blank=True, null=True)
    hcref = models.CharField(max_length=-1, blank=True, null=True)
    rubro_comercio = models.CharField(max_length=-1, blank=True, null=True)
    id_comercio = models.CharField(max_length=-1, blank=True, null=True)
    nombre_comercio = models.CharField(max_length=-1, blank=True, null=True)
    cuil_transf_entrante = models.CharField(max_length=-1, blank=True, null=True)
    banco_transf_entrante = models.CharField(max_length=-1, blank=True, null=True)
    cuil_transf_saliente = models.CharField(max_length=-1, blank=True, null=True)
    banco_transf_saliente = models.CharField(max_length=-1, blank=True, null=True)
    pes = models.CharField(max_length=-1, blank=True, null=True)
    pes_descripcion = models.CharField(max_length=-1, blank=True, null=True)
    id_rubro_consumo = models.IntegerField(blank=True, null=True)
    rubro_consumo = models.CharField(max_length=40, blank=True, null=True)
    fecha_hora_consumo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dl_movimientos_detalle_pr'


class DwAcreditacionesPayroll(models.Model):
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_acreditaciones_payroll'


class DwActivos180(models.Model):
    periodo = models.DateField(blank=True, null=True)
    activos_180 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_activos180'


class DwBeneficiariosCampanias(models.Model):
    id_cliente = models.IntegerField(blank=True, null=True)
    id_campania = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_beneficiarios_campanias'


class DwBlackList(models.Model):
    fecha_proceso = models.DateField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    tipo_black_list = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_black_list'


class DwBlackListGeneral(models.Model):
    id_cliente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_black_list_general'


class DwCalendario(models.Model):
    periodo = models.DateField(blank=True, null=True)
    fecha = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dw_calendario'


class DwCampaniaAuxiliar(models.Model):
    id_cliente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campania_auxiliar'


class DwCampaniaAuxiliar2(models.Model):
    id_cliente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campania_auxiliar_2'


class DwCampaniaClienteCanal(models.Model):
    id_campania = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campania_cliente_canal'


class DwCampaniaClienteCanalBackup(models.Model):
    id_campania = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campania_cliente_canal_backup'


class DwCampaniaClienteCanalGrupocontrol(models.Model):
    id_campania = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campania_cliente_canal_grupocontrol'


class DwCampaniaClienteCanalGrupocontrolBackup(models.Model):
    id_campania = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campania_cliente_canal_grupocontrol_backup'


class DwCampaniaTracking(models.Model):
    id_campania = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True)
    id_resultado = models.IntegerField(blank=True, null=True)
    fecha_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campania_tracking'


class DwCampaniaTrackingBackup(models.Model):
    id_campania = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    canal = models.CharField(max_length=50, blank=True, null=True)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    id_resultado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campania_tracking_backup'


class DwCampanias(models.Model):
    id_campania = models.BigAutoField(blank=True, null=True)
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
    id_clasificacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campanias'

    def __str__(self):
        return self.nombre_campania


class DwCampaniasBackup(models.Model):
    id_campania = models.BigIntegerField(blank=True, null=True)
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
    id_clasificacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campanias_backup'


class DwCampaniasImagen(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    nombre_archivo = models.CharField(max_length=100, blank=True, null=True)
    descrip_camp = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True)
    fecha_version = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_campanias_imagen'


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


class DwClientesDecilRentabilidad(models.Model):
    id_cliente = models.IntegerField()
    periodo = models.DateField()
    decil = models.IntegerField(blank=True, null=True)
    sumaingresos = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_clientes_decil_rentabilidad'


class DwClientesOfertaPatear(models.Model):
    id_cliente = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_clientes_oferta_patear'


class DwClientesOfertaPrestamos(models.Model):
    id_cliente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_clientes_oferta_prestamos'


class DwClientesStock(models.Model):
    periodo = models.DateField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    altas = models.IntegerField(blank=True, null=True)
    bajas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_clientes_stock'


class DwCustomer360(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    periodo = models.DateField()
    producto = models.CharField(max_length=10)
    moneda = models.CharField(max_length=10)
    saldo_eop = models.FloatField(blank=True, null=True)
    saldo_avg = models.FloatField(blank=True, null=True)
    mov_1m = models.IntegerField(blank=True, null=True)
    mov_3m = models.IntegerField(blank=True, null=True)
    open_date = models.DateField(blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    mob = models.IntegerField(blank=True, null=True)
    mov_opd = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    id_producto = models.BigIntegerField()
    cuotas = models.IntegerField(blank=True, null=True)
    saldo_eop_2 = models.FloatField(blank=True, null=True)
    saldo_avg_2 = models.FloatField(blank=True, null=True)
    decil = models.IntegerField(blank=True, null=True)
    tasa = models.FloatField(blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    fx_v_p = models.FloatField(blank=True, null=True)
    fx_v_u = models.FloatField(blank=True, null=True)
    fx_c = models.IntegerField(blank=True, null=True)
    dep_pf_v = models.FloatField(blank=True, null=True)
    dep_pf_c = models.IntegerField(blank=True, null=True)
    ext_pf_v = models.FloatField(blank=True, null=True)
    ext_pf_c = models.IntegerField(blank=True, null=True)
    p_intb_v = models.FloatField(blank=True, null=True)
    p_intb_c = models.IntegerField(blank=True, null=True)
    pes_v = models.FloatField(blank=True, null=True)
    pes_c = models.IntegerField(blank=True, null=True)
    pf_a_v = models.FloatField(blank=True, null=True)
    pf_a_c = models.IntegerField(blank=True, null=True)
    pf_au_v = models.FloatField(blank=True, null=True)
    pf_au_c = models.IntegerField(blank=True, null=True)
    pf_aup_v = models.FloatField(blank=True, null=True)
    pp_a_v = models.FloatField(blank=True, null=True)
    pp_a_c = models.IntegerField(blank=True, null=True)
    pp_p_v = models.FloatField(blank=True, null=True)
    pp_p_c = models.IntegerField(blank=True, null=True)
    pp_r_v = models.FloatField(blank=True, null=True)
    pp_r_c = models.IntegerField(blank=True, null=True)
    td_cc_v = models.FloatField(blank=True, null=True)
    td_cc_c = models.IntegerField(blank=True, null=True)
    td_cec_v = models.FloatField(blank=True, null=True)
    td_cec_c = models.IntegerField(blank=True, null=True)
    td_debin_v = models.FloatField(blank=True, null=True)
    td_debin_c = models.IntegerField(blank=True, null=True)
    td_atm_v = models.FloatField(blank=True, null=True)
    td_atm_c = models.IntegerField(blank=True, null=True)
    tr_bru_v = models.FloatField(blank=True, null=True)
    tr_bru_c = models.IntegerField(blank=True, null=True)
    tr_bru_u_v = models.FloatField(blank=True, null=True)
    tr_bru_u_c = models.IntegerField(blank=True, null=True)
    tr_bru_up_v = models.FloatField(blank=True, null=True)
    tr_3_v = models.FloatField(blank=True, null=True)
    tr_3_c = models.IntegerField(blank=True, null=True)
    tr_3_u_v = models.FloatField(blank=True, null=True)
    tr_3_u_c = models.IntegerField(blank=True, null=True)
    tr_3_up_v = models.FloatField(blank=True, null=True)
    tr_obmt_v = models.FloatField(blank=True, null=True)
    tr_obmt_c = models.IntegerField(blank=True, null=True)
    tr_obmt_u_v = models.FloatField(blank=True, null=True)
    tr_obmt_u_c = models.IntegerField(blank=True, null=True)
    tr_obmt_up_v = models.FloatField(blank=True, null=True)
    td_cce_v = models.FloatField(blank=True, null=True)
    td_cce_c = models.IntegerField(blank=True, null=True)
    td_cceu_v = models.FloatField(blank=True, null=True)
    td_cceu_c = models.IntegerField(blank=True, null=True)
    td_cceup_v = models.FloatField(blank=True, null=True)
    td_debinu_v = models.FloatField(blank=True, null=True)
    td_debinu_c = models.IntegerField(blank=True, null=True)
    td_debinup_v = models.FloatField(blank=True, null=True)
    p_intbu_v = models.FloatField(blank=True, null=True)
    p_intbu_c = models.IntegerField(blank=True, null=True)
    p_intbup_v = models.FloatField(blank=True, null=True)
    new_loan_volume = models.FloatField(blank=True, null=True)
    dep_atm_c = models.IntegerField(blank=True, null=True)
    dep_atm_v = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_customer360'
        unique_together = (('id_cliente', 'periodo', 'producto', 'moneda', 'id_producto'),)


class DwDiarioClientesActivos(models.Model):
    fecha = models.DateField(blank=True, null=True)
    cant_clientes_activos = models.IntegerField(blank=True, null=True)
    nuevos_activos = models.IntegerField(blank=True, null=True)
    nuevos_activos_acum = models.IntegerField(blank=True, null=True)
    activos_acum = models.IntegerField(blank=True, null=True)
    fx_acum = models.IntegerField(blank=True, null=True)
    fx_diario = models.IntegerField(blank=True, null=True)
    activos_diario = models.IntegerField(blank=True, null=True)
    cl_consumo_diario = models.IntegerField(blank=True, null=True)
    cl_consumo_acum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_diario_clientes_activos'


class DwDiarioFx(models.Model):
    periodo = models.DateField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    cant_compra_usd = models.IntegerField(blank=True, null=True)
    tot_deb_pesos = models.FloatField(blank=True, null=True)
    tot_cred_usd = models.FloatField(blank=True, null=True)
    cant_venta_usd = models.IntegerField(blank=True, null=True)
    tot_deb_usd = models.FloatField(blank=True, null=True)
    tot_cred_pesos = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_diario_fx'


class DwDiarioTransacResumen(models.Model):
    fecha = models.DateField(blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    transaccion = models.CharField(max_length=50, blank=True, null=True)
    cant_transacciones = models.IntegerField(blank=True, null=True)
    monto_pesos = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_diario_transac_resumen'


class DwEnvioCampaniasOnbInactivos(models.Model):
    fecha = models.DateField(primary_key=True)
    nro_envio = models.SmallIntegerField()
    id_campania = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    cant_reg = models.IntegerField(blank=True, null=True)
    fecha_archivo = models.DateTimeField(blank=True, null=True)
    id = models.AutoField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_envio_campanias_onb_inactivos'
        unique_together = (('fecha', 'nro_envio'),)


class DwEvaluationsAbr21(models.Model):
    cuil = models.CharField(max_length=11, blank=True, null=True)
    predictor_ingresos = models.CharField(max_length=3, blank=True, null=True)
    banco_actual = models.CharField(max_length=70, blank=True, null=True)
    situacion_max_actual = models.IntegerField(blank=True, null=True)
    deuda_max_actual = models.FloatField(blank=True, null=True)
    banco_ult_12m = models.CharField(max_length=70, blank=True, null=True)
    situacion_max_ult_12m = models.IntegerField(blank=True, null=True)
    deuda_max_ult_12m = models.FloatField(blank=True, null=True)
    fecha_ult_12m = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_evaluations_abr21'


class DwEvaluationsFinal(models.Model):
    id_cliente = models.BigIntegerField(blank=True, null=True)
    incomelevel = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_evaluations_final'


class DwFsd011Temp(models.Model):
    id_cliente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_fsd011_temp'


class DwFx(models.Model):
    fecha = models.DateField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    id_transaccion = models.IntegerField(blank=True, null=True)
    cta_deb_moneda = models.CharField(max_length=10, blank=True, null=True)
    cta_deb_monto = models.FloatField(blank=True, null=True)
    cta_cred_moneda = models.CharField(max_length=10, blank=True, null=True)
    cta_cred_monto = models.FloatField(blank=True, null=True)
    tipocambio = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_fx'


