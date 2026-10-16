# Auditoría inicial de fuentes — R001

**Agente:** investigador_fuentes. **Fase:** F0. **Consulta:** 14 de octubre de 2026. **Entradas:** versión 1.0.0, hashes de `coordinacion/contextos/R001_insumos.json`.

## Respuesta al encargo

La auditoría se ejecutó mediante un **subagente del entorno de esta sesión**. No se ejecutó Codex CLI ni se comprobó el descubrimiento de los perfiles en la computadora del usuario. Las conclusiones corresponden a la lectura del avance y a fuentes externas efectivamente abiertas; no certifican la tesis ni cierran F1 o F2.

Se verificaron por separado identidad, acceso y apoyo de las afirmaciones. Las cuatro fuentes prioritarias existen. F005 cuenta con texto completo leído; F007 y F009 con textos completos disponibles y apartados pertinentes revisados; F001 únicamente con catálogo oficial. El procedimiento completo PCI sigue pendiente. Las otras ocho referencias no quedan aprobadas para citas finales: algunas tienen metadatos comprobados o apoyo parcial, y las demás permanecen pendientes.

## Evidencia prioritaria

| ID y páginas del avance | Acceso efectivo y localización externa | Resultado y límite |
|---|---|---|
| F001; pp. 7, 12–14 | Catálogo ASTM D6433-18: alcance §1.1, uso §4.1 y versiones | Identidad y DOI comprobados. Es una edición histórica; el catálogo señala D6433-24 como activa. El PCI describe condición superficial y no mide capacidad estructural. No se accedió a las instrucciones, tablas ni curvas completas. Elegir edición con asesor y acceso autorizado; no sustituir silenciosamente la edición ni reproducirla desde antecedentes. |
| F005; pp. 4, 6, 10–11 y 14 | PDF español completo de ALCONPAT en SciELO; §3 pp. 225–226, §4.3 y tablas 8–11 pp. 230–232 | Se sostienen 19 tramos, PCI y relación débil. Son tramos de 80 m con pavimento flexible. Tabla 11: r=0.14 para sumideros y r=0.39 para cunetas. La tabla 8 asigna cero a ausencia y divide PCI por 25. Estos criterios no se transfieren automáticamente a Jaén. |
| F007; pp. 3–4, 12 y 14 | PDF del portal MTC, introducción pp. 12–13, objetivos pp. 16–17, §4.1.1.3.7(d) pp. 80–81, §4.1.2 pp. 171–172 y §4.2.4 p. 200 | El manual sustenta protección vial frente al agua y relevancia del mantenimiento. Es una guía de diseño hidrológico e hidráulico; su lectura visual no acredita capacidad de una estructura. No se deriva una escala ordinal validada ni obligatoriedad concreta en Pakamuros sin clasificar la vía. |
| F009; pp. 3–4, 7, 12 y 15 | El Peruano, publicación 29/05/2026; decreto art. 2; reglamento arts. 2, 3.4, 3.9–3.10, 3.16, 5.4 y 9.1–9.3 | Número y texto comprobados; definiciones y finalidad citadas tienen respaldo. El art. 5.4 excluye obras del sector transportes; 9.3 contempla interoperabilidad y 9.1 remite a CE.040. Se deroga DS 016-2018-VIVIENDA. La aplicabilidad exige conocer jurisdicción y sistema. No se certificó ausencia de toda modificación posterior. |

**URL de acceso de F001:** https://store.astm.org/d6433-18.html ; versión que el catálogo señala activa: https://store.astm.org/d6433-24.html . Consulta parcial, sin compra ni redistribución de norma completa. El coordinador comunicó otra copia localizada en portal UMV; este agente no la abrió ni la declara revisada.

**F005:** página editorial https://revistaalconpat.org/index.php/RA/article/view/604 ; PDF leído https://www.scielo.org.mx/pdf/ralconpat/v13n2/2007-6835-ralconpat-13-02-220-es.pdf . Español, CC BY 4.0; DOI 10.21041/ra.v13i2.604. La página editorial tiene un título inglés diferente al del avance; conservar el título de la versión utilizada y registrar la variante, sin inventar una corrección editorial.

**F007:** https://portal.mtc.gob.pe/transportes/caminos/normas_carreteras/MTC%20NORMAS/ARCH_PDF/MAN_11%20HHD-2011.pdf . El enlace gob.pe heredado devolvió error 418; se abrió el PDF del propio MTC. Tiene 222 páginas; los números citados son los impresos y coinciden con la posición PDF en los apartados revisados. El índice presenta desfases en algunas secciones; usar la página del cuerpo.

**F009:** https://busquedas.elperuano.pe/dispositivo/NL/2520332-4 . Se leyó el HTML oficial del decreto y anexo. La interfaz contiene una línea ajena al título; la identificación se contrastó con el encabezado y el articulado.

## Hallazgos priorizados y criterio de cierre

| Hallazgo | Severidad y ubicación en avance | Efecto | Propuesta verificable |
|---|---|---|---|
| BF01. Falta texto operativo PCI y decisión de edición | **Bloqueante para F2/F3**, pp. 7, 9, 12–13 | No permite fijar unidades, criterios ni cálculo normativo reproducible. | Obtener acceso legítimo al texto elegido, documentar edición, leer procedimiento pertinente y aprobar unidad PCI antes de recolectar. |
| BF02. Aplicabilidad normativa sin clasificar | **Mayor**, pp. 3–4, 7 y 12 | Una referencia general no acredita exigibilidad de un parámetro en una avenida urbana. | Documentar clasificación y administración de la vía y conexión al sistema urbano. Drenaje debe contrastar CE.040 y el marco que resulte aplicable. |
| BF03. Antecedente correlacional requiere lectura crítica | **Mayor**, pp. 4, 6, 10–11 | El antecedente no valida el plan de Jaén. | Estadística debe revisar comparación de medias no pareadas y umbral 0.5 (§3.2 y tabla 10), sin copiarlo como contraste de asociación. Tablas 6/8 califican PCI 81 de forma incompatible con tabla 2: confirmar versión original antes de reutilizar baremos. |
| BF04. Bibliografía heredada no equivale a evidencia | **Mayor**, pp. 4–5 y 10–15 | Persiste contenido específico sin verificación integral. | Integrar estados diferenciados y mantener las afirmaciones en borrador hasta fichas de método y resultados. Un DOI y metadatos no bastan. |
| BF05. Brecha local aún no documentada mediante búsqueda reproducible | **Mayor**, p. 12 | La frase «no se identificó» no describe bases, fechas ni estrategia; no permite sostener exhaustividad. | Crear protocolo de búsqueda para Jaén/Cajamarca y variables equivalentes, criterios de inclusión, duplicados y resultados de búsqueda. |
| BF06. Referencia del plan municipal necesita precisión | **Menor bibliográfica**, pp. 5 y 15 | El enlace conduce al Resumen Ejecutivo del PDU 2013–2025; no se confirmó el año bibliográfico 2014. | Verificar fecha de aprobación/publicación y citar título de portada. Su uso es contexto histórico, sin extrapolar al estado de la avenida en 2026. |
| BF07. Inconsistencia entre resúmenes de tesis nacional | **Mayor para cifra**, p. 11, F011 | Los resúmenes ES/EN de USAT difieren en una dimensión de cuneta. | Mantener pendiente el número hasta revisar tabla/plano del texto completo; no resolver por traducción o mayoría de resúmenes. |

## Otras fuentes: alcance real de esta ronda

- **F002, F004, F006 y F012:** identidad, autores, título y publicación comprobados contra el registro del DOI en Crossref; respuestas JSON conservadas. Se buscaron páginas editoriales; varias devolvieron errores o limitaciones. No se declaran métodos, muestras ni conclusiones verificados por estos metadatos. F004 conserva revisión de contenido pendiente aunque el resumen editorial sea localizable. F006 tiene texto en PMC, pero la apertura dio comprobación de navegador. F012 dio 429 en MDPI.
- **F003:** el handle devolvió403. No se verificaron texto, PCI 39 ni atribución causal del antecedente. Sigue pendiente.
- **F008:** no verificada en esta auditoría acotada. No se buscó exhaustivamente su edición, vigencia ni su apoyo específico.
- **F010:** se descargó el PDF municipal de 128 p. y se leyeron portada y pasajes pertinentes. El apoyo contextual se localiza en p. PDF 40/p. impresa 33 (expansión sin previsión de drenaje) y p. PDF 91/p. impresa 84 (zonas bajas y drenaje). URL: https://munijaen.gob.pe/documentos/proyecto1/RESUMEN%20EJECUTIVO.pdf . Fecha bibliográfica 2014 pendiente; no se leyó todo el plan.
- **F011:** se abrió el registro USAT por su handle https://hdl.handle.net/20.500.12423/7471 , que redirigió a https://repositorio.usat.edu.pe/items/27825ffd-919d-4c37-8560-025802895acc . Título, autor Marc Anthony Torres Vasquez y fecha 2024 comprobados. Se leyeron metadatos y resúmenes, no tesis completa. El resumen ES presenta 0.50×0.60m y el EN 0.50×0.70m. La cifra del avance coincide con ES pero necesita confirmación en el documento.

Estos estados se proponen en `propuesta_verificacion.json`; no se modificaron `fuentes/registro.csv`, capítulos ni matrices compartidas.

## Preguntas que el coordinador debe pasar a otros perfiles

1. **Metodología y drenaje:** ¿qué evidencia documental clasifica el tramo y permite distinguir sistema de drenaje urbano y obras del sector transportes? Resuelve el alcance de F007/F009; no bloquea la revisión conceptual.
2. **Estadística:** ¿cómo codificar ausencia de un dispositivo, no aplicabilidad y condición deficiente sin imponer el cero del antecedente? ¿Cómo justificar asociación y dependencia espacial sin copiar comparación de medias? La escala debe derivarse de indicadores validados y unidades emparejables.
3. **Pavimentos y metodología:** ¿qué edición y tipo de pavimento se usarán y cómo se relaciona unidad PCI con cada subtramo? No imponer 80 m, 19 unidades ni una muestra mínima por imitación de F005.
4. **Fuentes y asesor, siguiente ronda:** ¿existe estrategia documentada que sostenga la brecha de Jaén? ¿Qué referencias son indispensables antes del piloto? La respuesta determinará prioridades de F1.

## Archivos, integridad y verificación

Se leyeron AGENTS.md, perfil, skill y referencia, configuración, estado, decisiones, protocolo, texto completo del avance, registro y contexto R001. Se verificaron hashes de los insumos congelados mediante lectura. Herramientas: búsqueda web, descarga HTTP de fuentes públicas, pypdf 6.10.0 y Python 3.12.14. Los accesos fallidos se mantienen como límites, no se sustituyen por supuesta lectura. `doctor` confirmó ausencia de ejecutable Codex; `verify` devolvió ok con avisos esperados de plan pendiente, referencias heredadas y ausencia de campo. Son controles estructurales, no aprobación científica.

Los PDF F005 y F007 y sus extracciones están en esta carpeta. `capturas_manifest.json` documenta las otras capturas, URLs finales, fallos y hashes. `inventario_evidencias.json` añade todos los hashes. Las extracciones son auxiliares: el original PDF o HTML gobierna ante errores. No se redistribuye el estándar ASTM íntegro. La copia de F005 se atribuye a Diniz y Melo (2023), ALCONPAT; español; licencia https://creativecommons.org/licenses/by/4.0/ ; PDF original sin cambios, extracción derivada. Los demás documentos conservan emisor, procedencia y condiciones de acceso sin presumir una licencia no comprobada.

## Recomendación al coordinador

Integrar los hallazgos y las localizaciones comprobadas. F005 puede respaldar la descripción acotada del antecedente, sin adoptar automáticamente su instrumento o sus pruebas; F007/F009 respaldan las afirmaciones localizadas, con aplicabilidad pendiente. Mantener F001 parcial y las demás referencias pendientes para el contenido no leído. Iniciar metodología/estadística con estas cautelas; no esperar a cerrar toda F1 para resolver unidades, viabilidad y riesgos del diseño. Conservar abierto el acceso PCI y el trabajo de campo.
