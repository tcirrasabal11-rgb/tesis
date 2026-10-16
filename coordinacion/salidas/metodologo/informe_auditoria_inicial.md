# Auditoría metodológica inicial — R001

**Agente:** metodologo. **Fecha:** 2026-10-14. **Entradas:** versión 1.0.0, manifiesto R001 y pase técnico 2. **Fase auditada:** F0; propuestas para F2/F3. **Estado:** auditoría documental, sin aprobación del diseño.

## Respuesta al encargo

El avance conserva correspondencia entre pregunta general, dos preguntas específicas y sus objetivos. El diseño aplicado, cuantitativo, correlacional, no experimental y transversal puede mantenerse como planteamiento. Todavía no está demostrada su viabilidad: faltan límites medidos, material del pavimento, unidades compatibles, exposición de drenaje distinguible y una medición operacional validada. La existencia de perfiles, matrices o pruebas informáticas no resuelve esos requisitos.

Esta revisión la ejecutó un **subagente de esta sesión**, con el perfil y la skill del proyecto. No demuestra descubrimiento de agentes en el CLI local del usuario. No hubo visita, medición, aprobación del asesor, validación de expertos ni inferencia estadística. El coordinador integra las propuestas; este informe no modifica documentos canónicos.

## Evidencia e interacción entre agentes

Se leyó el avance de 15 páginas, mediante su extracción completa: pp. 3 y 8 fijan alcance; pp. 5–6 preguntas y objetivos; pp. 7–9 medición, ámbito y viabilidad; pp. 12–13 variables y límites. Se contrastaron matriz, operacionalización, escala, plan analítico, diccionario y registros de campo. La operacionalización y los CSV revisados no contienen observaciones; el capítulo metodológico conserva pendientes.

Se incorporaron los informes y propuestas de drenaje y pavimentos congelados en `R001_ronda2_inicial.json`, y después del aviso del coordinador se leyeron el informe final de fuentes y `propuesta_verificacion.json`. El SHA-256 del informe de fuentes es `14e84e248d44b5db59c2ca5558a0ff68f54c545f1d57a88ac5f5d371f02aea66`; sus estados son propuestas todavía no integradas al registro canónico. El manifiesto adjunto conserva los hashes y las comprobaciones.

Del investigador se adopta apoyo **acotado**: F005, §3 y tablas 8–11, permite describir el antecedente; no transferir 19 tramos, 80 m, puntuación de ausencias o contraste de medias. F001 sigue limitada al catálogo, sin procedimiento completo PCI. F007 y F009 aportan definiciones localizadas; su aplicabilidad exige clasificación y jurisdicción. No se presentan estos aportes como una segunda consulta externa independiente del metodólogo.

## Hallazgos y condiciones de cierre

| ID / gravedad | Evidencia y efecto | Resolución y cierre verificable |
|---|---|---|
| MET-01 — Bloqueante F2 | Avance p. 8 y PAV-01/02: ámbito sin geometría ni material; subtramo y unidad PCI no equivalen automáticamente. | Reconocimiento completo, croquis, inventario de material y tabla de correspondencia drenaje–PCI. Documentar cobertura y dependencia antes de justificar unidades y número viable. |
| MET-02 — Bloqueante F2/F3 | DRE-01/06 y escala: sin indicadores, aplicabilidad, agregación ni faltantes; no hay puntaje reproducible. | Definir contenido y reglas con fuentes pertinentes, revisión real y piloto. Ninguna escala, peso o penalización queda aprobada aquí. |
| MET-03 — Mayor | Objetivo específico 2 y DRE-08: observación de residuos no mide gestión o frecuencia histórica del mantenimiento. | Mantener dimensión operatividad/mantenimiento; distinguir condición observable de información documental. Someter al asesor el alcance operativo y cualquier ajuste de redacción. |
| MET-04 — Mayor | PAV-05 y avance p. 13: PCI creciente significa mejor condición, mientras el título habla de deterioro. | Conservar PCI original y explicar su dirección en matriz, hipótesis, tablas y discusión. No transformar automáticamente a 100−PCI ni anticipar signo. |
| MET-05 — Mayor | DRE-03/07: evacuación sin ubicación y agua retenida con mecanismo desconocido. | Integrar provisionalmente continuidad/conexión de evacuación en captación/conducción; mantener empozamiento como contexto hasta resolver validez y circularidad. Cierre con mapa de constructo e indicadores aceptados. |
| MET-06 — Mayor | Avance pp. 8–9 y PAV-06/07: falta ventana temporal y control de observadores. | Protocolo de campaña, lluvia antecedente, visitas complementarias y entrenamiento; piloto con discrepancias conservadas y concordancia pertinente. Visitas repetidas no aumentan n por defecto. |
| MET-07 — Mayor | BF02/05: marco normativo y brecha local insuficientemente delimitados. | Obtener clasificación/administración de vía, relación con sistema urbano y búsqueda local reproducible. F009 art. 5.4 impide asumir inclusión de toda infraestructura vial; no se emite conclusión jurídica de aplicabilidad. |

## Matriz de consistencia propuesta

El ámbito común de las tres filas es **avenida Pakamuros frente al Hospital General de Jaén, 2026**, con límites pendientes de medir. Debe escribirse completo en la matriz definitiva para evitar que «ámbito definido» oculte delimitaciones diferentes.

| Nivel | Pregunta y objetivo correspondientes | Variables / datos necesarios | Hipótesis candidata y análisis |
|---|---|---|---|
| General | ¿Qué relación existe entre deficiencias de drenaje y deterioro superficial? Establecer esa relación. | Valor global de drenaje validado, PCI y fallas originales del mismo ámbito. | Alternativa no direccional de asociación distinta de cero, frente a ausencia de asociación según el parámetro elegido. Estimación y contraste solo con plan justificado. |
| Específico 1 | ¿Qué relación existe entre captación/conducción y deterioro? Establecer esa relación. | Puntuación dimensional validada y el mismo PCI emparejado. | Igual formulación no direccional para esta dimensión; revisión de familia de comparaciones. |
| Específico 2 | ¿Qué relación existe entre operatividad/mantenimiento y deterioro? Establecer esa relación. | Puntuación dimensional validada, documentos separados de mantenimiento y el mismo PCI. | Igual formulación no direccional, condicionada al alcance realmente medido. |

Son propuestas, no resultados ni hipótesis aprobadas. Si las mediciones resultantes no permiten representar una dimensión o construir el índice general, no debe conservarse una fila sin datos ni sustituirse por un puntaje improvisado. Se devuelve esa incompatibilidad al asesor antes del campo definitivo.

El coordinador trasladó la revisión estadística: coincide con hipótesis bilaterales y empozamiento como contexto provisional. No transferir el contraste no pareado/umbral 0.5 de F005. El motor Spearman usa p asintótica; unidades reducidas o dependencia requieren revisar su pertinencia y posibles extensiones antes de inferencia. Pearson/Spearman permanecen pendientes.

La operacionalización requiere definición conceptual y operativa, indicador, dimensión, método, unidad/escala, aplicabilidad, fuente y evidencia. La geometría accesible, continuidad visible y obstrucciones de la ficha de drenaje son candidatos de registro bruto, todavía no indicadores puntuables. PCI requiere tipo/severidad/cantidad, denominadores correspondientes y respaldo del cálculo según la edición elegida. Las fallas nunca integran el predictor de drenaje.

## Respuestas explícitas a especialistas

**Drenaje — ¿Deficiencia observable o gestión del mantenimiento?** El avance p. 12 define condiciones observables; ese es el objeto operativo inicial. Los documentos de intervenciones pueden complementar contexto, sin inferir gestión desde limpieza visible. Si se desea medir gestión, hacen falta definición, fuentes y decisión del asesor; no se añade silenciosamente otra variable.

**Drenaje — ¿Dónde ubicar evacuación?** Mantener dos dimensiones. Ubicar continuidad física y conexión visible hacia salida dentro de captación/conducción; obstáculos y condición observable del componente, dentro de operatividad/mantenimiento. Registrar un hecho una vez y evitar penalizarlo por duplicado. Esa asignación se valida con mapa de indicadores.

**Drenaje — ¿Cómo tratar componentes alternativos?** Inventariar primero la solución real. Presencia, ausencia observada, alternativa, no aplicable y desconocido son estados diferentes. La ausencia solo recibe valoración cuando una regla sustentada establece la función requerida y cómo se satisface. Se rechaza copiar el cero de F005. No normalizar denominadores diferentes sin justificar comparabilidad con estadística.

**Pavimentos — ¿Cómo compatibilizar subtramos equivalentes, unidades PCI y heterogeneidad?** Mantener continuidad y selección ajena al daño. Mapear por separado subtramos, superficies y unidades del procedimiento disponible. Si la heterogeneidad hace incompatibles límites iguales, formular alternativas documentadas: conservar límites con unidades internas compatibles o proponer cambio de segmentación al asesor. No dividir una unidad ya evaluada ni duplicar su PCI para adaptar fronteras.

**Pavimentos y estadística — ¿Cómo integrar varias unidades PCI y visitas?** Conservar todos los resultados originales, cobertura y vínculos. La regla de síntesis requiere procedimiento completo, geometría, selección y propósito analítico; no se autoriza aquí media simple ni ponderada. Una visita adicional puede completar o repetir medición, identificando su función; no crea automáticamente otra observación independiente en el estudio transversal. Exposiciones compartidas se identifican y pasan al estadístico antes de formar pares.

**Fuentes — ¿Qué evidencia clasifica la vía y qué edición usar?** Inventario vial o acto/documento de la entidad competente que identifique clasificación y administración, junto a planos o documentos del drenaje urbano cuando existan. La fachada hospitalaria no prueba jurisdicción. La edición PCI debe decidirse con material real, acceso legítimo y asesor; la vigencia editorial no reemplaza pertinencia técnica.

## Validación, límites y expediente al asesor

La validación de contenido debe conservar expertos reales, versión revisada, criterios, observaciones y correcciones. El piloto comprueba medibilidad, instrucciones, registro temporal y concordancia pertinente; no se fija aquí número de expertos, coeficiente ni umbral. La aplicación local del procedimiento PCI necesita preparación y control; no se declara que un juicio de expertos haya validado nuevamente el estándar. No imponer alfa de Cronbach a una ficha heterogénea sin justificar el modelo de medición.

Tráfico, antigüedad, materiales, reparaciones, mantenimiento y clima se registran con fuente, fecha y estado desconocido cuando proceda. Mencionarlos no los controla; cualquier ajuste depende de datos, unidades y plan estadístico. El resultado se limitará al frente observado y campaña definida; un censo local no demuestra independencia ni autoriza generalización a Jaén.

Se entrega `propuesta_decisiones_metodologicas.md` con alternativas, evidencia necesaria y aceptación pendiente. El coordinador debe pasar estas reglas a estadística y devolver la ficha a drenaje/pavimentos para corrección. **F2 y F3 permanecen abiertas.** La auditoría puede integrarse en F0 al verificar sus entradas; cerrar diseño requiere expediente y validación reales, no este informe.

## Archivos y comprobaciones

Entregables en esta carpeta: informe, propuesta de decisiones e `insumos_revisados.json`. Se verificaron los siete hashes de R001 y los cuatro técnicos del pase 2: coincidencias completas; original de 15 páginas conservado. `python tools/tesis.py doctor` identificó Python compatible y ausencia de CLI Codex. `python tools/tesis.py verify` devolvió `ok: true`, con avisos esperados de plan, fuentes y campo pendientes. Estos controles son estructurales y no certifican la metodología.
