# Laboratorio FamiLab — Coronel Bogado y Carmen del Paraná, Paraguay

Sitio estático, sin dependencias de runtime. Se sube tal cual a cualquier
hosting o CDN.

```
index.html                       página principal
servicios/<slug>/index.html      una página por servicio (campañas)
assets/estilos.css               estilos compartidos por todas las páginas
assets/app.js                    scripts compartidos
fotos/                           logo y marca
tools/build.py                   genera el HTML a partir de los datos
sitemap.xml · robots.txt         generados junto con las páginas
```

Construido a partir del formulario de onboarding Nexo × FamiLab, con la misma
arquitectura que el sitio de Policlínica Sanitas.

## Cómo está pensada la página

El orden responde a lo que necesita alguien que llega de un anuncio con un
pedido médico en la mano, no a lo que el laboratorio quiere contar de sí mismo:

**pedido médico → presupuesto → qué hacemos → cómo prepararte → dónde y cuándo**

1. **Hero** — «¿Tenés un pedido médico?» y qué hacer con él ahora mismo.
2. **Datos concretos** — horario, resultados en el día, estudios que no se
   hacen en el hospital, urgencias al llamado.
3. **Cómo saber cuánto te sale** — los tres pasos del camino principal:
   foto del pedido → presupuesto → venís o vamos.
4. **Análisis y servicios** — siete áreas, cada una con su página.
5. **Accesos rápidos** — un WhatsApp por motivo de consulta.
6. **Cómo prepararte** — ayuno, hormonas y ciclo, curva de tolerancia,
   medicamentos, qué muestras trae el paciente.
7. **Extracción a domicilio** — cobertura, costo y cómo se coordina.
8. **Trayectoria** — 10 años, +49.000 pacientes, dos sedes.
9. **Equipo profesional** — con registro profesional de cada uno.
10. **Convenios** — seguros médicos, empresas y derivaciones.
11. **Sedes** — las dos, cada una con su WhatsApp, horarios y mapa.
12. **Preguntas frecuentes** — las que reciben todos los días.
13. **CTA final**.

### Acción principal

El formulario marcó «consultar por WhatsApp» y «solicitar precio» como las
acciones prioritarias. Toda la página empuja a lo mismo: **mandar la foto del
pedido médico por WhatsApp para recibir el presupuesto.** Cada sede tiene su
propio número y los botones de cada sección arrastran un mensaje distinto
según el contexto, así el que responde sabe de dónde viene el contacto.

### Reglas de redacción

Cada frase tiene que ayudar al paciente a decidir si FamiLab resuelve lo que
necesita ahora. Si sólo dice que el laboratorio es «completo», «humano» o «de
confianza», se reemplaza por información concreta.

Quedan fuera: «calidad y calidez», «tu salud es nuestra prioridad»,
«tecnología de última generación», «atención personalizada». También quedan
fuera las promesas de resultado y los plazos que no estén confirmados: se dice
«la mayoría de las determinaciones está el mismo día», que es lo que el
laboratorio afirma, y no «resultados en el día» a secas.

Español de Paraguay, con voseo, en tono directo.

## Páginas por servicio

Una página por servicio, para mandar tráfico segmentado sin obligar a nadie a
buscar dentro de la página general. Quien busca «análisis hormonales Coronel
Bogado» cae en `servicios/analisis-hormonales/index.html` y ve de entrada qué
incluye, la preparación, las dos sedes y el WhatsApp.

Hoy existen siete: análisis de rutina, hormonales, microbiológicos, de
urgencia, extracción a domicilio, chequeos preventivos y ocupacionales.

## Editar el contenido

Todo el texto vive en `tools/build.py`, arriba de todo: `SEDES`, `SERVICIOS`,
`MOTIVOS`, `EQUIPO`, `PREPARACION`, `FAQ`, `SEGUROS` y `PAGOS`. Después de
cambiar algo:

```bash
python3 tools/build.py
```

Regenera `index.html`, las siete páginas de servicio, el sitemap y el
robots.txt, consistentes entre sí. Editar el HTML a mano funciona, pero el
próximo build lo pisa.

## Identidad

Cian `#00AFF0` y verde `#76C04D`, tomados del logo. Los tokens están en
`assets/estilos.css`, en el bloque `:root`. Los neutros están sesgados hacia el
cian.

El verde de marca aparece en acentos, tildes de confirmación e íconos. El verde
de WhatsApp (`#25D366`) se reserva para los botones de ese canal, que es el
color con el que la gente lo reconoce. El naranja aparece sólo en los bloques
de urgencias y advertencias.

El logo llegó como captura dentro del PDF de onboarding: `fotos/logo.png` es el
logo completo sobre su fondo negro y `fotos/logo-marca.png` es sólo el matraz,
que se usa en el header. **Conviene pedirle a FamiLab el archivo original**
(vectorial o PNG con transparencia) para reemplazar ambos.

## Datos que usa el sitio

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

Los números personales que figuran en el formulario (dirección, bioquímica de
planta, técnico) **no están publicados**: la página sólo muestra los dos
números institucionales de las sedes.

## Mapa

La sede de Coronel Bogado usa **-27.169587, -56.233484**, coordenadas
decodificadas del código plus `RQJ8+5JC` (`5845RQJ8+5J`) que envió FamiLab.
Alimentan el embed de Google Maps, el botón «Cómo llegar» y el campo `geo` de
los datos estructurados.

Carmen del Paraná todavía no tiene coordenadas confirmadas: su mapa y su botón
«Cómo llegar» se arman con la dirección `Gral. Díaz 644, Carmen del Paraná
070701`. Cuando lleguen las coordenadas exactas, se cargan en `SEDES` igual que
las de la otra sede.

Los embeds no usan API key y se cargan recién cuando el visitante se acerca a
la sección. Si un iframe no carga, el bloque muestra igual el nombre, la
dirección y un enlace a Google Maps.

## Lo que falta

- **Tarifario.** El formulario marcó «faltaría». Por eso la página no publica
  ningún precio de análisis: todo pasa por el presupuesto en WhatsApp. El único
  precio publicado es el traslado a domicilio (15.000 Gs dentro del casco
  urbano), que sí está confirmado. Cuando llegue el tarifario de rutina se puede
  agregar una sección de precios.
- **Logo original**, en vectorial o PNG con transparencia.
- **Fotos reales** del laboratorio, del equipo y de los equipos de análisis. La
  página hoy no tiene galería; conviene agregarla cuando haya material.
- **Coordenadas** exactas de Carmen del Paraná.
- **Dominio.** `DOMINIO` en `tools/build.py` apunta a
  `https://familab.com.py`. Cambiarlo antes de publicar: de ahí salen las URLs
  canónicas, el Open Graph y el sitemap.
- **Tiempo de respuesta.** El formulario fija 5 minutos como objetivo interno.
  No está publicado como promesa hasta que FamiLab confirme que quiere
  comprometerse a ese plazo.
- **Reseñas y testimonios** autorizados, con nombre.
- **Píxeles y analítica** (Meta, Google) cuando estén creadas las cuentas.
