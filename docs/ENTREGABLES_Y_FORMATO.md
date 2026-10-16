# Entregables y formato académico

Los archivos Markdown son el texto canónico editable. La estructura inicial contiene preliminares, introducción, problema, marco, metodología, resultados, discusión, conclusiones y anexos; ajústala a la guía institucional cuando se incorpore. No declares que esa estructura ya es la exigida por la universidad.

## Citas y referencias
Usa `[@F001]` para una fuente o `[@F001; @F002]` para varias. En referencias.json usa formato CSL JSON con la misma clave. Completa los metadatos según el original y selecciona el CSL institucional. La plantilla no presupone APA 7 como requisito. Verifica páginas, nombres, títulos, DOI y fecha de documentos normativos. Guarda las citas textuales cortas y su página; no conviertas una paráfrasis en una cita literal.

## Exportación
Ejecuta `python tools/tesis.py export --mode draft --output entregables/borrador.docx`. Requiere Pandoc instalado. Puede aplicar `plantilla_word` y `archivo_csl` de proyecto.yaml si apuntan a archivos proporcionados. La bibliografía debe tener CSL JSON utilizable cuando existan citas. El borrador muestra sus pendientes y no se etiqueta como tesis terminada.
Si no hay plantilla institucional configurada, utiliza `plantillas/referencia_base.docx`, un estilo provisional carta con texto y títulos negros. Se puede regenerar con `python tools/crear_referencia_word.py --output plantillas/referencia_base_v2.docx`. El estilo base no satisface automáticamente requisitos institucionales y no permite desbloquear una exportación final por sí solo.
`--mode final` exige formato_validado, requisitos aprobados, plantilla institucional, fuentes citadas verificadas, aprobación del análisis, expediente de datos y registro de cierre de revisión académica. Esos registros deben proceder de validaciones reales; el programa solo comprueba su presencia y campos. No certifique calidad académica mediante un indicador booleano.

## Word y PDF
El exportador genera DOCX con Pandoc. Para PDF y páginas PNG ejecuta `python tools/tesis.py render --input entregables/borrador.docx --output entregables/qa/borrador`. Requiere LibreOffice y pdftoppm accesibles. El renderizador crea una instancia de perfil temporal y no altera configuración de Office del usuario. Si estos motores faltan, el doctor lo indica; usa Word para actualizar campos, exportar PDF y revisar las páginas, documentando el procedimiento.
Revisa todas las páginas: cortes, tablas, fuentes, ecuaciones, numeración, índice, encabezados, pies y legibilidad. Actualiza índices y referencias cruzadas en Word/LibreOffice y confirma el PDF definitivo. Las ecuaciones deben permanecer como ecuaciones editables cuando se requiera; Pandoc interpreta matemáticas Markdown según el formato de salida.

## Expediente final
Incluye documento, anexos pertinentes, datos depurados con diccionario, scripts, resultados, trazabilidad de fuentes y evidencia de revisión. Conserva originales para auditoría sin incorporarlos indiscriminadamente a una entrega pública. Registra la versión de documento y de datos que sustentan cada resultado. El auditor académico y el asesor validan lo que los controles estructurales no pueden determinar.
