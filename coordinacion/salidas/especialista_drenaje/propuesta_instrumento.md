# Ficha preliminar de observación del drenaje

**R001 - versión 0.1 - 2026-10-14.** Propuesta para revisión de contenido y piloto. No validada; sin calificaciones, baremos, pesos ni índice calculable. Ninguna celda contiene una medición realizada en Pakamuros.

## Propósito y alcance

Registrar condiciones directamente observables del drenaje del frente vial definido por el avance, páginas 5-9 y 12-13. Conservar las dimensiones captación/conducción y operatividad/mantenimiento. Su uso definitivo depende de inventario, fuentes pertinentes, revisión metodológica, criterio del asesor y validación documentada. La asignación propuesta no modifica la matriz canónica.

La capacidad de captación o transporte no se califica a partir de esta ficha. No se deduce saturación interna ni causa de daños. No se emplean baches, grietas, severidades del pavimento ni PCI para construir el futuro puntaje de drenaje.

## Identificación y condiciones de visita

Registrar ID de visita, fecha y hora, observador, versión, subtramo, lado, progresivas/coordenadas de inicio-fin, componente y fotografías. Conservar croquis de continuidad y relación componente-subtramo. Un componente que sirve a varios subtramos mantiene el mismo ID; su repetición no crea nuevas unidades independientes.

Describir condición meteorológica y del suelo/superficie al momento de inspección; lluvia antecedente con hora y fuente, o desconocida; indicios de lavado/fuga u otros aportes; limpieza reciente respaldada por observación/documento, o desconocida. No completar historial meteorológico ni de mantenimiento por suposición. Guardar el documento/fotografía que respalda cada dato de contexto.

## Registro bruto por componente

| ID provisional | Dimensión propuesta | Qué registrar y método | Unidad/evidencia | Límite de interpretación |
|---|---|---|---|---|
| INV-01 | Contexto, sin puntuar | Inventario de componentes presentes y alternativa visible; recorrido completo y croquis | Tipo, ID, ubicación, cantidad inventariada, foto | Existencia no equivale a adecuación. Ausencia no equivale automáticamente a deficiencia. |
| CC-01 | Captación/conducción | Continuidad visible del recorrido superficial hacia entradas o salida; identificar inicio, fin e interrupciones | Descripción, longitud accesible en m, croquis y foto | Flujo potencial o aparente no acredita dirección por cotas ni capacidad. |
| CC-02 | Captación/conducción | Geometría accesible de entrada y sección; medir largo/ancho y profundidad solo donde sea seguro | m o cm declarados, puntos y equipo, foto con referencia | No inferir caudal de diseño ni eficiencia de captación. |
| CC-03 | Captación/conducción; evacuación integrada de forma provisional | Punto de conexión o descarga visible y continuidad conocida/desconocida | Ubicación, ID de conexión, texto y foto | No asumir destino final o continuidad subterránea. Sin acceso se registra desconocida. |
| CC-04 | Captación/conducción; opcional, pendiente de viabilidad | Diferencia de cota y longitud entre puntos identificados, si hay equipo y método definidos | Cotas y distancia en m; pendiente derivada en %, con precisión | Con móvil/cámara y apariencia solamente no se registra porcentaje de pendiente. No es diseño hidráulico. |
| OM-01 | Operatividad/mantenimiento | Material que obstruye una abertura accesible; contorno libre/ocupado visible, con foto perpendicular y referencia cuando sea posible | Material, área visible y área ocupada en unidad coherente, o descripción si no es medible | No extrapolar a obstrucción interna. La proporción de área solo se calcula con bases comparables; no se transforma aún en puntuación. |
| OM-02 | Operatividad/mantenimiento | Acumulación de material en conducción abierta; localización, extensión longitudinal y sección visible | Material, longitud en m y dimensiones accesibles, fotos | No deducir pérdida de capacidad ni frecuencia de limpieza. |
| OM-03 | Operatividad/mantenimiento | Condición física del propio componente que impida acceso o continuidad visibles, sin usar daño de pavimento | Tipo, localización, descripción y foto | Un mismo hecho no recibe dos penalizaciones automáticas por función y mantenimiento. |
| CT-01 | Contexto funcional; incorporación a escala por decidir | Agua observada: extensión delimitada, ubicación y profundidad accesible sin entrar en la calzada | Largo/ancho en m, profundidad en cm, hora y foto | Sin agua observada no significa funcionamiento en lluvia comprobado. No atribuir mecanismo causal. |
| CT-02 | Contexto temporal; sin puntuar | Si existe seguimiento previsto, vincular observaciones del agua en momentos identificados | Horas reales, intervalo y fotos repetibles | Una fotografía no permite estimar duración ni tiempo de evacuación. |
| DOC-01 | Contexto documental; relación con segunda dimensión por decidir | Documento de intervención o mantenimiento, componente, fecha, alcance y procedencia | Identificador documental y localización de evidencia | Distinguir fecha documentada de recuerdo o apariencia. Documento ausente no prueba que no hubo mantenimiento. |

Los IDs INV/CT/DOC son auxiliares de esta propuesta; no deben registrarse como indicadores aprobados. El fundamento específico de cada indicador y su aceptación deberán incorporarse en la operacionalización definitiva. La fuente F009, reglamento 3.9-3.10 y 3.15-3.17, sirve para distinguir funciones y acciones; no prescribe esta ficha ni sus mediciones.

## Reglas preliminares de registro

1. **Observado:** describir o medir el atributo y enlazar evidencia. Un cero solo significa medición válida de cero con método y aplicabilidad conocidos.
2. **Ausencia observada:** el componente no se identificó dentro del ámbito accesible, con recorrido registrado. No convertirla en penalización hasta determinar su aplicabilidad y solución alternativa.
3. **No aplicable:** reservar para una decisión respaldada por la configuración del sistema y la regla del instrumento. Un observador no debe inventar esa regla durante el recorrido.
4. **Desconocido/no observado:** falta de acceso, falta de documento, visibilidad insuficiente, evento no ocurrido o método no disponible. Conservar motivo; no rellenar con cero ni deducir condición favorable.
5. **Dato discrepante:** guardar observaciones originales y conciliación; no sustituirlas por consenso sin trazabilidad.

La implementación necesita campos para estado de observación, motivo de faltante, componente, visita y evidencia. El CSV actual no tiene todos estos campos explícitos. Esta propuesta **no altera su esquema**: el coordinador deberá revisar con metodología/estadística si se amplía el CSV y su diccionario o se crean tablas relacionadas antes de recolectar.

## Secuencia de piloto y aceptación

Reconocer todo el frente y su configuración; elaborar croquis y asignar IDs; fijar unidades y rutas de aplicabilidad; aplicar una visita piloto conforme al protocolo temporal; revisar discrepancias de observadores y medidas; documentar cambios. La muestra del piloto, el número de observadores y la evaluación de repetibilidad se justifican según la viabilidad real; no se fijan aquí tamaños ni umbrales arbitrarios.

Solo después se decidirá el subconjunto de indicadores puntuables, sentido, pesos, agregación y regla de faltantes con respaldo explícito. Hasta entonces, la ficha permite preparar un levantamiento y revisar contenido; no producir un índice de deficiencia ni resultados estadísticos definitivos.
