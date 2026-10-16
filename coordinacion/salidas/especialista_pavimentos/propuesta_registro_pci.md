# Propuesta provisional de registro y trazabilidad PCI

R001, 2026-10-14. Documento de diseño para discusión; no instrumento validado ni reproducción de formularios ASTM. No incluye curvas, tablas de descuento, tamaños normativos o resultados inventados. Su integración corresponde al coordinador tras revisión técnica y metodológica.

## Reconocimiento y unidades

Antes de inspeccionar, registrar fecha, responsable, geometría medida, material observado y cambios de superficie. Elaborar croquis de calzadas, carriles o lados cuando corresponda, accesos, límites y elementos de drenaje. El tipo de pavimento sigue pendiente de confirmar; no llenar catálogos por analogía con otra investigación.

Se propone un inventario de unidades de inspección enlazado al inventario de subtramos existente. Campos por decidir:

| Grupo | Campos propuestos | Criterio de revisión |
|---|---|---|
| Identificación | `unidad_pci_id`, sección, `subtramo_id`, versión del mapa | ID estable y ubicación inequívoca. |
| Geometría | Progresivas, croquis/polígono, lado o calzada, material, medidas | Conservar geometría original y fuente; no deducir área solo de la longitud. |
| Denominadores | Área medida y, si el método aplicable lo requiere, inventario o conteo de elementos | Campos finales dependen del material y de la edición consultada. |
| Selección | Regla, cobertura, unidades incluidas y motivo documentado | Separar selección para inspección de selección analítica; no elegir solo daños visibles. |
| Norma | ID, edición, apartados consultados, acceso al respaldo | Una ficha editorial no sustituye el procedimiento completo. |

No crear aún un CSV canónico alternativo: primero comprobar qué campos exige la edición elegida y cómo se vinculan a las tablas del proyecto.

## Registro de fallas

Mantener los campos de `datos/campo/fallas.csv`. Proponer adicionalmente localización dentro de la unidad, referencia al croquis y a las medidas originales, versión del instrumento y referencia al criterio de clasificación usado. Registrar cada severidad y cantidad sin sustituirlas por una opinión global. Toda foto debe tener identificación y relación con el registro; deben conservarse fecha, escala cuando corresponda y contexto suficiente para revisión.

Ausencia de evidencia no equivale a cantidad cero. Separar no observado, inaccesible, no medido y no aplicable con el motivo en el registro de faltantes.

## Respaldo de cálculo

El archivo señalado por `origen_calculo` deberá conservar:

1. Unidad, visita, operador y registros originales de fallas utilizados.
2. Medidas, denominadores y transformaciones efectuadas, con unidades.
3. Norma, edición y localización de cada criterio de cálculo consultado.
4. Hoja o software utilizado, versión y operaciones reproducibles; acceso al respaldo técnico permitido, sin distribuir indiscriminadamente material protegido.
5. Resultado PCI, revisión independiente del cálculo, fecha y discrepancias corregidas.

Comprobar rango e IDs es necesario para control informático; no demuestra que las fallas o la severidad sean correctas. La revisión debe poder volver del PCI hasta las mediciones. El piloto aún debe producir datos reales para probar este circuito.

## Correspondencia con drenaje y análisis

Preparar una tabla de propuesta con unidad PCI, subtramo, campaña, lado/calzada, elementos de drenaje vinculados, cobertura, conexión compartida y regla de integración. No rellenar puntuaciones. Si una unidad cruza subtramos o varios subtramos comparten exposición, derivar a metodología y estadística antes de construir pares.

Cada fila analítica deberá señalar qué unidades y registros de drenaje la originaron. No asignar automáticamente a todas las unidades el PCI global del frente ni copiar un puntaje de drenaje para simular observaciones independientes. Si hay varias visitas, distinguir visita complementaria y nueva observación según el diseño, sin incrementar n por defecto.

## Piloto y criterio de aceptación

La preparación incluye entrenar al observador con el procedimiento accesible, probar fichas en campo, revisar clasificación y medición y documentar desacuerdos. El número de casos y el criterio de concordancia se justifican con metodología; no se propone aquí un umbral universal.

Aceptar la ficha cuando un revisor pueda ubicar la misma unidad, comprender las medidas, repetir el cálculo desde originales y reconstruir el par de drenaje. Registrar aprobación y versión reales. Mantener PCI como condición creciente y evitar inferencias de daño estructural, saturación o causa desde esta inspección superficial.
