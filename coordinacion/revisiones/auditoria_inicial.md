# Auditoría inicial integrada de la tesis — R001

Fecha: 2026-10-14. Versión de entrega: 1.1.0. Estado del documento: auditoría documental R001 cerrada, con revisión académica de IA. Esta auditoría no es una aprobación del asesor ni una tesis terminada.

## Resultado

El avance proporciona tema, ámbito inicial, preguntas, objetivos, justificación y antecedentes. Permite continuar una investigación correlacional transversal sobre drenaje y pavimento. No permite todavía recoger datos definitivos o ejecutar inferencia: faltan geometría y material del pavimento, correspondencia entre unidades, medición operacional del drenaje y decisiones de diseño con respaldo.

Se conserva sin cambios el PDF recibido como **avance de tesis.pdf**, guardado en `requisitos/avance_original.pdf`: quince páginas; SHA-256 `947b2eb9d631236326de6f3ad211d6f2453a13d76ae6245b0f91c8778fbb8415`. La extracción es un auxiliar; ante discrepancia gobierna el PDF. No se modificaron el ámbito, los objetivos ni las dos dimensiones del documento original.

## Trabajo realmente ejecutado

El coordinador aplicó el protocolo y la skill de orquestación. Primera ronda: fuentes, drenaje y pavimentos revisaron las mismas entradas. Segunda ronda: metodología y estadística leyeron esas salidas y respondieron sus preguntas; las observaciones se devolvieron a los especialistas técnicos. Tercera ronda: revisión académica del conjunto integrado. Los encargos y hashes están en `coordinacion/contextos/`; los informes y addenda están en `coordinacion/salidas/`.

| Perfil | Aporte que debe consultarse |
|---|---|
| investigador_fuentes | Identidad, acceso, apoyo localizado, copias y límites de las doce referencias. |
| especialista_drenaje | Ocho hallazgos; propuesta de observables sin pesos ni puntajes inventados. |
| especialista_pavimentos | Siete hallazgos; propuesta de trazabilidad de unidades, fallas y cálculo PCI. |
| metodologo | Siete hallazgos, respuestas a especialistas y diez decisiones propuestas al asesor. |
| estadistico | Seis hallazgos, crítica del antecedente, límites del motor y decisiones analíticas pendientes. |
| revisor_academico | Comprobación final del expediente y de la distinción entre evidencia, propuestas y pendientes. |

Los subagentes se ejecutaron en el entorno de esta sesión, con los perfiles y procedimientos del proyecto como instrucciones. Esto prueba una aplicación de sus responsabilidades y su coordinación; **no prueba que el Codex CLI/IDE del usuario ya haya descubierto esos archivos**. El ejecutable `codex` no está disponible en este entorno. La prueba de arranque local se mantiene explícitamente pendiente.

## Hallazgos integrados que gobiernan el siguiente trabajo

| Prioridad / ID | Evidencia y efecto | Qué permite resolverlo |
|---|---|---|
| Bloqueante — R001-01: ámbito y unidades | Avance p. 8; DRE-02, PAV-01/02, MET-01 y EST-01. Faltan límites, ancho, material y mapa PCI–subtramo–drenaje. Dividir una vía no demuestra independencia. | Reconocimiento continuo del frente, croquis, coordenadas, material y componentes compartidos; regla de emparejamiento revisada. |
| Bloqueante — R001-02: medición de drenaje | Avance pp. 7 y 12; DRE-01/06, MET-02 y EST-02. No hay escala puntuable con reglas de aplicabilidad y agregación. | Indicadores sustentados, orientación, faltantes, ausencia/no aplicable y denominadores; revisión real y piloto del instrumento. |
| Bloqueante — R001-03: procedimiento PCI | PAV-03/04, BF01 y EST-03. El catálogo no contiene el método operativo completo ni valida el cálculo. | Edición elegida, acceso y lectura del procedimiento pertinente, tipo de pavimento y cálculo piloto reconstruible. No recrear curvas. |
| Mayor — R001-04: campo y análisis | Avance pp. 8–9; EST-04/05. No hay campaña, observaciones ni plan aprobado; el software valida solo parte de la trazabilidad. | Protocolo temporal, originales, instrumento/PCI válidos, estimando, dependencia e inferencia justificados. |
| Mayor — R001-05: contenido de las dimensiones | Avance pp. 6–7 y 12; DRE-03/07/08, MET-03/05. Evacuación, empozamiento y mantenimiento requieren definición. | Mapa de constructo sin doble conteo ni daños de pavimento dentro del predictor de drenaje. |
| Mayor — R001-06: normativa | BF02, MET-07. Una referencia general no acredita aplicación específica a la avenida. | Clasificación y administración de la vía, configuración del sistema urbano y revisión técnica de alcance. |
| Mayor — R001-07: antecedentes y brecha | BF03/04/05/07. Un antecedente semejante no valida método, puntajes, muestra ni contraste; la brecha local no tiene búsqueda reproducible. | Fichas por afirmación, lectura crítica y protocolo de búsqueda con bases, fechas, criterios y resultados. |
| Menor — R001-08: presentación del avance | Introducción p. 3 anuncia cinco antecedentes y pp. 10–11 presentan seis; índice p. 2 no enumera términos básicos de p. 13. | Corregir en una versión de trabajo tras decidir el esquema institucional; conservar el original. |

Estas prioridades no obligan a detener todo el proyecto. La revisión bibliográfica, el expediente metodológico y la preparación de registros pueden avanzar mientras se obtiene evidencia de campo y de la universidad.

## Bibliografía: qué se verificó y qué no

La integración conserva el registro heredado anterior como histórico. Se actualiza el registro de trabajo con estados separados y fichas de las doce referencias. F005, F007 y F009 tienen apoyo **acotado a afirmaciones y localizaciones expresas**; esto no habilita cualquier afirmación futura sobre esos documentos. F001 y otras cinco referencias cuentan con comprobaciones de metadatos o resumen, F010 con apoyo contextual parcial y F003/F008 siguen pendientes.

- **F005:** se leyó el artículo español completo, con copia CC BY 4.0 y atribución. Respalda la descripción limitada del antecedente de diecinueve tramos y asociación débil. Sus decisiones de codificación y análisis no se transfieren al proyecto. Estadística contrastó directamente el método y las tablas; la comparación de medias que describe el antecedente no sustituye un contraste de asociación.
- **F007:** se consultó el manual oficial y sus apartados pertinentes. Sirve para principios técnicos localizados, sin convertirse por sí solo en escala de inspección ni en obligación específica aplicable al tramo.
- **F009:** se consultaron decreto y reglamento oficiales. Las definiciones y finalidad revisadas tienen respaldo. La aplicabilidad a esta infraestructura y una revisión exhaustiva de modificatorias siguen pendientes; no se emite una conclusión jurídica para Jaén.
- **F001:** se consultó el catálogo editorial, que distingue la edición citada de la activa. No se distribuye ni se declara leído el procedimiento completo. La elección de edición requiere justificación y acceso.

Las rutas, páginas y límites están en `fuentes/registro.csv`, `fuentes/fichas/`, `fuentes/afirmaciones.csv` y en el informe de bibliografía. `fuentes/referencias.json` contiene únicamente entradas con metadatos contrastados para las tres fuentes de apoyo localizado. Los capítulos siguen siendo borradores por completar; estas comprobaciones no rellenan resultados.

## Propuestas convergentes, todavía sin aprobar

Se mantienen las dos dimensiones del avance. Metodología propone ubicar continuidad/conexión de evacuación en captación/conducción, y registrar obstáculos y condición observable dentro de operatividad/mantenimiento. La gestión documentada del mantenimiento se separa de la limpieza visible. El empozamiento queda inicialmente como contexto, sujeto a revisión de validez y circularidad. Los addenda técnicos responden a estas propuestas; no constituyen validación por expertos.

PCI conserva su orientación: un valor mayor expresa mejor condición. No se transforma automáticamente a `100−PCI`, ni se anticipa signo o significación. Las hipótesis bilaterales no direccionales son candidatas; población, parámetro y método se precisarán al cerrar la medición y la viabilidad.

Fotos, tipos de falla, sumideros y visitas no aumentan automáticamente el número de observaciones independientes. Un censo del frente tampoco autoriza generalizar a toda Jaén. No se autoriza una media PCI simple o ponderada sin procedimiento, cobertura y objetivo definidos. Si el reconocimiento revela información insuficiente, se formula una alternativa al asesor antes de cambiar el ámbito.

## Configuración y controles de software

Se contrastaron las páginas oficiales de Subagents, Configuration Reference y Build skills el 2026-10-14. Se conservaron los seis perfiles independientes y las nueve skills. Se retiró `sandbox_mode` de los perfiles: los subagentes heredan los permisos del hilo principal, por lo que esa clave no creaba aislamiento propio. Se corrigió la guía y se añadió una prueba de regresión al verificador.

La batería completa registra **41 pruebas correctas** en `R001_pruebas_software.txt` y `.json`. Estadística registra once controles selectivos adicionales. Los CSV reales vacíos se rechazan correctamente: no se produjeron correlaciones o resultados aparentes. La validación final de estructura y citas se registra por separado antes del empaquetado.

El motor ofrece Pearson/Spearman con opciones delimitadas; no implementa por sí mismo un análisis espacial ni resuelve una escala inválida. Su inferencia predeterminada requiere revisión conforme a la muestra y el diseño. Si se necesita una extensión, se implementa y verifica antes de usarla. Las pruebas informáticas no acreditan datos, instrumentos, aprobación académica ni validez inferencial.

## Próximos entregables y dependencia real

1. **Requisitos institucionales:** guía, rúbrica, plantilla y observaciones del asesor. El usuario puede añadirlos siguiendo `docs/AGREGAR_DOCUMENTOS.md`; el coordinador registra e integra.
2. **Expediente de viabilidad:** reconocimiento del frente y tabla de correspondencia. Lo produce el trabajo de campo real; los especialistas revisan el diseño con esa evidencia.
3. **Instrumentos y plan:** criterios, edición PCI, piloto, control de observadores y análisis. Las propuestas de esta ronda son material para revisión, no decisiones aprobadas.
4. **Bibliografía pendiente:** recuperar textos que faltan, resolver discrepancias y documentar la brecha local. No es necesario inventar fuentes para llenar capítulos.

`PREGUNTAS_AL_ASESOR.md` vincula preguntas con la decisión y la evidencia requerida. `ESTADO.md` y `coordinacion/tareas.csv` dejan el punto de continuación. F0 conserva requisitos pendientes; F2/F3/F5 y la entrega final permanecen abiertas. Lo completado en R001 es la auditoría documental y la preparación de trabajo verificable.

## Cierre de revisión

El revisor académico de IA concluyó que la plantilla está apta para continuar y no identificó bloqueantes de entrega del paquete. Dos incidencias menores se corrigieron: descripción de los estados bibliográficos en README y dependencias de tareas para evitar un ciclo con el cierre. Su informe está en `coordinacion/salidas/revisor_academico/informe_auditoria_inicial.md`.

Se cierra T001/R001 como auditoría documental. Se mantienen abiertas las decisiones científicas y F2/F3/F5/F7. Tras la revisión se actualizaron etiquetas transitorias y se prepararon metadatos de distribución para dos capturas web, con declaración en R001_alcance_copias.json. Los controles finales y el manifiesto registran exactamente la versión empaquetada.
