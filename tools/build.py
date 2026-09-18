#!/usr/bin/env python3
"""
Genera index.html y las páginas por servicio a partir de los datos de abajo.
Todas las páginas comparten assets/estilos.css y assets/app.js.

    python3 tools/build.py

Todo el contenido editable vive en este archivo, arriba de todo. Cambiá los
datos y volvé a correrlo: el HTML se regenera y queda consistente entre
páginas. Editar el HTML a mano funciona, pero el próximo build lo pisa.
"""
import os, html
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPRITE = open(os.path.join(RAIZ, 'tools/_sprite.html'), encoding='utf-8').read()

DOMINIO = 'https://familab.com.py'          # cambiar cuando se confirme el dominio

# --------------------------------------------------------------- contacto ----
TEL1, TEL1_VIS = '595995371105', '0995 371 105'      # Coronel Bogado
TEL2, TEL2_VIS = '595992995397', '0992 995 397'      # Carmen del Paraná

# Coordenadas de la sede central: decodificadas del código plus RQJ8+5JC
# (5845RQJ8+5J) que envió FamiLab. Las de Carmen del Paraná todavía no están
# confirmadas, por eso ese mapa se arma con la dirección.
LAT1, LNG1 = '-27.169587', '-56.233484'

SEDES = [
    dict(
        slug='coronel-bogado', nombre='Coronel Bogado', rol='Sede central',
        dir='Encarnación y Tacuary', ref='Esquina del Hospital Distrital de Coronel Bogado',
        ciudad='Coronel Bogado, Itapúa', cp='070803',
        tel=TEL1, tel_vis=TEL1_VIS,
        mapa='-27.169587,-56.233484 (Laboratorio FamiLab)',
        maps_link='https://www.google.com/maps/search/?api=1&query=-27.169587%2C-56.233484',
        ruta='https://www.google.com/maps/dir/?api=1&destination=-27.169587%2C-56.233484',
        horarios=['Lunes a viernes de 06:00 a 21:00 hs',
                  'Sábados de 06:00 a 18:00 hs',
                  'Domingos de 07:00 a 12:00 hs'],
        urgencias='Urgencias fuera del horario: a partir de las 21:00 hs, al llamado telefónico.',
        responsable='Bqco. Mgtr. Oscar Manuel Alvarez Duarte',
    ),
    dict(
        slug='carmen-del-parana', nombre='Carmen del Paraná', rol='Sucursal desde 2020',
        dir='Gral. Díaz entre Alberdi y Colón', ref='Frente al IPS de Carmen del Paraná',
        ciudad='Carmen del Paraná, Itapúa', cp='070701',
        tel=TEL2, tel_vis=TEL2_VIS,
        mapa='Gral. Díaz 644, Carmen del Paraná 070701, Paraguay (Laboratorio FamiLab)',
        maps_link='https://www.google.com/maps/search/?api=1&query=' +
                  quote('Gral. Díaz 644, Carmen del Paraná 070701, Paraguay', safe=''),
        ruta='https://www.google.com/maps/dir/?api=1&destination=' +
             quote('Gral. Díaz 644, Carmen del Paraná 070701, Paraguay', safe=''),
        horarios=['Lunes a viernes de 06:30 a 11:00 y de 13:00 a 15:00 hs',
                  'Sábados de 06:00 a 12:00 hs'],
        urgencias='Urgencias fuera del horario: al llamado telefónico.',
        responsable='Bqca. Sandra Avalos',
    ),
]

def wa(msg, tel=TEL1):
    return 'https://wa.me/%s?text=%s' % (tel, quote('Hola, %s' % msg, safe=''))

def e(t):
    return html.escape(t, quote=True)

PRESUPUESTO = 'quiero un presupuesto. Les mando la foto de mi pedido médico.'

# --------------------------------------------------------------- servicios ----
SERVICIOS = [
    dict(slug='analisis-de-rutina', nombre='Análisis de rutina', icono='i-tube',
         resumen='Hemograma, glicemia, perfil lipídico, orina simple y el resto de los estudios de control. La mayoría entrega resultados en el día.',
         titulo='Análisis clínicos de rutina en Coronel Bogado y Carmen del Paraná',
         intro='Los estudios de control que pide el médico en la consulta: hemograma, glicemia, '
               'perfil lipídico, función renal, función hepática, orina simple y materia fecal.',
         incluye=['Hemograma completo', 'Glicemia y curva de tolerancia', 'Perfil lipídico (colesterol y triglicéridos)',
                  'Urea, creatinina y ácido úrico', 'Perfil hepático', 'Orina simple y urocultivo', 'Parasitológico de materia fecal'],
         prep='La mayoría de los análisis de rutina se toman con 8 a 10 horas de ayuno. '
              'Si el pedido incluye algún estudio con preparación especial, te lo indicamos antes de venir.',
         tiempo='La mayoría de las determinaciones de rutina están el mismo día.'),

    dict(slug='analisis-hormonales', nombre='Análisis hormonales', icono='i-hormone',
         resumen='Perfil tiroideo, hormonas de fertilidad y control endocrinológico. Varios dependen del día del ciclo menstrual.',
         titulo='Análisis hormonales y estudios endocrinológicos',
         intro='Estudios hormonales que en la zona no siempre se consiguen: perfil tiroideo, hormonas '
               'reproductivas y controles endocrinológicos indicados por el especialista.',
         incluye=['Perfil tiroideo (TSH, T3, T4)', 'Hormonas reproductivas y de fertilidad',
                  'Control endocrinológico indicado por el especialista', 'Estudios de seguimiento de tratamiento hormonal'],
         prep='Varias hormonas se toman en un día determinado del ciclo menstrual y otras necesitan un '
              'horario específico de extracción. Mandanos la foto del pedido y te decimos qué día y a qué hora venir.',
         tiempo='El plazo depende del estudio: te lo confirmamos cuando armamos el presupuesto.'),

    dict(slug='analisis-microbiologicos', nombre='Análisis microbiológicos', icono='i-micro',
         resumen='Cultivos y antibiogramas: urocultivo, coprocultivo, exudados y las muestras que el hospital deriva.',
         titulo='Análisis microbiológicos: cultivos y antibiogramas',
         intro='Cultivos con antibiograma para identificar el germen y saber a qué antibiótico responde. '
               'Es una de las áreas por las que más nos derivan pacientes.',
         incluye=['Urocultivo con antibiograma', 'Coprocultivo', 'Cultivo de exudados y secreciones',
                  'Cultivo de otras muestras según el pedido médico'],
         prep='Cada cultivo tiene su forma de tomar la muestra. Escribinos antes de venir: te explicamos '
              'cómo recolectarla o te indicamos que la tomemos nosotros en el laboratorio.',
         tiempo='Los cultivos necesitan días de incubación. Te damos la fecha exacta al recibir la muestra.'),

    dict(slug='analisis-de-urgencia', nombre='Análisis de urgencia', icono='i-alert',
         resumen='Estudios que no pueden esperar, también fuera del horario de atención y para pacientes internados.',
         titulo='Análisis clínicos de urgencia en Coronel Bogado y Carmen del Paraná',
         intro='Procesamos estudios de urgencia dentro del horario y también fuera de él, al llamado. '
               'Atendemos pedidos de guardia, de consultorio y de pacientes internados.',
         incluye=['Estudios de urgencia dentro del horario de atención',
                  'Atención al llamado fuera del horario, en ambas sedes',
                  'Análisis de pacientes internados',
                  'Estudios derivados desde urgencias y pediatría'],
         prep='En una urgencia no esperes: llamá directamente al número de la sede más cercana y decinos '
              'qué estudio pide el médico.',
         tiempo='Los estudios de urgencia se procesan de inmediato.'),

    dict(slug='extraccion-a-domicilio', nombre='Extracción a domicilio', icono='i-home',
         resumen='Vamos a tu casa a tomar la muestra. Casco urbano, compañías y zonas rurales, con coordinación previa.',
         titulo='Extracción de muestras a domicilio',
         intro='Si no podés trasladarte, vamos a tu casa a tomar la muestra. El servicio cubre el casco '
               'urbano de Coronel Bogado y Carmen del Paraná, las compañías y las zonas rurales cercanas.',
         incluye=['Pacientes con dificultad para movilizarse', 'Adultos mayores',
                  'Pacientes en reposo o en recuperación', 'Grupos familiares en una misma visita',
                  'Compañías y zonas alejadas del casco urbano, coordinando el día'],
         prep='Escribinos por WhatsApp con tu ubicación y la foto del pedido médico. Te confirmamos el '
              'horario y qué preparación necesita cada estudio. Salimos a partir de las 07:00 hs.',
         tiempo='Costo del traslado: 15.000 Gs dentro del casco urbano. Fuera del casco urbano se calcula '
                'por distancia y te lo confirmamos antes de salir.',
         nota='Casi todos los estudios pueden tomarse a domicilio. Las excepciones son las muestras que '
              'necesitan procesarse de inmediato y no resisten el traslado desde zonas alejadas: en ese caso '
              'te lo decimos al momento de coordinar.'),

    dict(slug='chequeos-preventivos', nombre='Chequeos preventivos', icono='i-shield',
         resumen='Controles periódicos aunque no tengas síntomas. Si no tenés pedido médico, te orientamos con los estudios básicos.',
         titulo='Chequeos preventivos y controles periódicos',
         intro='Controlarse una vez al año detecta a tiempo lo que todavía no da síntomas: glicemia, '
               'colesterol, función renal, tiroides y hemograma.',
         incluye=['Control anual de adultos', 'Control de glicemia y colesterol',
                  'Control de función renal y hepática', 'Perfil tiroideo',
                  'Seguimiento de pacientes con diabetes o hipertensión'],
         prep='El chequeo básico se hace con 8 a 10 horas de ayuno. Si no tenés pedido médico, escribinos '
              'y te orientamos sobre los estudios de control más habituales.',
         tiempo='La mayoría de los estudios del chequeo básico se entregan el mismo día.'),

    dict(slug='analisis-ocupacionales', nombre='Análisis ocupacionales', icono='i-briefcase',
         resumen='Estudios para ingreso y control periódico de personal, con convenios para empresas de la zona.',
         titulo='Análisis ocupacionales para empresas',
         intro='Estudios preocupacionales y de control periódico para el personal de tu empresa, '
               'coordinados en una sola visita y con los resultados agrupados.',
         incluye=['Estudios de ingreso de personal', 'Controles periódicos del plantel',
                  'Coordinación de grupos en una misma jornada', 'Extracción en el lugar de trabajo, a coordinar'],
         prep='Escribinos indicando cuántas personas son y qué estudios autoriza la empresa. Coordinamos '
              'la jornada y te pasamos el presupuesto.',
         tiempo='Los plazos se acuerdan según la cantidad de personas y los estudios solicitados.'),
]
SERV_POR_SLUG = {s['slug']: s for s in SERVICIOS}

# ------------------------------------------------------------------ motivos ----
MOTIVOS = [
    ('i-camera',  'Tengo un pedido médico',        'tengo un pedido médico y quiero el presupuesto. Les mando la foto.'),
    ('i-money',   'Quiero saber el precio',        'quiero saber el precio de un análisis.'),
    ('i-no-food', '¿Tengo que venir en ayunas?',   'quiero saber si tengo que venir en ayunas.'),
    ('i-doc-check','¿Cuándo están mis resultados?','quiero consultar por mis resultados.'),
    ('i-home',    'Extracción a domicilio',        'quiero una extracción a domicilio. Mi ubicación es:'),
    ('i-alert',   'Análisis de urgencia',          'necesito un análisis de urgencia.'),
    ('i-shield',  'Trabajan con mi seguro',        'quiero saber si trabajan con mi seguro médico.'),
    ('i-briefcase','Análisis para el trabajo',     'necesito análisis ocupacionales para mi empresa.'),
    ('i-search',  'No sé qué estudio necesito',    'no sé qué estudio necesito. ¿Me orientan?'),
]

# ------------------------------------------------------------------- equipo ----
EQUIPO = [
    dict(nombre='Bqco. Mgtr. Oscar Manuel Alvarez Duarte', rol='Dirección técnica',
         reg='Reg. Prof. 1707 · Egresado de la Universidad Nacional de Misiones (UNaM, Argentina)', icono='i-flask'),
    dict(nombre='Bqca. Sirley Karina Cubilla Surnyak', rol='Bioquímica clínica',
         reg='Reg. Prof. 3133 · Especialista en Bioquímica Clínica, Universidad del Norte', icono='i-micro'),
    dict(nombre='Bqca. Luján Ferreira', rol='Bioquímica de planta',
         reg='Reg. Prof. 4997', icono='i-tube'),
    dict(nombre='Bqca. Sandra Avalos', rol='Responsable de la sede Carmen del Paraná',
         reg='Reg. Prof. 5132', icono='i-tubes'),
    dict(nombre='Tec. Ramón Solís', rol='Técnico en enfermería',
         reg='Reg. Prof. 18573', icono='i-syringe'),
]

SEGUROS = ['Medilife', 'Salud Protegida', 'SPS', 'Fleming', 'Comedi']
PAGOS = ['Efectivo', 'Transferencia bancaria', 'Pago con QR', 'Tarjetas de crédito', 'POS']

# ---------------------------------------------------------------- preparación ----
PREPARACION = [
    ('i-no-food', 'Ayuno de 8 a 10 horas',
     'Lo necesita la mayoría de los análisis de rutina. Podés tomar agua. Si tu pedido no requiere ayuno, '
     'te lo decimos al pasarte el presupuesto.'),
    ('i-hormone', 'Estudios hormonales: el día importa',
     'Varias hormonas se miden en un día determinado del ciclo menstrual. Otras necesitan un horario fijo '
     'de extracción que el laboratorio te indica.'),
    ('i-clock', 'Curva de tolerancia a la glucosa',
     'Después de tomar el líquido azucarado tenés que quedarte 2 horas en el laboratorio. Vení con tiempo '
     'y, si podés, acompañado.'),
    ('i-sunrise', 'Condiciones especiales',
     'Algunas determinaciones piden venir sin haber hecho actividad física y, en ciertos casos, sin haberse '
     'bañado antes. Te avisamos cuáles son al recibir tu pedido.'),
    ('i-tube', 'Medicamentos: no los suspendas por tu cuenta',
     'La mayoría de los estudios no requiere suspender la medicación. Avisanos qué estás tomando y el '
     'bioquímico te confirma cómo seguir.'),
    ('i-doc', 'Muestras que traés vos',
     'Las muestras de orina y de materia fecal las trae el paciente. Para sangre y otras muestras te damos '
     'las indicaciones y las tomamos acá.'),
]

# ------------------------------------------------------------------- FAQ ----
FAQ = [
    ('¿Hacen este análisis? Tengo el pedido médico',
     ['Sí. Trabajamos con análisis de sangre, orina, materia fecal y otras muestras. Mandanos la foto del '
      'pedido médico por WhatsApp y te confirmamos qué estudios hacemos en el laboratorio y cuáles derivamos '
      'a un centro de mayor complejidad.']),
    ('¿Cuánto cuesta?',
     ['El precio depende de las determinaciones que pide el médico. Mandanos la foto del pedido y te pasamos '
      'el presupuesto completo.',
      'Los pedidos con muchas determinaciones o con letra difícil de leer los revisa un bioquímico antes de '
      'responder, para no pasarte un presupuesto equivocado.']),
    ('¿Me piden solo sangre o también orina?',
     ['Depende del pedido. Cuando lo vemos te decimos exactamente qué muestras vamos a tomar y cuáles tenés '
      'que traer vos.']),
    ('¿En cuánto tiempo están los resultados?',
     ['La mayoría de las determinaciones está el mismo día. Los cultivos y algunos estudios especializados '
      'necesitan más tiempo: te damos la fecha exacta cuando recibimos la muestra.']),
    ('¿Tengo que estar en ayunas?',
     ['Algunos estudios sí y otros no. La mayoría no lo requiere, pero venir en ayunas siempre es la opción '
      'más segura: si el médico agrega una determinación, no tenés que volver otro día.',
      'El ayuno habitual para los estudios de rutina es de 8 a 10 horas.']),
    ('¿Necesito turno?',
     ['No. Se atiende por orden de llegada en el horario de cada sede.',
      'Algunos estudios sí se coordinan antes: los que necesitan un horario específico de toma de muestra o '
      'la presencia del bioquímico para procesarla de inmediato.']),
    ('¿Trabajan con seguros médicos?',
     ['Sí. Tenemos convenio con Medilife, Salud Protegida, SPS, Fleming y Comedi. Consultanos por el tuyo '
      'antes de venir.']),
    ('¿Hacen extracción a domicilio?',
     ['Sí. Mandanos tu ubicación por WhatsApp y coordinamos el horario. Salimos a partir de las 07:00 hs.',
      'El traslado cuesta 15.000 Gs dentro del casco urbano. Para zonas más alejadas se calcula por distancia '
      'y te lo confirmamos antes de salir.']),
    ('¿Atienden los fines de semana?',
     ['En Coronel Bogado atendemos sábados de 06:00 a 18:00 hs y domingos de 07:00 a 12:00 hs. '
      'En Carmen del Paraná, sábados de 06:00 a 12:00 hs.',
      'Fuera de horario atendemos urgencias al llamado telefónico, en ambas sedes.']),
    ('¿Cómo recibo mis resultados?',
     ['Te decimos el horario en que van a estar listos. Podés retirarlos en el laboratorio o pedirnos que te '
      'los enviemos por WhatsApp.']),
    ('¿Cómo puedo pagar?',
     ['En efectivo, por transferencia bancaria, con QR, con tarjeta de crédito o por POS.']),
    ('¿Puedo hacerme análisis sin pedido médico?',
     ['Sí, podés pedir estudios de control por tu cuenta. Escribinos y te orientamos sobre los estudios de '
      'rutina más habituales antes de venir.']),
]

# ============================================================ fragmentos ====
def head(titulo, descripcion, base, canonical):
    return f'''<!DOCTYPE html>
<html lang="es-PY">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titulo)}</title>
<meta name="description" content="{e(descripcion)}">
<meta name="theme-color" content="#00AFF0">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{DOMINIO}/{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_PY">
<meta property="og:site_name" content="Laboratorio FamiLab">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(descripcion)}">
<meta property="og:image" content="{DOMINIO}/fotos/logo.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23000'/%3E%3Cpath d='M13 6v6.5a5.5 5.5 0 1 0 6 0V6' fill='none' stroke='%2300AFF0' stroke-width='2.6' stroke-linecap='round'/%3E%3Cpath d='M11.5 6h9' stroke='%2300AFF0' stroke-width='2.6' stroke-linecap='round'/%3E%3Ccircle cx='16' cy='19' r='4.2' fill='%2376C04D'/%3E%3C/svg%3E">
<link rel="apple-touch-icon" href="{base}fotos/logo-marca.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700;800&display=swap">
<link rel="stylesheet" href="{base}assets/estilos.css">
</head>
<body>

<noscript><style>[data-reveal]{{opacity:1!important;transform:none!important}}</style></noscript>

{SPRITE}
'''

NAV = [('Inicio', '#inicio'), ('Servicios', '#servicios'), ('Preparación', '#preparacion'),
       ('A domicilio', '#domicilio'), ('Sedes', '#sedes'), ('Preguntas', '#preguntas')]

def header(base):
    ini = base + 'index.html' if base else ''
    links = '\n'.join(f'      <a href="{ini}{h}">{e(t)}</a>' for t, h in NAV)
    mlinks = '\n'.join(f'  <a href="{ini}{h}">{e(t)}</a>' for t, h in NAV)
    cta = wa(PRESUPUESTO)
    return f'''<header class="hdr" id="hdr">
  <div class="wrap">
    <a href="{ini or '#inicio'}" class="logo" aria-label="Laboratorio FamiLab — inicio">
      <img class="logo-mark" src="{base}fotos/logo-marca.png" alt="" width="400" height="400" decoding="async">
      <span class="logo-txt">
        <b>Fami<i>Lab</i></b>
        <span>Laboratorio de Análisis Clínicos</span>
      </span>
    </a>
    <nav class="nav" id="nav" aria-label="Navegación principal">
{links}
    </nav>
    <div class="hdr-cta">
      <a class="btn btn--wa" href="{cta}" target="_blank" rel="noopener">
        <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Pedir presupuesto
      </a>
      <button class="burger" id="burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="mnav">
        <svg class="ico" id="burger-i" aria-hidden="true"><use href="#i-menu"/></svg>
      </button>
    </div>
  </div>
</header>

<div class="mnav" id="mnav">
{mlinks}
  <a class="btn btn--wa btn--block" href="{cta}" target="_blank" rel="noopener">
    <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Pedir presupuesto
  </a>
</div>
'''

def presupuesto(base=''):
    """Los tres pasos del camino principal: foto del pedido → presupuesto → venir."""
    ini = base + 'index.html' if base else ''
    return f'''
<section class="sec sec--alt" id="presupuesto">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Presupuesto</span>
      <h2>Cómo saber cuánto te sale</h2>
      <p class="lead" style="margin-top:16px">No hace falta llamar ni venir hasta el laboratorio para preguntar el precio.</p>
    </div>
    <div class="pasos">
      <article class="paso" data-reveal>
        <h3>Sacale una foto al pedido médico</h3>
        <p>Mandala por WhatsApp al número de la sede que te queda más cerca. Si no tenés pedido, contanos qué querés controlar.</p>
      </article>
      <article class="paso" data-reveal style="--d:90ms">
        <h3>Te pasamos el presupuesto</h3>
        <p>Te decimos el precio de cada determinación, qué muestras vamos a tomar, si necesitás ayuno y cuándo estarían los resultados.</p>
      </article>
      <article class="paso" data-reveal style="--d:180ms">
        <h3>Venís, o vamos nosotros</h3>
        <p>Se atiende por orden de llegada en el horario de cada sede. Si no podés trasladarte, coordinamos la extracción a domicilio.</p>
      </article>
    </div>
    <div class="paso-nota" data-reveal>
      <svg aria-hidden="true"><use href="#i-info"/></svg>
      <span>Los pedidos con muchas determinaciones o con letra difícil de leer los revisa un bioquímico antes de
      responder: preferimos demorar unos minutos más y no pasarte un presupuesto equivocado.
      <a href="{ini}#preguntas">Ver preguntas frecuentes</a></span>
    </div>
    <div class="center" style="margin-top:34px" data-reveal>
      <a class="btn btn--wa btn--lg" href="{wa(PRESUPUESTO)}" target="_blank" rel="noopener">
        <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Mandar la foto del pedido médico
      </a>
    </div>
  </div>
</section>
'''

def tarjeta_sede(s, delay=0):
    horarios = '<br>'.join(e(h) for h in s['horarios'])
    return f'''      <article class="sede" data-reveal style="--d:{delay}ms">
        <div class="sede-top">
          <span class="kicker"><svg class="ico" style="width:15px;height:15px" aria-hidden="true"><use href="#i-building"/></svg> {e(s['rol'])}</span>
          <h3>{e(s['nombre'])}</h3>
          <p>{e(s['ref'])}</p>
        </div>
        <div class="sede-body">
          <div class="sede-rows">
            <div class="sede-row">
              <svg aria-hidden="true"><use href="#i-pin"/></svg>
              <div><b>Dirección</b><p>{e(s['dir'])}<br>{e(s['ciudad'])}</p></div>
            </div>
            <div class="sede-row">
              <svg aria-hidden="true"><use href="#i-clock"/></svg>
              <div><b>Horario de atención</b><p>{horarios}</p></div>
            </div>
            <div class="sede-row">
              <svg aria-hidden="true"><use href="#i-wa"/></svg>
              <div><b>WhatsApp y teléfono</b><p><a href="{wa(PRESUPUESTO, s['tel'])}" target="_blank" rel="noopener">{e(s['tel_vis'])}</a></p></div>
            </div>
            <div class="sede-row">
              <svg aria-hidden="true"><use href="#i-user"/></svg>
              <div><b>Responsable</b><p>{e(s['responsable'])}</p></div>
            </div>
          </div>
          <div class="sede-urg">
            <svg aria-hidden="true"><use href="#i-moon"/></svg>
            <span>{e(s['urgencias'])}</span>
          </div>
          <div class="map-card" style="margin-top:20px;min-height:250px"
               data-map="{e(s['mapa'])}" data-map-title="Mapa con la ubicación de FamiLab en {e(s['nombre'])}">
            <div class="map-ph">
              <span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-pin"/></svg></span>
              <b>FamiLab {e(s['nombre'])}</b>
              <span>{e(s['dir'])}<br>{e(s['ciudad'])}</span>
              <a class="btn btn--ghost" href="{s['maps_link']}" target="_blank" rel="noopener">
                <svg class="ico" aria-hidden="true"><use href="#i-nav"/></svg> Abrir en Google Maps
              </a>
            </div>
          </div>
          <div class="btn-row">
            <a class="btn btn--wa" href="{wa(PRESUPUESTO, s['tel'])}" target="_blank" rel="noopener">
              <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Escribir a esta sede
            </a>
            <a class="btn btn--ghost" href="{s['ruta']}" target="_blank" rel="noopener">
              <svg class="ico" aria-hidden="true"><use href="#i-nav"/></svg> Cómo llegar
            </a>
          </div>
        </div>
      </article>'''

def seccion_sedes():
    tarjetas = '\n'.join(tarjeta_sede(s, i * 110) for i, s in enumerate(SEDES))
    return f'''
<section class="sec" id="sedes">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Dónde estamos</span>
      <h2>Dos sedes en Itapúa</h2>
      <p class="lead" style="margin-top:16px">Escribile directamente a la sede que te queda más cerca: cada una tiene su propio WhatsApp.</p>
    </div>
    <div class="sedes">
{tarjetas}
    </div>
  </div>
</section>
'''

def cta_final(texto):
    nums = '\n'.join(
        f'''      <a class="cta-num" href="{wa(PRESUPUESTO, s['tel'])}" target="_blank" rel="noopener">
        <svg aria-hidden="true"><use href="#i-wa"/></svg>
        <span>{e(s['tel_vis'])}<small>{e(s['nombre'])}</small></span>
      </a>''' for s in SEDES)
    return f'''
<section class="sec dark cta-final" id="contacto">
  <div class="cta-orbs" aria-hidden="true">
    <span class="o" style="width:420px;height:420px;top:-140px;left:-90px"></span>
    <span class="o" style="width:640px;height:640px;bottom:-280px;right:-160px"></span>
    <svg class="cta-cross" style="width:84px;top:15%;right:9%" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-cross"/></svg>
    <svg class="cta-cross" style="width:48px;bottom:14%;left:8%;animation-delay:1.4s" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-cross"/></svg>
  </div>
  <div class="wrap">
    <span class="eyebrow" data-reveal>Presupuestos</span>
    <h2 data-reveal style="--d:70ms">¿Tenés el pedido médico a mano?</h2>
    <p class="lead" data-reveal style="--d:140ms;color:rgba(232,247,253,.84);max-width:640px;margin-inline:auto">{e(texto)}</p>
    <div class="btn-row" data-reveal style="--d:210ms">
      <a class="btn btn--wa btn--lg" href="{wa(PRESUPUESTO)}" target="_blank" rel="noopener">
        <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Mandar la foto por WhatsApp
      </a>
    </div>
    <div class="cta-nums" data-reveal style="--d:280ms">
{nums}
    </div>
  </div>
</section>
'''

def footer(base):
    ini = base + 'index.html' if base else ''
    servicios = '\n'.join(
        f'          <li><a href="{base}servicios/{s["slug"]}/index.html">{e(s["nombre"])}</a></li>' for s in SERVICIOS)
    sedes = '\n'.join(
        f'''          <div><svg aria-hidden="true"><use href="#i-pin"/></svg><span><b style="color:#fff">{e(s['nombre'])}</b><br>{e(s['dir'])}<br>
            <a href="{wa(PRESUPUESTO, s['tel'])}" target="_blank" rel="noopener">{e(s['tel_vis'])}</a></span></div>''' for s in SEDES)
    return f'''
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-grid">
      <div>
        <a href="{ini or '#inicio'}" class="logo-plate" aria-label="Laboratorio FamiLab — inicio">
          <img src="{base}fotos/logo.png" alt="Laboratorio FamiLab" width="560" height="503" decoding="async">
        </a>
        <p class="ftr-claim">Laboratorio de análisis clínicos con 10 años de trayectoria en Coronel Bogado
        y Carmen del Paraná. Urgencias, extracción a domicilio y convenios con seguros médicos.</p>
      </div>
      <div>
        <h4>Servicios</h4>
        <ul>
{servicios}
        </ul>
      </div>
      <div>
        <h4>Sedes</h4>
        <div class="ftr-contact">
{sedes}
        </div>
        <a class="btn btn--wa" style="margin-top:22px" href="{wa(PRESUPUESTO)}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Pedir presupuesto
        </a>
      </div>
    </div>
    <div class="ftr-bottom">
      <span>© 2026 Laboratorio FamiLab. Todos los derechos reservados.</span>
      <span>Coronel Bogado y Carmen del Paraná — Itapúa, Paraguay</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="{wa(PRESUPUESTO)}" target="_blank" rel="noopener" aria-label="Pedir presupuesto por WhatsApp">
  <svg aria-hidden="true"><use href="#i-wa"/></svg>
  <span class="lbl">Pedí tu presupuesto</span>
</a>

<div class="wa-bar">
  <a class="btn btn--wa btn--lg btn--block" href="{wa(PRESUPUESTO)}" target="_blank" rel="noopener">
    <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Pedir presupuesto por WhatsApp
  </a>
</div>
'''

def jsonld(extra=''):
    servicios = ',\n      '.join('{"@type":"MedicalTest","name":"%s"}' % s['nombre'] for s in SERVICIOS)
    sedes = []
    for s in SEDES:
        geo = ('"geo":{"@type":"GeoCoordinates","latitude":%s,"longitude":%s},' % (LAT1, LNG1)
               if s['slug'] == 'coronel-bogado' else '')
        horas = ('''[
        {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"06:00","closes":"21:00"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"06:00","closes":"18:00"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"07:00","closes":"12:00"}
      ]''' if s['slug'] == 'coronel-bogado' else '''[
        {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"06:30","closes":"11:00"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"13:00","closes":"15:00"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"06:00","closes":"12:00"}
      ]''')
        sedes.append('''{
      "@type":"MedicalClinic",
      "name":"Laboratorio FamiLab — %s",
      "address":{"@type":"PostalAddress","streetAddress":"%s","addressLocality":"%s","addressRegion":"Itapúa","postalCode":"%s","addressCountry":"PY"},
      %s"telephone":"+%s",
      "openingHoursSpecification":%s
    }''' % (s['nombre'], s['dir'], s['ciudad'].split(',')[0], s['cp'], geo, s['tel'], horas))
    return '''
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"MedicalBusiness",
  "name":"Laboratorio FamiLab",
  "description":"Laboratorio de análisis clínicos en Coronel Bogado y Carmen del Paraná, Itapúa. Análisis de rutina, hormonales, microbiológicos, urgencias y extracción de muestras a domicilio.",
  "url":"%s/",
  "logo":"%s/fotos/logo.png",
  "foundingDate":"2016",
  "areaServed":["Coronel Bogado","Carmen del Paraná","Itapúa, Paraguay"],
  "telephone":"+%s",
  "department":[
    %s
  ],
  "availableService":[
      %s
  ]%s
}
</script>
''' % (DOMINIO, DOMINIO, TEL1, ',\n    '.join(sedes), servicios, extra)

def faq_ld():
    entradas = ',\n    '.join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}'
        % (_json(q), _json(' '.join(a))) for q, a in FAQ)
    return '''
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
    %s
]}
</script>
''' % entradas

def _json(t):
    import json
    return json.dumps(t, ensure_ascii=False)

def cierre(base, extra_ld='', con_faq=False):
    return footer(base) + jsonld(extra_ld) + (faq_ld() if con_faq else '') + f'''
<script src="{base}assets/app.js" defer></script>
</body>
</html>
'''

# ================================================================= index ====
def escena_matraz(chips=True):
    """Matraz de laboratorio en 3D, con los colores del logo."""
    extra = '''
        <div class="chip3d chip3d--1"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-clock"/></svg></span><span>Resultados en el día<small>en la mayoría de los estudios</small></span></div>
        <div class="chip3d chip3d--2 chip3d--leaf"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-home"/></svg></span><span>Extracción a domicilio<small>casco urbano y compañías</small></span></div>
        <div class="chip3d chip3d--3"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-building"/></svg></span><span>Dos sedes<small>Cnel. Bogado y Carmen del Paraná</small></span></div>
        <div class="chip3d chip3d--4 chip3d--leaf"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-moon"/></svg></span><span>Urgencias al llamado<small>fuera del horario de atención</small></span></div>''' if chips else ''
    return f'''
      <div class="scene-in" id="sceneIn">
        <div class="glow"></div>
        <div class="ring ring--c"></div>
        <div class="ring ring--a"><i></i></div>
        <div class="ring ring--b"><i></i></div>
        <div class="pedestal"></div>
        <div class="flask-wrap">
          <svg class="ill" viewBox="0 0 180 200">
            <defs>
              <linearGradient id="vidrio" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0" stop-color="#8CDBF9"/><stop offset=".5" stop-color="#00AFF0"/><stop offset="1" stop-color="#0093C6"/>
              </linearGradient>
              <linearGradient id="liquido" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0" stop-color="#AEDC8E"/><stop offset="1" stop-color="#63A93D"/>
              </linearGradient>
              <linearGradient id="brillo" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
              </linearGradient>
              <clipPath id="bulbo"><circle cx="90" cy="128" r="54"/></clipPath>
            </defs>
            <circle cx="90" cy="128" r="54" fill="#EAF8FE"/>
            <g clip-path="url(#bulbo)">
              <path fill="url(#liquido)" d="M20 118c14-9 26 6 40 0s24-12 38-6 26 14 46 4v76H20Z"/>
              <circle class="bubble" cx="70" cy="140" r="6" fill="#fff" opacity=".55"/>
              <circle class="bubble" cx="100" cy="150" r="4.5" fill="#fff" opacity=".5"/>
              <circle class="bubble" cx="86" cy="158" r="3.5" fill="#fff" opacity=".45"/>
            </g>
            <circle cx="90" cy="128" r="54" fill="none" stroke="url(#vidrio)" stroke-width="9"/>
            <path d="M72 80V26M108 80V26" fill="none" stroke="url(#vidrio)" stroke-width="9" stroke-linecap="round"/>
            <path d="M64 24h18M98 24h18" fill="none" stroke="url(#vidrio)" stroke-width="9" stroke-linecap="round"/>
            <ellipse cx="66" cy="104" rx="15" ry="9" fill="url(#brillo)" transform="rotate(-38 66 104)" opacity=".75"/>
          </svg>
        </div>
        <div class="res-card">
          <div class="lbl"><span>Resultados</span><em>listos</em></div>
          <div class="res-rows"><i></i><i></i><i></i></div>
        </div>{extra}
        <div class="particles">
          <i style="width:7px;height:7px;top:16%;left:22%"></i>
          <i style="width:5px;height:5px;top:64%;left:14%;animation-delay:1.6s"></i>
          <i style="width:8px;height:8px;top:78%;left:72%;animation-delay:3.1s"></i>
          <i style="width:5px;height:5px;top:24%;left:82%;animation-delay:2.2s"></i>
        </div>
      </div>'''


def pagina_index():
    serv_cards = '\n'.join(f'''      <article class="card" data-reveal style="--d:{i*70}ms">
        <span class="itile{' itile--leaf' if i % 3 == 1 else ''}"><svg class="ico" aria-hidden="true"><use href="#{s['icono']}"/></svg></span>
        <h3>{e(s['nombre'])}</h3>
        <p>{e(s['resumen'])}</p>
        <a class="card-link" href="servicios/{s['slug']}/index.html">Ver el servicio <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
      </article>''' for i, s in enumerate(SERVICIOS))

    motivos = '\n'.join(
        f'''      <a class="motivo" data-reveal style="--d:{i*50}ms" href="{wa(msg)}" target="_blank" rel="noopener"><span class="b"><svg class="ico" aria-hidden="true"><use href="#{ico}"/></svg></span> {e(t)} <svg class="arw" aria-hidden="true"><use href="#i-arrow"/></svg></a>'''
        for i, (ico, t, msg) in enumerate(MOTIVOS))

    prep = '\n'.join(f'''      <article class="prep" data-reveal style="--d:{i*70}ms">
        <span class="itile{' itile--soft' if i % 2 else ''}"><svg class="ico" aria-hidden="true"><use href="#{ico}"/></svg></span>
        <div><h3>{e(t)}</h3><p>{e(d)}</p></div>
      </article>''' for i, (ico, t, d) in enumerate(PREPARACION))

    equipo = '\n'.join(f'''      <article class="team-card" data-reveal style="--d:{i*70}ms">
        <span class="av"><svg class="ico" aria-hidden="true"><use href="#{p['icono']}"/></svg></span>
        <div>
          <h3>{e(p['nombre'])}</h3>
          <span class="rol">{e(p['rol'])}</span>
          <p class="reg">{e(p['reg'])}</p>
        </div>
      </article>''' for i, p in enumerate(EQUIPO))

    seguros = '\n'.join(
        f'        <span class="pill"><svg aria-hidden="true"><use href="#i-check"/></svg> {e(x)}</span>' for x in SEGUROS)
    pagos = '\n'.join(
        f'        <span class="pill"><svg aria-hidden="true"><use href="#i-check"/></svg> {e(x)}</span>' for x in PAGOS)

    faq = '\n'.join(f'''      <details data-reveal style="--d:{min(i,6)*50}ms"{' open' if i == 0 else ''}>
        <summary>{e(q)} <svg aria-hidden="true"><use href="#i-chevron"/></svg></summary>
        <div class="ans">{''.join('<p>%s</p>' % e(x) for x in a)}</div>
      </details>''' for i, (q, a) in enumerate(FAQ))

    dom = SERV_POR_SLUG['extraccion-a-domicilio']

    return head(
        'Laboratorio FamiLab | Análisis clínicos en Coronel Bogado y Carmen del Paraná',
        'Laboratorio de análisis clínicos con 10 años en Itapúa. Mandá la foto de tu pedido médico por '
        'WhatsApp y te pasamos el presupuesto. Análisis de rutina, hormonales y microbiológicos, urgencias '
        'al llamado y extracción de muestras a domicilio.',
        '', '') + header('') + f'''
<main id="inicio">

<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="badge" data-reveal><i class="dot"></i> FamiLab · 10 años en Itapúa</span>
      <h1 data-reveal style="--d:80ms">¿Tenés un <span class="u">pedido médico?</span></h1>
      <p class="hero-sub" data-reveal style="--d:160ms">
        Mandanos la foto por WhatsApp y te pasamos el presupuesto: qué muestras vamos a tomar,
        si necesitás ayuno y cuándo estarían los resultados.
      </p>
      <p class="hero-note" data-reveal style="--d:220ms">
        Coronel Bogado, de 06:00 a 21:00 hs, también sábados y domingos.
        Carmen del Paraná, de lunes a sábado.
      </p>
      <div class="btn-row" data-reveal style="--d:280ms">
        <a class="btn btn--wa btn--lg" href="{wa(PRESUPUESTO)}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Mandar la foto del pedido
        </a>
        <a class="btn btn--ghost btn--lg" href="#servicios">
          <svg class="ico" aria-hidden="true"><use href="#i-tubes"/></svg> Ver análisis y servicios
        </a>
      </div>
      <div class="hero-mini" data-reveal style="--d:340ms">
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> Más de 49.000 pacientes atendidos</span>
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> La mayoría de los resultados, en el día</span>
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> Extracción a domicilio</span>
      </div>
    </div>

    <div class="scene" id="scene" aria-hidden="true">{escena_matraz()}
    </div>
  </div>
</section>

<section class="sec datos" style="padding-top:clamp(10px,2vw,26px)">
  <div class="wrap">
    <div class="grid datos-grid">
      <article class="card" data-reveal>
        <span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-clock"/></svg></span>
        <h3>Abrimos a las 06:00</h3>
        <p>En Coronel Bogado atendemos hasta las 21:00 hs, y también sábados y domingos.</p>
      </article>
      <article class="card" data-reveal style="--d:90ms">
        <span class="itile itile--soft"><svg class="ico" aria-hidden="true"><use href="#i-doc-check"/></svg></span>
        <h3>Resultados en el día</h3>
        <p>La mayoría de las determinaciones de rutina se entrega el mismo día. Te los mandamos por WhatsApp si querés.</p>
      </article>
      <article class="card" data-reveal style="--d:180ms">
        <span class="itile itile--accent"><svg class="ico" aria-hidden="true"><use href="#i-micro"/></svg></span>
        <h3>Los estudios que no se hacen en el hospital</h3>
        <p>Hormonales, microbiológicos y especializados, sin tener que viajar a Encarnación.</p>
      </article>
      <article class="card" data-reveal style="--d:270ms">
        <span class="itile itile--warn"><svg class="ico" aria-hidden="true"><use href="#i-moon"/></svg></span>
        <h3>Urgencias al llamado</h3>
        <p>Fuera del horario de atención respondemos por teléfono, en las dos sedes.</p>
      </article>
    </div>
  </div>
</section>
''' + presupuesto() + f'''
<section class="sec sec--sky" id="servicios">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Qué hacemos</span>
      <h2>Análisis y servicios</h2>
      <p class="lead" style="margin-top:16px">Si tu pedido incluye algún estudio muy específico que no procesamos acá,
      lo derivamos a un laboratorio de mayor complejidad y te avisamos antes.</p>
    </div>
    <div class="grid serv-grid">
{serv_cards}
      <article class="card serv-cta" data-reveal style="--d:{len(SERVICIOS)*70}ms;background:linear-gradient(160deg,var(--cy-600),var(--cy-950));border-color:transparent;color:#fff">
        <span class="itile" style="background:rgba(255,255,255,.14);border-color:rgba(255,255,255,.2);color:#fff"><svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg></span>
        <h3 style="color:#fff">¿No sabés qué estudio necesitás?</h3>
        <p style="color:rgba(232,247,253,.84)">Mandanos la foto del pedido médico o contanos qué te indicó el doctor.
        Un bioquímico lo revisa y te responde.</p>
        <a class="btn btn--wa btn--block" style="margin-top:20px" href="{wa('no sé qué estudio necesito. ¿Me orientan?')}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar por WhatsApp
        </a>
      </article>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Accesos rápidos</span>
      <h2>¿Qué necesitás consultar?</h2>
      <p class="lead" style="margin-top:16px">Tocá lo más parecido a tu caso y te respondemos por WhatsApp.</p>
    </div>
    <div class="motivos">
{motivos}
    </div>
  </div>
</section>

<section class="sec sec--leaf" id="preparacion">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Antes de venir</span>
      <h2>Cómo prepararte</h2>
      <p class="lead" style="margin-top:16px">Venir bien preparado evita tener que repetir la extracción otro día.</p>
    </div>
    <div class="grid prep-grid">
{prep}
    </div>
    <div class="aviso" data-reveal style="max-width:900px;margin-inline:auto">
      <svg aria-hidden="true"><use href="#i-alert"/></svg>
      <span><b>Confirmá siempre tu caso antes de venir.</b> Estas indicaciones son generales. Cuando nos mandás
      el pedido médico te decimos exactamente qué preparación necesita cada determinación que te pidieron.</span>
    </div>
  </div>
</section>

<section class="sec dark" id="domicilio">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow">A domicilio</span>
      <h2>Si no podés venir, vamos nosotros</h2>
      <p class="lead" style="margin-top:20px;color:rgba(232,247,253,.84)">
        {e(dom['intro'])}
      </p>
      <ul class="checklist">
        <li><svg aria-hidden="true"><use href="#i-check-c"/></svg> Salimos a partir de las 07:00 hs, coordinando antes por WhatsApp</li>
        <li><svg aria-hidden="true"><use href="#i-check-c"/></svg> 15.000 Gs de traslado dentro del casco urbano</li>
        <li><svg aria-hidden="true"><use href="#i-check-c"/></svg> Fuera del casco urbano se calcula por distancia y te lo confirmamos antes</li>
        <li><svg aria-hidden="true"><use href="#i-check-c"/></svg> Pensado para quienes tienen dificultad para movilizarse</li>
      </ul>
      <div class="btn-row" style="margin-top:32px">
        <a class="btn btn--wa btn--lg" href="{wa('quiero una extracción a domicilio. Mi ubicación es:')}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Coordinar una extracción
        </a>
        <a class="btn btn--outline-light btn--lg" href="servicios/extraccion-a-domicilio/index.html">
          Ver cómo funciona <svg class="ico" aria-hidden="true"><use href="#i-arrow"/></svg>
        </a>
      </div>
    </div>
    <div class="grid lab-grid" data-reveal style="--d:120ms">
      <div class="glass"><span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-pin"/></svg></span><h3>Mandás tu ubicación</h3><p>Por WhatsApp, junto con la foto del pedido médico.</p></div>
      <div class="glass"><span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-calendar"/></svg></span><h3>Coordinamos el horario</h3><p>Te confirmamos si llegamos a tu zona y a qué hora.</p></div>
      <div class="glass"><span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-syringe"/></svg></span><h3>Tomamos la muestra en tu casa</h3><p>Con las mismas condiciones que en el laboratorio.</p></div>
      <div class="glass"><span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-doc-check"/></svg></span><h3>Te avisamos los resultados</h3><p>Los retirás en la sede o te los enviamos por WhatsApp.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Trayectoria</span>
      <h2>Diez años acompañando a la región</h2>
      <p class="lead" style="margin-top:16px">FamiLab nació junto a la zona hospitalaria de Coronel Bogado, para que la gente
      tuviera respuestas rápidas sin tener que viajar. En 2020 abrimos la sucursal de Carmen del Paraná.</p>
    </div>
    <div class="nums">
      <div class="num-card" data-reveal><b>10 años</b><span>de trayectoria en análisis clínicos</span></div>
      <div class="num-card" data-reveal style="--d:90ms"><b>+49.000</b><span>pacientes registrados en nuestro sistema</span></div>
      <div class="num-card" data-reveal style="--d:180ms"><b>2 sedes</b><span>Coronel Bogado y Carmen del Paraná</span></div>
    </div>
  </div>
</section>

<section class="sec sec--alt" id="equipo">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Quién procesa tus muestras</span>
      <h2>Equipo profesional</h2>
      <p class="lead" style="margin-top:16px">Bioquímicos matriculados, con registro profesional y responsables técnicos en cada sede.</p>
    </div>
    <div class="grid team-grid">
{equipo}
    </div>
  </div>
</section>

<section class="sec sec--sky" id="convenios">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow">Convenios</span>
      <h2>Seguros médicos, empresas y derivaciones</h2>
      <p class="lead" style="margin-top:18px">
        Trabajamos con seguros médicos y con empresas de la zona. Los pacientes derivados del Centro Médico
        San Blas tienen descuentos especiales.
      </p>
      <div class="pills">
{seguros}
      </div>
      <p class="lead" style="margin-top:30px;font-size:1rem">Formas de pago</p>
      <div class="pills">
{pagos}
      </div>
      <div class="btn-row" style="margin-top:32px">
        <a class="btn btn--brand btn--lg" href="{wa('quiero saber si trabajan con mi seguro médico.')}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-shield"/></svg> Consultar por mi seguro
        </a>
      </div>
    </div>
    <div class="grid" data-reveal style="--d:120ms">
      <article class="card">
        <span class="itile itile--leaf"><svg class="ico" aria-hidden="true"><use href="#i-briefcase"/></svg></span>
        <h3>Convenios con empresas</h3>
        <p>Estudios preocupacionales y controles periódicos del personal, coordinados en una misma jornada.
        Escribinos indicando cuántas personas son y qué estudios autoriza la empresa.</p>
        <a class="card-link" href="servicios/analisis-ocupacionales/index.html">Ver análisis ocupacionales <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
      </article>
      <article class="card">
        <span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-stetho"/></svg></span>
        <h3>Médicos y clínicas que derivan</h3>
        <p>Recibimos derivaciones del Centro Médico San Blas y de profesionales de la zona. Si sos médico y
        querés derivar pacientes, escribinos y coordinamos.</p>
        <a class="card-link" href="{wa('soy médico y quiero coordinar derivaciones al laboratorio.')}" target="_blank" rel="noopener">Coordinar derivaciones <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
      </article>
    </div>
  </div>
</section>
''' + seccion_sedes() + f'''
<section class="sec sec--alt" id="preguntas">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Preguntas frecuentes</span>
      <h2>Lo que más nos preguntan</h2>
      <p class="lead" style="margin-top:16px">Las mismas respuestas que damos todos los días por WhatsApp.</p>
    </div>
    <div class="faq">
{faq}
    </div>
  </div>
</section>
''' + cta_final(
    'Mandala por WhatsApp al número de la sede que te queda más cerca y te pasamos el presupuesto con '
    'los plazos de entrega y la preparación que necesitás.'
) + '\n</main>\n' + cierre('', con_faq=True)

# ================================================= páginas por servicio ====
def pagina_servicio(s):
    base = '../../'
    incluye = '\n'.join(
        f'''        <div class="proc"><span class="itile{' itile--soft' if i % 2 else ''}"><svg class="ico" aria-hidden="true"><use href="#{s['icono']}"/></svg></span><div><b>{e(x)}</b><span>Consultanos por disponibilidad y precio</span></div></div>'''
        for i, x in enumerate(s['incluye']))

    otros = [o for o in SERVICIOS if o['slug'] != s['slug']][:3]
    relacionados = '\n'.join(f'''      <article class="card" data-reveal style="--d:{i*70}ms">
        <span class="itile{' itile--leaf' if i % 2 else ''}"><svg class="ico" aria-hidden="true"><use href="#{o['icono']}"/></svg></span>
        <h3>{e(o['nombre'])}</h3>
        <p>{e(o['resumen'])}</p>
        <a class="card-link" href="{base}servicios/{o['slug']}/index.html">Ver el servicio <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
      </article>''' for i, o in enumerate(otros))

    nota = f'''
    <div class="aviso" data-reveal style="max-width:820px;margin-inline:auto;margin-top:30px">
      <svg aria-hidden="true"><use href="#i-info"/></svg>
      <span>{e(s['nota'])}</span>
    </div>''' if s.get('nota') else ''

    enlace = wa('quiero consultar por %s. Les mando la foto del pedido médico.' % s['nombre'].lower())
    return head(
        '%s | Laboratorio FamiLab' % s['nombre'],
        '%s Mandá la foto de tu pedido médico por WhatsApp y te pasamos el presupuesto. '
        'FamiLab, Coronel Bogado y Carmen del Paraná.' % s['intro'],
        base, 'servicios/%s/' % s['slug']) + header(base) + f'''
<main id="inicio">

<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <a class="volver" href="{base}index.html"><svg aria-hidden="true"><use href="#i-arrow"/></svg> Todos los servicios</a>
      <h1 data-reveal>{e(s['titulo'])}</h1>
      <p class="hero-sub" data-reveal style="--d:120ms">{e(s['intro'])}</p>
      <p class="hero-note" data-reveal style="--d:180ms">{e(s['tiempo'])}</p>
      <div class="btn-row" data-reveal style="--d:240ms">
        <a class="btn btn--wa btn--lg" href="{enlace}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Pedir presupuesto
        </a>
        <a class="btn btn--ghost btn--lg" href="#incluye">Ver qué incluye <svg class="ico" aria-hidden="true"><use href="#i-arrow"/></svg></a>
      </div>
      <div class="hero-mini" data-reveal style="--d:300ms">
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> Coronel Bogado y Carmen del Paraná</span>
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> Bioquímicos matriculados</span>
      </div>
    </div>
    <div class="scene" aria-hidden="true">{escena_matraz(chips=False)}
    </div>
  </div>
</section>

<section class="sec" id="incluye">
  <div class="wrap" style="max-width:820px">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Qué incluye</span>
      <h2>Estudios de esta área</h2>
      <p class="lead" style="margin-top:16px">El listado completo depende de lo que pida tu médico: mandanos la foto del pedido y lo revisamos.</p>
    </div>
    <div class="proc-list">
{incluye}
    </div>
  </div>
</section>

<section class="sec sec--leaf">
  <div class="wrap" style="max-width:820px">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Antes de venir</span>
      <h2>Preparación</h2>
    </div>
    <p class="lead center" data-reveal style="max-width:64ch;margin-inline:auto">{e(s['prep'])}</p>{nota}
    <div class="center" style="margin-top:34px" data-reveal>
      <a class="btn btn--wa btn--lg" href="{enlace}" target="_blank" rel="noopener">
        <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar mi caso
      </a>
    </div>
  </div>
</section>
''' + presupuesto(base) + seccion_sedes() + f'''
<section class="sec sec--sky">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">También hacemos</span>
      <h2>Otros servicios</h2>
    </div>
    <div class="grid serv-grid">
{relacionados}
    </div>
  </div>
</section>
''' + cta_final(
        'Mandanos la foto del pedido médico y te pasamos el presupuesto de %s con los plazos de entrega.'
        % s['nombre'].lower()
    ) + '\n</main>\n' + cierre(base)


# ==================================================================== salida ====
def escribir(ruta, contenido):
    destino = os.path.join(RAIZ, ruta)
    os.makedirs(os.path.dirname(destino) or '.', exist_ok=True)
    open(destino, 'w', encoding='utf-8').write(contenido)
    print('  %-50s %6.1f KB' % (ruta, len(contenido.encode()) / 1024))


def sitemap():
    urls = ['%s/' % DOMINIO] + ['%s/servicios/%s/' % (DOMINIO, s['slug']) for s in SERVICIOS]
    cuerpo = '\n'.join('  <url><loc>%s</loc><changefreq>monthly</changefreq></url>' % u for u in urls)
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % cuerpo


if __name__ == '__main__':
    print('Generando páginas:')
    escribir('index.html', pagina_index())
    for s in SERVICIOS:
        escribir('servicios/%s/index.html' % s['slug'], pagina_servicio(s))
    escribir('sitemap.xml', sitemap())
    escribir('robots.txt', 'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % DOMINIO)
    print('Listo.')
