# Diccionario de datos

Todos los IDs son texto estable y único en su tabla. Fechas ISO `AAAA-MM-DD`. Valores numéricos finitos con punto decimal; vacíos son faltantes, nunca cero. Las rutas son relativas a la raíz. Preservar medidas originales y evidencia; no completar observaciones que no ocurrieron.

| Tabla | Granularidad | Restricción principal |
|---|---|---|
| subtramos.csv | Un subtramo delimitado | ID único; geometría medida; tipo de pavimento real. |
| drenaje.csv | Indicador observado por subtramo/visita | Versión de instrumento, medida, unidad y evidencia. |
| fallas.csv | Falla cuantificada por unidad PCI/visita | Código/severidad/unidad según norma disponible. |
| pci.csv | Cálculo de una unidad PCI | PCI entre 0 y 100; respaldo del cálculo. |
| contexto.csv | Contexto por subtramo/visita | Fuentes reales de clima, tráfico y mantenimiento. |
| evidencias.csv | Archivo de evidencia | Ruta existente, hash y relación con unidad. |
| faltantes.csv | Dato ausente o no aplicable | Motivo y decisión explícitos. |
| pares_analisis.csv | Un subtramo de la campaña transversal | ID único, PCI y puntuaciones emparejadas sin pseudorreplicación. |

## Pares de análisis
`pci`: condición de 0 a 100, mayor es mejor. `deficiencia_drenaje`: puntuación global según instrumento aprobado, mayor debe significar más deficiencia. Las dos puntuaciones dimensionales mantienen ese mismo sentido. No hay un rango numérico universal de drenaje fijado en el kit; se documenta en la escala validada.
`origen_pci` y `origen_drenaje`: archivo de cálculo/evaluación que permite auditar el valor, no una URL o frase genérica. `procedencia`: campo_real o sintetico_prueba; el último solo se usa en fixtures de pruebas.

## Excel y CSV
Si se carga desde Excel, guardar como CSV UTF-8 y comprobar separador y decimales antes del análisis. La plantilla no mezcla CSV separados por punto y coma con los separados por coma. Hacer transformaciones explícitas sobre copias, con script y registro; no editar originales para adaptar su apariencia.
