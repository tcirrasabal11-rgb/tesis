# Verificación de esta versión del proyecto

Fecha: 2026-10-13. Versión: 1.0.0. Se verificó la plantilla y sus herramientas; esto no es una validación académica de la tesis.

## Comprobaciones realizadas

| Elemento | Prueba | Resultado |
|---|---|---|
| Configuración y perfiles | Parseo TOML, campos obligatorios y catálogo de seis agentes. | Sin errores estructurales. |
| Nueve skills | Encabezados YAML, nombres, metadatos de interfaz, referencias y validador de skills. | Las nueve pasan. |
| Herramientas Python | Cuarenta pruebas de datos, procedencia, rangos, integridad, rutas, planes, correlaciones conocidas y CLI. | Cuarenta pruebas pasan. |
| Avance original | SHA-256 contrastado con el adjunto y extracción por página. | Original conservado; quince páginas extraídas. |
| Word | Exportación real con Pandoc y estilo base, con texto de los capítulos de plantilla. | DOCX generado; no contiene resultados de campo. |
| PDF y render | Conversión real con motor Office disponible y pdftoppm, con comprobación PNG. | PDF y tres páginas de prueba generados. |
| Presentación | Estilo base renderizado y revisado, y las tres páginas del borrador de prueba inspeccionadas. | Sin recortes ni solapamientos en esta prueba; índice dinámico requiere actualización en el motor de entrega. |
| Instalación Bash | Análisis de sintaxis con `bash -n`. | Sin errores de sintaxis. |

Durante una salida de prueba se detectó un PNG truncado. Se reforzó el renderizador para comprobar firma, estructura, CRC e IEND antes de declarar la generación de páginas. La repetición produjo imágenes completas; la revisión visual sigue siendo necesaria.

## Pruebas de uso de las skills

Tres agentes independientes recibieron encargos concretos sin las conclusiones esperadas del autor de la plantilla:

- Bibliografía: aplicó la skill a una referencia heredada, accedió al documento primario, localizó evidencia y registró discrepancias editoriales sin actualizar registros compartidos automáticamente.
- Metodología: reconstruyó correspondencias y decisiones pendientes a partir del avance, preservó el diseño y mantuvo F2 provisional. Detectó y documentó un cambio concurrente de configuración hecho por el coordinador durante la prueba.
- Estadística: rechazó seis pares sintéticos sin respaldo y un plan pendiente como base para resultados de tesis; los controles detectaron también el archivo vacío de campo.

Estas pruebas evalúan los procedimientos. Sus salidas no se incorporan como datos de campo ni como una aprobación del asesor. Las doce referencias del registro inicial siguen pendientes de la auditoría canónica del proyecto.

## Alcance y comprobaciones pendientes en la computadora del usuario

- No hay ejecutable local `codex` en el entorno donde se generó el kit. Por ello, se comprobó el formato y la aplicación de instrucciones, pero no el descubrimiento automático de estos perfiles dentro de una instalación CLI/IDE. El primer prompt y CONFIGURACION_CODEX.md incluyen esa comprobación real.
- No se ejecutó PowerShell en Windows ni se instalaron dependencias dentro de la computadora del usuario. Se incluyen scripts y comandos manuales con rutas relativas para esa plataforma.
- La disponibilidad del modelo, sus niveles de esfuerzo y los permisos efectivos dependen de la cuenta y del cliente. No se fijan IDs de modelo ni credenciales.
- La guía universitaria, la norma PCI completa, la validez de instrumentos, la suficiencia del diseño, los datos de campo y las aprobaciones reales siguen siendo entradas de la investigación.
- Los detectores de citas e integridad no prueban veracidad de mediciones ni apoyo semántico de fuentes. Las revisiones especializadas y del asesor están previstas para esos puntos.

## Reproducción

Ejecutar desde la raíz `python tools/tesis.py verify`, `python -m unittest discover -s tests -v` y el primer prompt. Las imágenes y documentos temporales de pruebas no se distribuyen como resultados de tesis. El estilo base de Word sí forma parte del proyecto, como referencia provisional de exportación.
