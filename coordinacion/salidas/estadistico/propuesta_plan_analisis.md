# Propuesta de plan analítico — R001

**Estado:** propuesta sin aprobar, 2026-10-14. Complementa la auditoría; no reemplaza `config/plan_analisis.yaml`, no autoriza inferencia y no contiene resultados. Autora, asesor y coordinador conservarán las decisiones y su evidencia antes de cambiar archivos canónicos.

## Pregunta, alcance y población

Mantener provisionalmente la asociación entre deficiencias observables del drenaje y condición superficial mediante PCI, en el frente de Pakamuros ante el Hospital General de Jaén durante 2026. Es un estudio transversal, no experimental y correlacional. No estima efecto causal del drenaje ni explica por sí solo humedad interna, soporte o daño estructural.

Antes de aprobar: identificar límites, geometría, tipo de pavimento, administración de la vía y campaña. Precisar si se describe el censo del frente delimitado o si se pretende inferir a una población más amplia; esta última requiere justificación. Medir todas las subdivisiones contiguas no genera por sí solo una muestra representativa de Jaén.

## Unidad, emparejamiento y dependencia

| Decisión pendiente | Evidencia que debe recibirse | Criterio de revisión |
|---|---|---|
| Delimitación de subtramos equivalentes | Reconocimiento, longitud y ancho medidos, coordenadas, material y croquis | Compatibilidad con alcance original, variación real y unidades PCI; selección independiente del daño. |
| Correspondencia drenaje–PCI | Tabla con subtramo, unidades PCI, cobertura, calzada/lado, componentes, conexiones y visita/campaña | Cada par mide el mismo espacio y periodo con origen reconstruible. |
| Exposición compartida | IDs de elementos y posibles grupos; conexiones observadas y desconocidas | Separar número de filas de información independiente; no estimar n efectivo sin estructura real. |
| Varias unidades PCI por subtramo | Procedimiento íntegro elegido, material, áreas/denominadores y cobertura | Integración técnicamente compatible; justificar ponderación o alternativa. No usar media universal. |
| Visitas complementarias | Propósito, ventana temporal, lluvia antecedente y cambios de condición | Definir medición transversal antes de resultados; conservar repetición sin contarla como nuevo subtramo. |

El archivo actual admite una fila por `subtramo_id` en la campaña. Si la unidad defendible o el diseño requieren otra granularidad, el coordinador deberá proponer cambio explícito de tabla, diccionario, plan y validadores. Renombrar IDs no elimina dependencia. Un modelo espacial o agrupado requiere estructura e información suficientes; no es una solución automática para pocos grupos.

## Escala e instrumentos

Conservar las dimensiones captación/conducción y operatividad/mantenimiento. Como propuesta pendiente, situar continuidad y conexión visible hacia evacuación en la primera; condición observable de obstrucción y operatividad en la segunda. Gestionar historial documental de mantenimiento como contexto hasta demostrar que existe medición adecuada. Mantener empozamiento inicialmente como contexto, separado del daño superficial, para revisar mecanismos y circularidad.

Para cada indicador se requiere definición, unidad bruta, ubicación, opciones, aplicabilidad, orientación, transformación a puntuación y respaldo. Decidir pesos, reglas de agregación dimensional/general y cobertura mínima justificadas por contenido; no presumir escala 0–3, pesos iguales o umbrales heredados. Si distintos subtramos tienen rutas de aplicabilidad distintas, revisar comparabilidad de sus puntuaciones. El desconocimiento no se convierte en cero. No usar fallas, PCI o depresiones puntuadas por el PCI dentro de la exposición.

La validez de contenido, repetibilidad de observación y utilidad de cada dimensión necesitan evidencia real. No imponer un coeficiente de consistencia interna a un inventario de componentes heterogéneos sin justificar qué modelo de medición representa. El criterio de acuerdo entre observadores dependerá del tipo de dato, la viabilidad y el protocolo; no se inventan número de expertos ni umbrales.

Mantener PCI en 0–100, mayor es mejor condición. Su respaldo exige norma/edición accesible, registro de fallas, mediciones, denominadores y cálculo reproducible. No transformar a deterioro creciente salvo decisión previa y variable claramente nombrada.

## Descripción y revisión antes de inferencia

Con datos reales: verificar integridad de originales, IDs y enlaces, campaña, unidades, duplicados, versiones, rangos y origen de puntuaciones. Preparar tabla de cobertura, faltantes y motivos por variable/subtramo. Describir distribución, dispersión, empates, constantes y casos extremos; conservar todos los originales y documentar cualquier corrección.

Dibujar PCI frente a cada puntuación y mostrar ubicación de las unidades en el croquis para examinar forma y agrupación espacial. No tratar una prueba automática de normalidad como selector del método. Si no existe variación de una variable, la correlación está indefinida; describir esa limitación. Si las unidades no son comparables, resolver medición antes de calcular.

La herramienta `describe` solo entrega n, faltantes, mínimo, máximo, media y mediana. No sustituye estas revisiones, gráficos ni análisis de dispersión. El coordinador deberá incorporar el código adicional pertinente una vez conocido el instrumento.

## Estimando, hipótesis y método por decidir

Propuesta: asociación general y dos asociaciones dimensionales con PCI, con hipótesis bilaterales no direccionales. Tras elegir coeficiente y población, formular para cada comparación H0: coeficiente poblacional=0 y H1: distinto de cero, si la inferencia resulta defendible. No anticipar signo, fuerza ni significación. Ninguna hipótesis de medias sustituye este objetivo.

| Ruta posible | Cuándo considerarla | Qué falta antes de ejecutarla |
|---|---|---|
| Pearson | Puntuaciones con interpretación cuantitativa defendible y asociación lineal de interés | Escala, forma, influencia y condiciones del contraste/intervalo; independencia o tratamiento apropiado de dependencia. |
| Spearman | Rangos ordenables y asociación monótona de interés | Orden válido, empates, variación y método de p adecuado; no depender sin evaluación de aproximación asintótica. |
| Método adicional | Dependencia, ajuste contextual o incertidumbre requieren otra estructura | Especificación previa, datos/grupos suficientes y script con pruebas verificadas. Permutación exige intercambiabilidad; remuestreo iid no corrige espacialidad. |
| Descripción limitada o revisión del diseño | Ámbito sin variación, comparabilidad o información suficiente | Explicar límite y consultar ampliación/reformulación explícita al asesor. No forzar inferencia ni cambiar ámbito silenciosamente. |

No ejecutar ambas correlaciones para seleccionar la p más pequeña. Una sensibilidad justificada se especificará antes, con interpretación separada. El valor de tres pares es un límite computacional del motor, no suficiencia estadística. No existe todavía n, efecto relevante, precisión objetivo o estructura de dependencia para calcular potencia o tamaño de muestra; definirlos sin fabricar estimaciones y revisar viabilidad con reconocimiento/piloto.

## Comparaciones, faltantes e incertidumbre

El YAML propone tres comparaciones. Acordar si forman una familia confirmatoria y si la general es primaria. Alfa 0.05 y Holm son propuestas revisables, no requisitos institucionales confirmados. Registrar todas las comparaciones previstas y resultados, sin ocultar una por p desfavorable. Holm no exige que las tres pruebas sean independientes, pero necesita p válidas para su finalidad; no corrige sesgo de medición o dependencia de observaciones.

La exclusión por par con registro es lo que implementa el motor, no una decisión científica ya validada. Evaluar magnitud y mecanismos de faltantes y sus consecuencias; informar n e IDs por comparación. Si esta regla no es defendible, diseñar otra y verificar su implementación. No imputar cero, media u otros valores por conveniencia, ni eliminar atípicos para mejorar una correlación.

Definir intervalo de confianza y método defendible según estimando y dependencia; el motor actual no produce intervalos. Si no puede justificarse uno con la información disponible, explicitar la limitación. No clasificar fuerza con baremos universales. P grande no demuestra ausencia; p pequeña no establece causalidad ni relevancia práctica.

## Reproducibilidad y aprobación

Congelar pares, originales, instrumento y plan. Conservar hashes, versiones, comandos, valores completos, casos excluidos y justificaciones. La salida debe mostrar coeficiente, n usado, p cruda/ajustada cuando proceda e incertidumbre disponible, con nombres y sentido consistentes. Pasar interpretación a drenaje/pavimentos y límites al metodólogo mediante el coordinador.

Para aprobar faltan: mapa y población; unidades y n viable; norma PCI y cálculo piloto; escala y reglas; campaña; tratamiento de dependencia/faltantes; método de contraste e incertidumbre; familia/alfa; criterio documentado de aprobación. Un archivo existente o un `true` en YAML no prueba validez. Si se requiere un motor adicional, probarlo y documentarlo antes de analizar los originales reales. No se modifica el estado pendiente del plan con este informe.
