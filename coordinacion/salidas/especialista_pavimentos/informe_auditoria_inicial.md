# Auditoría inicial de pavimentos y PCI

**Tarea:** R001 — especialista_pavimentos. **Fecha:** 2026-10-14. **Fase:** F0. **Entradas:** versión 1.0.0, congeladas en `coordinacion/contextos/R001_insumos.json`.

## Respuesta al encargo

El PCI es coherente como indicador propuesto de condición superficial, pero todavía no existe un procedimiento de campo ejecutable para Pakamuros. No se conoce el material real del pavimento, la geometría del frente ni la correspondencia entre subtramo de investigación y unidad de inspección. Tampoco hay mediciones o cálculos que auditar. Estos vacíos bloquean cerrar el diseño, no impiden preparar instrumentos y resolver la estructura de trazabilidad.

El avance conserva correctamente el alcance correlacional y declara que valores mayores de PCI representan mejor condición. No procede atribuir los daños al drenaje ni anticipar el signo o significación de la asociación. La auditoría identifica siete observaciones; las dos primeras son bloqueantes y las restantes mayores. No se generaron resultados de campo.

Esta revisión se ejecutó mediante un subagente de esta sesión, con lectura de perfil y skill. No constituye una prueba del descubrimiento ni de la ejecución de agentes en el CLI del usuario; `doctor` no encontró ese ejecutable en este entorno.

## Evidencia consultada y alcance del acceso

Se leyó íntegramente `requisitos/avance_texto_extraido.txt`, de 15 páginas, y se comprobó que `avance_original.pdf` tiene 15 páginas y SHA-256 `947b2eb9d631236326de6f3ad211d6f2453a13d76ae6245b0f91c8778fbb8415`, coincidente con el expediente. Las páginas indicadas abajo corresponden a la numeración del PDF.

También se leyeron instrucciones generales, perfil, skill y referencia PCI, estado, decisiones, configuración, protocolo, criterios de fase, matriz de consistencia, operacionalización, escala de drenaje, plan de análisis, diccionario y todas las cabeceras CSV de campo. La operacionalización y las tablas de campo carecen de registros; el capítulo metodológico contiene pendientes.

Las comprobaciones externas se limitaron a fuentes primarias:

- **F001, consulta parcial:** [ficha oficial ASTM D6433-18](https://store.astm.org/d6433-18.html), apartados 1.1 y 4.1, identificación y versiones. Verifica el método de inspección visual para vías y estacionamientos y sus límites: el PCI no mide capacidad estructural ni proporciona mediciones directas de fricción o rugosidad. La ficha identifica esta edición como histórica. No se verificaron aquí las curvas ni el procedimiento completo.
- **PAV-EXT-01, ID provisional:** [ficha oficial ASTM D6433](https://store.astm.org/standards/d6433), encabezado y versiones; muestra D6433-24 como activa y actualización de 2024-11-15. Esto exige revisar la elección editorial, no invalida automáticamente la edición citada ni prueba obligatoriedad jurídica en Jaén.
- **PAV-EXT-02, candidato documental:** [PDF D6433-18 alojado por la UMV](https://www.umv.gov.co/sisgestion2023/Documentos/MISIONAL/PCI/PCI-DE-009_V1_Astm_6433_metodologia_del_calculo_de_pci_para_pavimentos.pdf). La apertura devolvió 47 páginas; la relectura del contenido agotó el tiempo. Su disponibilidad no equivale a lectura técnica, autenticación de integridad ni verificación del derecho de redistribución. No se incorporó al paquete ni se usó para calcular.

Consultas: 2026-10-14. Los IDs PAV-EXT son referencias locales de esta propuesta; el coordinador debe asignar IDs canónicos sin colisiones. F001 permanece con acceso parcial, no «norma completa verificada».

## Observaciones y resolución

### PAV-01 — Tipo de pavimento desconocido — Bloqueante

**Evidencia:** pp. 7–8 y 12–13 hablan de pavimento genérico; p. 11 distingue antecedentes de concreto y pavimento flexible en otras ciudades. Ninguno identifica el material de Pakamuros. `subtramos.csv` tiene el campo pertinente, sin valores.

**Efecto:** no se puede confirmar catálogo, cuantificación, delimitación de unidades ni compatibilidad del procedimiento elegido. No debe trasladarse la identificación de un antecedente al ámbito investigado.

**Resolución:** reconocimiento con fecha, croquis, coordenadas, fotos y registro de material; señalar cambios de superficie, reparaciones y sectores que requieran revisión. Consultar el procedimiento completo para el material observado. Si existen superficies diferentes, proponer tratamiento separado antes de cualquier agregación. **Cierre:** inventario verificable y decisión metodológica documentada; no basta seleccionar «flexible» en un formulario.

### PAV-02 — Subtramo y unidad PCI sin correspondencia — Bloqueante

**Evidencia:** p. 8 propone subtramos de longitud equivalente, continuos, definidos durante el reconocimiento. No da longitud total, ancho, calzada, carriles, secciones homogéneas ni número de unidades. La matriz declara «subtramo por definir y revisar».

**Efecto:** no existe todavía un par observacional reproducible drenaje–pavimento. Una longitud igual no demuestra compatibilidad con la unidad del método. Copiar una exposición común a varias unidades podría aparentar más observaciones independientes de las disponibles.

**Resolución:** conservar la propuesta de continuidad sin seleccionar por daño, levantar geometría y dibujar dos delimitaciones: subtramos de investigación y unidades de inspección. Elaborar tabla de correspondencia, cobertura y regla de integración. Si una unidad atraviesa límites, resolverlo antes del campo; no duplicar su PCI. Metodología y estadística deben valorar cuántas exposiciones distinguibles existen y si el ámbito permite la pregunta planteada. **Cierre:** mapa y regla aprobados, número viable y dependencia evaluada; no se fija aquí un tamaño mínimo o una longitud universal.

### PAV-03 — Edición y procedimiento completo sin cerrar — Mayor

**Evidencia:** pp. 7 y 14 citan D6433-18; el registro F001 está pendiente. La ficha editorial actual muestra una edición posterior activa.

**Efecto:** citar nombre y DOI no demuestra que se disponga de instrucciones, definiciones y herramientas completas para reproducir la evaluación. Mezclar versiones impediría reconstruir el resultado.

**Resolución:** verificar acceso legítimo, edición, alcance y compatibilidad con el pavimento observado. Documentar con el asesor la edición de trabajo y consultar sus apartados operativos completos. Conservar referencias precisas al respaldo utilizado. **Cierre:** ficha técnica y decisión de edición; ninguna curva o tabla se reconstruye de memoria. Esta observación puede resolverse parcialmente mediante la fuente candidata; su lectura aún está pendiente.

### PAV-04 — Cadena de cálculo incompleta — Mayor

**Evidencia:** pp. 7 y 12–13 prevén tipo, severidad y densidad; `fallas.csv` conserva cantidades, mientras `pci.csv` registra área y resultado. No existen fichas de medición, geometría de cada unidad ni hojas de cálculo reales.

**Efecto:** un PCI ingresado manualmente podría pasar el control de rango sin demostrar su origen. `origen_calculo` ayuda, pero necesita apuntar a un respaldo identificable. Debe comprobarse si el área es el denominador suficiente para el material y procedimiento seleccionados.

**Resolución:** añadir al instrumento provisional identificación espacial de unidad, mediciones originales, unidad de cantidad, denominador aplicable y referencia del criterio usado. Cada cálculo deberá enlazar con registros de fallas, procedimiento, archivo y revisión. Véase `propuesta_registro_pci.md`. **Cierre:** un cálculo piloto real puede repetirse por otro revisor desde los originales; este informe no lo simula.

### PAV-05 — Sentido del indicador necesita conservarse en toda la cadena — Mayor

**Evidencia:** p. 13 establece correctamente «valores más altos expresan mejor condición superficial». Título y objetivos utilizan «deterioro»; el plan propone `y: pci`, sin transformación, y drenaje crece con deficiencia.

**Efecto:** rotular PCI como deterioro creciente invertiría la interpretación verbal. El problema reside en la futura coherencia del informe, no en un error numérico ya observado.

**Resolución:** escribir «condición superficial medida con PCI» al describir el indicador y recordar su dirección en tablas, figuras e interpretación. No transformar automáticamente a `100−PCI`. Si se propone transformar, registrar variable, motivo y consecuencias antes del análisis. **Cierre:** diccionario, matriz, hipótesis y leyendas consistentes; ningún signo se predetermina.

### PAV-06 — Emparejamiento hidráulico y temporal no operacionalizado — Mayor

**Evidencia:** p. 8 exige fecha y condiciones meteorológicas; p. 12 enumera elementos de drenaje, obstrucciones y empozamiento. No hay mapa de qué elementos o flujos corresponden a cada superficie.

**Efecto:** proximidad visual no garantiza que dos registros describan la misma exposición. Una inspección seca tampoco acredita ausencia de empozamiento en lluvia. Incluir baches o fisuras dentro del índice de drenaje contaminaría la comparación propuesta.

**Resolución:** acordar con drenaje identificación de lado, calzada, elementos relacionados, área de observación y momento de medición. Registrar exposición compartida y conexiones aguas arriba sin afirmar capacidad hidráulica medida. Definir cómo se tratarán visitas adicionales. Mantener por separado el daño observado y la deficiencia de drenaje. **Cierre:** reglas de correspondencia y tiempo en ambos instrumentos, con faltantes explícitos.

### PAV-07 — Control del observador y límites interpretativos pendientes — Mayor

**Evidencia:** pp. 8–9 reconocen límites de inspección y prevén validación; pp. 3 y 13 mencionan factores concurrentes y alcance no causal. Aún no hay protocolo de entrenamiento ni piloto.

**Efecto:** diferencias de clasificación o medición podrían confundirse con variación espacial. Las fotos facilitan revisión, pero no sustituyen todas las mediciones. Una correlación no identifica daño de base, saturación interna ni mecanismo causal.

**Resolución:** preparar capacitación con la edición elegida, piloto y revisión de concordancia apropiada a los datos. Registrar desacuerdos y correcciones con originales conservados. Contextualizar tráfico, antigüedad y mantenimiento únicamente con evidencias disponibles. **Cierre:** instrumento versionado, resultados reales del piloto y límites expresos; no inventar número de expertos, coeficientes ni umbrales.

## Preguntas para los otros especialistas

| Destinatario | Pregunta concreta y evidencia necesaria |
|---|---|
| Metodólogo | ¿Cómo compatibilizar subtramos equivalentes del avance con unidades PCI y heterogeneidad real? Necesita inventario y croquis. |
| Estadístico | ¿Cuál será la observación independiente cuando varios subtramos compartan drenaje? Necesita mapa de exposición y geometría; no tomar número de fotos o fallas como n. |
| Drenaje | ¿Qué área y elementos describen la exposición de cada unidad, y cómo registrar conexiones compartidas? Necesita reconocimiento conjunto. |
| Metodólogo y estadístico | ¿Cómo integrar varias unidades PCI en un subtramo y cómo tratar visitas repetidas sin aumentar artificialmente n? Necesitan regla previa, cobertura y campaña. |
| Investigador de fuentes | ¿Puede recuperarse y revisarse la norma completa de trabajo y documentarse la elección de edición? Necesita texto accesible y referencia verificable. |

## Verificación y recomendación al coordinador

`python tools/tesis.py doctor`: Python compatible; Codex CLI no localizado. `python tools/tesis.py verify`: `ok: true`, con avisos esperados por plan pendiente, fuentes no verificadas y ausencia de originales de campo. La comprobación de páginas y hash con `pypdf` y `hashlib` fue coincidente. Estos controles no validan instrumentos ni investigación.

Integrar los siete hallazgos en el expediente F0 y pasar las preguntas a metodología y estadística. Incorporar el registro propuesto como borrador revisable. Mantener F2 abierto hasta resolver geometría, procedimiento, emparejamiento y viabilidad. No modificar el original, adjudicar resultados ni presentar esta revisión como inspección física del frente hospitalario.
