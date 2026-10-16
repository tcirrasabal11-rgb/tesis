# Incorporar documentos a la tesis

## Lo que haces tú

1. Copia el archivo en la carpeta correspondiente de esta tabla.
2. Indica a Codex: **Incorpora los documentos nuevos siguiendo `prompts/08_INCORPORAR_DOCUMENTOS.md`.**

| Documento | Carpeta | Uso |
|---|---|---|
| Artículo, tesis ajena, libro, manual, norma o informe publicado | `fuentes/documentos/` | Evidencia y antecedentes; requiere lectura y verificación. |
| Guía, rúbrica, plantilla oficial y observaciones del asesor | `requisitos/` | Requisitos de formato y decisiones académicas. |
| Nueva versión de tu avance | `requisitos/` | Comparación con la base; se conserva el original y se documenta cuál versión rige. |
| Ficha de campo, fotografía, cálculo o archivo de medición original | `datos/originales/` | Evidencia propia, con fecha, responsable y procedencia. |

Conserva nombres descriptivos, por ejemplo `guia_tesis_2026.pdf`, `observaciones_asesor_2026-10-14.docx` o `autor_titulo_2024.pdf`. Si cambia un documento, conserva ambas versiones y explica qué versión sustituye a cuál. No sobrescribas `avance_original.pdf`.

## Lo que realiza Codex

El coordinador aplica `$tesis-orquestar` y `$tesis-fuentes`; lee el estado y los registros antes de buscar o extraer de nuevo.

1. **Inventario.** Detecta archivos nuevos, registra nombre, ruta, fecha de recepción, tipo, SHA-256, función y versión. Compara hashes y metadatos para reconocer duplicados. Un archivo diferente con título parecido puede ser otra edición.
2. **Lectura.** Extrae texto y conserva correspondencia con páginas o secciones. Revisa visualmente tablas, fórmulas e imágenes que afecten una afirmación. Los documentos escaneados necesitan OCR verificable.
3. **Clasificación.** La guía institucional gobierna el formato, las observaciones del asesor proponen decisiones y las publicaciones aportan evidencia. Una tesis ajena no redefine por sí sola el ámbito ni la metodología de este proyecto.
4. **Registro.** Las fuentes externas reciben un ID Fxxx único en `fuentes/registro.csv`, una ficha en `fuentes/fichas/` y, cuando corresponda, afirmaciones con localización en `fuentes/afirmaciones.csv`. Los requisitos y versiones propias se registran en `requisitos/registro_documentos.csv`; los cambios de autoridad o alcance se documentan en `DECISIONES.md`.
5. **Verificación.** Contrasta autor, título, año, edición, DOI o URL con el emisor. Distingue metadatos confirmados, documento disponible y afirmaciones efectivamente revisadas. Una descarga o el resultado de un buscador no basta para marcar una fuente como verificada.
6. **Integración.** Explica qué aporta al problema, antecedentes, marco, metodología o discusión; registra contradicciones y límites. Propone cambios concretos y los integra solo con el respaldo y la revisión que correspondan. Completa CSL JSON únicamente desde metadatos comprobados.
7. **Cierre.** Ejecuta los controles pertinentes y actualiza estado, tareas y decisiones. Entrega una lista de incorporados, duplicados, pendientes de OCR/acceso y capítulos afectados.

## Extracción PDF disponible

Desde la raíz del proyecto, con el Python del entorno:

```bash
python tools/tesis.py extract-pdf --input fuentes/documentos/autor_titulo_2024.pdf --output fuentes/fichas/F013_texto_extraido.md
```

`F013` es solo un ejemplo: el coordinador debe comprobar el próximo ID libre antes de usarlo. Este comando conserva el PDF, registra su hash y separa el texto por página. Señala páginas con poco texto, pero **no ejecuta OCR ni verifica la bibliografía automáticamente**. Para otros formatos se usa un lector disponible y se documenta la herramienta; no hay un importador universal silencioso.

Copiar un archivo no ejecuta trabajo en segundo plano. La incorporación se realiza cuando se da el encargo en Codex. No es necesario crear otro agente por cada documento.

## Cuando haya un conflicto

Conserva las dos evidencias y localiza la contradicción. Explica si afecta un dato, una definición, una edición normativa, el formato o una decisión de diseño. Si el documento nuevo es una corrección autorizada del asesor, registra esa autoridad y su efecto. Si es una publicación que discrepa, intégrala en la discusión y revisa la comparabilidad; no borres evidencia adversa.

No cierres instrumentos, tamaño de muestra, resultados o decisiones del asesor rellenando valores ausentes. Continúa en las tareas documentales que sí cuentan con entradas suficientes.
