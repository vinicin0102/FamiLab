# Centro Médico San Blas + Laboratorio FamiLab — Coronel Bogado, Paraguay

Sitio estático, sin dependencias de runtime. Se sube tal cual a cualquier
hosting o CDN.

```
index.html                       página principal del ecosistema
servicios/<slug>/index.html      una página por servicio de laboratorio
assets/estilos.css               estilos compartidos por todas las páginas
assets/app.js                    scripts compartidos
fotos/                           logos de las dos marcas
tools/build.py                   genera el HTML a partir de los datos
sitemap.xml · robots.txt         generados junto con las páginas
```

## El concepto

No es una landing de laboratorio con un centro médico pegado al lado. Son
**dos empresas distintas del mismo propietario, a una cuadra una de la otra**,
que se derivan pacientes entre sí:

- **Centro Médico San Blas** — consulta, diagnóstico médico y seguimiento.
  Es la puerta de entrada del ecosistema y lleva la prioridad visual.
- **Laboratorio FamiLab** — análisis, estudios y respaldo diagnóstico.
  Tiene bloque, identidad y páginas propias: no aparece como «el laboratorio
  de San Blas».

El circuito comercial es `Consulta → Diagnóstico → Análisis → Resultados →
Seguimiento`, y funciona en los dos sentidos: quien llega con un pedido médico
entra directo por FamiLab y, si necesita que lo vea un médico, lo tiene a una
cuadra.

## Cómo está ordenada la página

1. **Hero — San Blas protagonista.** «Tu salud, atendida en un mismo lugar».
   CTAs: *Agendar una consulta* y *Ver especialidades*.
2. **Los dos recorridos.** El punto central: dos tarjetas, «Necesito atención
   médica» (San Blas) y «Ya tengo un pedido médico» (FamiLab), cada una con
   sus cuatro pasos y su propio CTA. Nadie recorre un embudo que no le toca.
3. **Atención médica en San Blas** — especialidades, profesionales y servicios.
4. **Un solo circuito de atención** — los cinco pasos, coloreados por marca.
5. **Bloque propio de FamiLab** — 10 años, +49.000 pacientes, dos sedes,
   resultados en el día, urgencias y domicilio, con los tres CTA que pide el
   documento: *Enviar pedido médico*, *Solicitar presupuesto* y *Ver servicios
   de laboratorio*.
6. **Análisis y servicios** — siete áreas, cada una con su página.
7. **Presupuesto en tres pasos** — foto del pedido → presupuesto → venís o vamos.
8. **Preparación del paciente** — ayuno, hormonas y ciclo, curva de tolerancia,
   medicación, qué muestras trae el paciente.
9. **Extracción a domicilio** — cobertura, costo y cómo se coordina.
10. **Equipo profesional de FamiLab** — con registro profesional de cada uno.
11. **Convenios** — seguros médicos, empresas y derivaciones.
12. **Dónde estamos** — el bloque de «a una cuadra» con las dos marcas, y
    debajo las dos sedes del laboratorio con su WhatsApp y su mapa.
13. **Accesos por intención** — seis entradas de WhatsApp, no un «contactar»
    genérico: agendar consulta, consultar especialidad, enviar pedido médico,
    solicitar presupuesto, consultar resultados y atención a domicilio. Cada
    una abre el chat con su mensaje armado, para que después el CRM pueda
    separar los leads por intención.
14. **Preguntas frecuentes** — las del ecosistema y las del laboratorio.
15. **CTA final** con las dos acciones.

### Reglas de redacción

Cada frase tiene que ayudar al paciente a decidir si acá resuelve lo que
necesita ahora. Si sólo dice que la institución es «completa», «humana» o «de
confianza», se reemplaza por información concreta.

Quedan fuera: «calidad y calidez», «tu salud es nuestra prioridad»,
«tecnología de última generación», «atención personalizada». También quedan
fuera las promesas de resultado y los plazos sin confirmar: se dice «la mayoría
de las determinaciones está el mismo día», que es lo que el laboratorio afirma.

Español de Paraguay, con voseo, en tono directo.

## Editar el contenido

Todo el texto vive en `tools/build.py`, arriba de todo:

| Bloque | Qué controla |
|---|---|
| `SEDES` | las dos sedes del laboratorio |
| `SERVICIOS` | los siete servicios de laboratorio y sus páginas |
| `SAN_BLAS` | datos del centro médico |
| `ESPECIALIDADES_SB`, `PROFESIONALES_SB`, `SERVICIOS_SB` | contenido de San Blas |
| `RUTAS` | los dos recorridos |
| `CIRCUITO` | los cinco pasos |
| `INTENCIONES` | los accesos de WhatsApp |
| `EQUIPO`, `PREPARACION`, `FAQ`, `FAQ_ECO`, `SEGUROS`, `PAGOS` | el resto |

Después de cambiar algo:

```bash
python3 tools/build.py
```

Regenera todo y avisa por consola qué datos siguen faltando.

## Identidad

Las dos marcas comparten paleta, porque sus logos la comparten: San Blas usa
cian `#00ADEF` y verde `#70BE43`; FamiLab, `#00AFF0` y `#76C04D`. Los tokens
están en `assets/estilos.css`, en el bloque `:root`.

La diferencia entre marcas no la hace el tono sino el tratamiento:

- **San Blas** lidera en cian sólido, sobre fondo claro (`.sec--sb`), con
  botones `btn--brand`.
- **FamiLab** aparece en la franja oscura (`.dark`) y con acentos verdes.
- El verde de WhatsApp (`#25D366`) se reserva para los botones de ese canal.
- El naranja aparece sólo en urgencias y advertencias.

Los dos logos van juntos en el header y en el footer (`.marca-dual`), separados
por un `+`: ninguna marca absorbe a la otra.

Los cuatro archivos de marca son PNG con fondo transparente, recortados del
material que envió el cliente:

| Archivo | Qué es | Dónde se usa |
|---|---|---|
| `fotos/logo.png` | FamiLab completo, con bajada | footer |
| `fotos/logo-marca.png` | sólo el matraz | header, chips, bloque de la cuadra |
| `fotos/san-blas.png` | San Blas completo | header y footer |
| `fotos/san-blas-marca.png` | sólo el corazón con la mano | chips, bloque de la cuadra |

Al ser transparentes funcionan igual sobre fondo claro y sobre la franja oscura:
el trazo blanco de cada logo los separa del fondo. Por eso ningún contenedor les
pone color de fondo — si se reemplazan por versiones opacas, hay que revisar
`.marca-dual`, `.marca-chip` y `.cuadra-punto` en `assets/estilos.css`.

El de San Blas todavía sale de una captura del PDF de onboarding: **conviene
pedir el original** (vectorial o PNG de más resolución).

## Datos que usa el sitio

### Laboratorio FamiLab

| Dato | Coronel Bogado | Carmen del Paraná |
|---|---|---|
| Dirección | Encarnación y Tacuary | Gral. Díaz entre Alberdi y Colón |
| Referencia | Esquina del H.D.C.B. | Frente al IPS |
| WhatsApp | 0995 371 105 | 0992 995 397 |
| Lunes a viernes | 06:00 a 21:00 | 06:30 a 11:00 y 13:00 a 15:00 |
| Sábados | 06:00 a 18:00 | 06:00 a 12:00 |
| Domingos | 07:00 a 12:00 | — |
| Urgencias | al llamado desde las 21:00 | al llamado |
| Responsable | Bqco. Mgtr. Oscar Alvarez | Bqca. Sandra Avalos |

Los números personales que figuran en el formulario de onboarding **no están
publicados**: la página sólo muestra los dos números institucionales.

### Centro Médico San Blas

Sólo está confirmado que queda en Coronel Bogado, a una cuadra del laboratorio,
que deriva pacientes a FamiLab y que esos pacientes tienen descuentos
especiales. El resto está pendiente (ver abajo).

## Mapa

La sede de Coronel Bogado usa **-27.169587, -56.233484**, coordenadas
decodificadas del código plus `RQJ8+5JC` (`5845RQJ8+5J`) que envió FamiLab.
Carmen del Paraná arma su mapa con la dirección. Los embeds no usan API key y
se cargan recién cuando el visitante se acerca a la sección.

## Lo que falta

Ordenado por lo que más frena la página:

1. **WhatsApp propio del Centro Médico San Blas.** Es lo más urgente: hoy todos
   los CTA de consulta médica entran por el número de FamiLab Coronel Bogado,
   que ya coordina las derivaciones entre ambos. Se carga en `TEL_SB` y
   `TEL_SB_VIS` y todos los botones cambian solos.
2. **Especialidades, profesionales y servicios de San Blas.** El documento de
   orientación lo dice expresamente. Mientras no lleguen, la sección de San Blas
   no inventa nada: muestra un bloque que invita a consultar por WhatsApp qué
   especialidad corresponde. Al cargar `ESPECIALIDADES_SB`, `PROFESIONALES_SB` y
   `SERVICIOS_SB`, ese bloque se reemplaza solo por las grillas completas.
3. **Dirección exacta y horarios de San Blas**, en `SAN_BLAS`.
4. **Fotos reales** de médicos, bioquímicos, consultorios, laboratorio y
   equipos. El documento pide expresamente evitar imágenes genéricas o
   generadas por IA. Hoy la página no tiene galería ni retratos: usa
   ilustraciones propias construidas con los colores de las marcas.
5. **Tarifario** del laboratorio. Por eso la página no publica ningún precio de
   análisis: todo pasa por el presupuesto en WhatsApp. El único precio publicado
   es el traslado a domicilio (15.000 Gs dentro del casco urbano), que sí está
   confirmado.
6. **Dominio.** `DOMINIO` en `tools/build.py` apunta a `https://familab.com.py`.
   Si el sitio pasa a ser del ecosistema, conviene revisar qué dominio va: de ahí
   salen las URLs canónicas, el Open Graph y el sitemap.
7. **Coordenadas** exactas de Carmen del Paraná y de San Blas.
8. **Tiempo de respuesta.** El onboarding fija 5 minutos como objetivo interno.
   No está publicado como promesa hasta que lo confirmen.
9. **Reseñas y testimonios** autorizados, con nombre.
10. **Píxeles y analítica** (Meta, Google) cuando estén creadas las cuentas.
