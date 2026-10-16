# Auditoría inicial de drenaje

**Tarea:** R001; **perfil aplicado:** especialista_drenaje; **fecha:** 2026-10-14; **fase:** F0; **entradas:** versión 1.0.0 de `coordinacion/contextos/R001_insumos.json`.

## Respuesta al encargo

El avance permite desarrollar una investigación sobre **deficiencias observables del drenaje**, pero todavía no contiene un instrumento aplicable ni evidencia de las condiciones del frente vial. Conviene conservar el ámbito, el diseño correlacional transversal y las dos dimensiones de la página 6. Para continuar se necesitan un reconocimiento documentado, reglas de observación y una correspondencia explícita entre componentes de drenaje y subtramos. La apariencia de un elemento no autoriza a declarar insuficiencia hidráulica, humedad interna ni causalidad del deterioro.

Esta revisión fue ejecutada por un **subagente de esta sesión**, siguiendo el perfil y la skill incluidos en el proyecto. No demuestra que el CLI de Codex del usuario descubra esos archivos. No hubo visita, medición, juicio de expertos ni aprobación del asesor.

## Evidencia revisada

Se leyó el avance original de 15 páginas y su extracción. Las páginas 3 y 8 fijan el diseño y sus límites; 5-6 describen variables, preguntas y objetivos; 7-9 delimitan procedimientos; 12-13 ofrecen definiciones preliminares. Las referencias de 14-15 son antecedentes documentales cuya verificación completa corresponde a bibliografía.

Se contrastaron `config/proyecto.yaml`, `config/plan_analisis.yaml`, `metodologia/matriz_consistencia.csv`, `metodologia/escala_drenaje.yaml`, `capitulos/04_metodologia.md` y `datos/campo/drenaje.csv`. La escala carece de indicadores, agregación y regla de faltantes; metodología contiene pendientes y el CSV de drenaje solo tiene cabecera. Esto acredita ausencia de registros en el paquete, no ausencia de drenaje en Pakamuros.

**Fuente primaria externa consultada:** F009, [DS 009-2026-VIVIENDA y su reglamento, El Peruano](https://busquedas.elperuano.pe/dispositivo/NL/2520332-4), publicación indicada 29/05/2026; consulta 14/10/2026. Se leyeron los artículos 1-3 del decreto y, del reglamento, artículo 2 y numerales 3.4, 3.9-3.10 y 3.15-3.17. Estos apartados permiten contrastar las definiciones de infraestructura, escorrentía y mantenimiento. No se hizo una revisión exhaustiva de modificatorias, obligaciones locales ni parámetros técnicos de diseño. No se modificó el estado canónico de F009.

## Hallazgos priorizados

### DRE-01. La variable explicativa todavía no puede puntuarse

**Bloqueante para F3-F5. Evidencia:** páginas 7 y 12: la ficha y sus indicadores se elaborarán y validarán; `escala_drenaje.yaml`: indicadores vacíos y método de agregación nulo.

**Efecto:** actualmente no existe un valor reproducible de deficiencia general ni por dimensión para correlacionar con PCI. Un puntaje improvisado introduciría decisiones posteriores a observar daños.

**Propuesta:** usar la ficha provisional adjunta para definir el registro bruto. Con metodología, fuentes y expertos se justificará después qué observables son indicadores, cómo se orientan y agregan y qué información queda solo como contexto. **Cierre:** instrumento versionado con fundamento, reglas de aplicabilidad, evidencia de revisión y piloto real. No convertir categorías descriptivas en una escala validada.

### DRE-02. Falta una unidad de exposición de drenaje emparejable

**Bloqueante para F2-F5. Evidencia:** página 8 propone subtramos de longitud equivalente, sin longitudes ni inventario; página 9 solo enumera recursos disponibles.

**Efecto:** un mismo sumidero, cuneta o descarga podría servir a varios subtramos. Copiar su calificación en todos no crea exposiciones independientes. Tampoco se sabe si habrá variación observable suficiente dentro del frente vial.

**Propuesta:** levantar el frente completo y sus conexiones visibles, asignar IDs a componentes y dibujar la relación componente-subtramo, lado de vía y dirección de escurrimiento comprobable. Registrar conexiones desconocidas. Conservar la selección continua y sin elegir por daño. **Cierre:** croquis verificable, límites, inventario y regla conjunta de emparejamiento revisada por estadística y pavimentos.

### DRE-03. Evacuación necesita ubicación explícita dentro de las dos dimensiones

**Mayor. Evidencia:** página 6 formula captación/conducción y operatividad/mantenimiento; páginas 5, 7 y 12 incluyen también evacuación.

**Efecto:** puede omitirse una función relevante o contar dos veces el mismo problema.

**Propuesta:** conservar las dos dimensiones. Como alternativa a validar, ubicar continuidad física y conexión visible hacia la salida en captación/conducción; registrar residuos u obstáculos en operatividad/mantenimiento. La falta de acceso a la descarga se codifica como información desconocida. Una interrupción con residuos tiene un solo registro del hecho y mecanismos diferenciados; no dos penalizaciones automáticas. **Cierre:** definición de cada indicador y mapa dimensión-función, aceptados por metodología antes de puntuar.

### DRE-04. El momento de visita puede confundirse con la condición de drenaje

**Mayor. Evidencia:** páginas 8-9 reconocen diferencias entre lluvia y estiaje y piden fecha y condición climática, sin procedimiento temporal.

**Efecto:** calzada seca no demuestra evacuación satisfactoria; agua presente puede proceder de lavado, fuga o lluvia. Un mantenimiento reciente puede alterar la condición observada.

**Propuesta:** registrar hora, estado meteorológico, lluvia antecedente y su fuente, humedad de la superficie y limpieza reciente solo si hay evidencia. Si se observa agua, medir extensión y profundidad cuando sea seguro; su duración exige observaciones temporales identificadas. En visita seca registrar “sin agua observada”, no “sin empozamiento durante lluvia”. **Cierre:** protocolo común que defina ventana de visitas, fuente meteorológica y tratamiento de condiciones incomparables, sin seleccionar días por el resultado esperado.

### DRE-05. Pendiente aparente y obstrucción visible no prueban capacidad

**Mayor. Evidencia:** página 12 propone pendientes aparentes; páginas 7-8 excluyen diseño hidráulico y evaluación interna.

**Efecto:** un juicio visual podría presentarse erróneamente como comprobación cuantitativa del funcionamiento o como diagnóstico de subdimensionamiento.

**Propuesta:** describir continuidad y dirección visibles sin asignar porcentajes de pendiente. Si se incorpora una pendiente medida, declarar puntos, diferencia de cota, longitud, equipo y precisión, mediante decisión documentada. La capacidad requeriría otro expediente con geometría, aportes y condiciones hidráulicas; queda fuera de este diagnóstico. **Cierre:** retirar del instrumento preliminar etiquetas de capacidad “suficiente/insuficiente” sustentadas solo en apariencia.

### DRE-06. Ausencia, no aplicable y dato faltante no son equivalentes

**Mayor. Evidencia:** página 12 enumera componentes posibles; no afirma que todos estén presentes. La escala no define estas reglas.

**Efecto:** penalizar automáticamente la falta de sumidero o rejilla presupone una solución obligatoria que no se ha identificado; excluir componentes ausentes sin criterio también puede alterar comparaciones.

**Propuesta:** inventariar existencia observada, configuración alternativa, inaccesibilidad y desconocimiento. Determinar aplicabilidad según la solución identificada y su fundamento, antes de calificar deficiencia. Los registros sin inspección conservan motivo y fecha. **Cierre:** reglas de rutas del instrumento y denominadores comparables acordadas con metodología/estadística; no sustituir desconocidos por cero.

### DRE-07. Separar exposición, daño y explicación del empozamiento

**Mayor. Evidencia:** páginas 12-13 separan deterioros superficiales y drenaje, pero la definición de empozamiento incorpora explicaciones todavía no comprobadas.

**Efecto:** usar baches, fisuras o PCI para puntuar drenaje provocaría circularidad. Además, una depresión de la superficie puede retener agua; el agua observada no identifica por sí sola la dirección causal.

**Propuesta:** registrar acumulación de agua de forma descriptiva y mantener separada la interpretación de su mecanismo. Mapear la coincidencia con daños con IDs, sin incorporar esos daños al índice de drenaje. Evaluar con metodología si el empozamiento será indicador de funcionamiento observado o contexto complementario, y prever análisis alternativo si se justifica. **Cierre:** revisión cruzada por pavimentos y registro explícito de la decisión.

### DRE-08. Estado de limpieza no acredita historial de mantenimiento

**Mayor. Evidencia:** objetivo específico 2, página 6; F009, reglamento, numerales 3.15-3.17, distingue acciones correctivas, preventivas y operación.

**Efecto:** residuos visibles no prueban frecuencia de limpieza ni inexistencia de un programa; una apariencia limpia tampoco prueba mantenimiento periódico.

**Propuesta:** registrar material, localización y extensión de la obstrucción con fotografías. Separar estos datos de información documental sobre intervenciones y fechas, si se obtiene. No afirmar incumplimiento municipal desde la ficha visual. **Cierre:** distinguir “condición observable” de “gestión documentada”; revisar si el instrumento cubre realmente ambas partes del nombre de la dimensión.

## Instrumento y reconocimiento propuestos

`propuesta_instrumento.md` contiene una ficha preliminar de observables, unidades y evidencias, sin pesos ni puntuaciones. No reemplaza `escala_drenaje.yaml`. El reconocimiento debe cubrir todo el frente, registrar ambos bordes donde existan y documentar componentes compartidos. Las fotografías necesitan fecha, ubicación y vínculo al componente. No deben abrirse cámaras ni intervenir la vía para completar campos; la inaccesibilidad queda registrada, coherentemente con la observación sin intervención prevista en página 9.

El piloto verificará comprensión de definiciones, tiempo de recorrido, medibilidad, coincidencia entre observadores y completitud. Las discrepancias se conservan para revisar reglas. La evidencia del piloto y del juicio de expertos debe existir antes de afirmar validación; no hay resultados que permitan declararla ahora.

## Preguntas que debe pasar el coordinador

- **Metodología:** ¿la variable se define como deficiencia observable o incluye gestión del mantenimiento? ¿Dónde se ubica evacuación y cuál será la regla ante componentes alternativos? Requiere inventario y sustento de indicadores; bloquea escala definitiva.
- **Estadística:** ¿cómo tratar exposiciones compartidas, falta de variación, observaciones repetidas y denominadores diferentes? ¿Qué diseño permite interpretar la asociación dentro de un único frente? Requiere croquis y pares reales; bloquea inferencia.
- **Pavimentos:** ¿coinciden los espacios y fechas de ambas observaciones? ¿Algún indicador depende de baches o deformaciones usados en PCI? Requiere unidades PCI y ficha de drenaje; bloquea emparejamiento.
- **Fuentes:** identificar procedimiento aplicable a inspección urbana y evidencia que fundamente los observables. El manual MTC citado no se declara automáticamente obligatorio para esta vía. Requiere verificar edición, ámbito y texto pertinente.

## Verificación y recomendación

Se comprobaron por SHA-256 las siete entradas del manifiesto R001: todas coinciden. `python tools/tesis.py doctor` confirmó Python 3.12.14 y dependencias; no encontró ejecutable Codex. `python tools/tesis.py verify` devolvió `ok: true`, con avisos esperados de plan y referencias pendientes y ausencia de originales de campo. Es validación estructural, no académica.

Integrar estos hallazgos en F0 y pasar la ficha a revisión cruzada. Mantener F2-F5 abiertas donde dependen de campo y validación. El siguiente trabajo técnico útil es el inventario documentado y la decisión sobre unidades y aplicabilidad; no calcular correlaciones ni anticipar su signo con registros inexistentes.
