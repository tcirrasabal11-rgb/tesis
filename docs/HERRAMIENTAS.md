# Herramientas ejecutables

Ejecuta todos los comandos desde la raíz. `python` significa el intérprete con las dependencias del proyecto. Las herramientas nunca deben sobrescribir insumos; las salidas usan rutas diferentes y control de sobrescritura explícito.

| Comando | Función |
|---|---|
| `python tools/tesis.py doctor` | Identifica Python, dependencias, Codex, Git, Pandoc y motores de render. |
| `python tools/tesis.py verify` | Comprueba TOML/YAML, perfiles, skills, estructura y hash del PDF original. |
| `python tools/tesis.py snapshot-originals` | Registra SHA-256 de los originales de campo sin modificar sus bytes. |
| `python tools/tesis.py extract-pdf --input requisitos/avance_original.pdf --output fuentes/fichas/avance_extraido.md` | Extrae texto por página y registra el hash. Señala páginas que requieren OCR. |
| `python tools/tesis.py validate-data --input datos/campo/pares_analisis.csv` | Revisa IDs, fechas, valores finitos, PCI, procedencia y rutas de evidencia. |
| `python tools/tesis.py describe --input datos/campo/pares_analisis.csv --output analisis/resultados/descriptivos.json` | Describe pares disponibles sin inferencia. |
| `python tools/tesis.py analyze --input datos/campo/pares_analisis.csv --plan config/plan_analisis.yaml --output analisis/resultados/campana_2026` | Correlaciones y ajuste de multiplicidad según un plan aprobado. |
| `python tools/tesis.py audit-citations` | Detecta IDs desconocidos, referencias pendientes y marcadores de contenido incompleto. |
| `python tools/tesis.py export --mode draft --output entregables/borrador.docx` | Genera Word con Pandoc. |
| `python tools/tesis.py render --input entregables/borrador.docx --output entregables/qa/borrador` | Convierte a PDF/PNG si existen los motores. |
| `python -m unittest discover -s tests -v` | Ejecuta pruebas de integridad, procedencia e inferencia. |

Los CSV de la plantilla están vacíos salvo registros iniciales de gestión y bibliografía heredada. Un archivo vacío no permite analizar. El directorio `tests/fixtures` contiene exclusivamente casos sintéticos identificados, que el comando de análisis real debe rechazar.
El código no descarga automáticamente artículos ni convierte enlaces en evidencia verificada. Esa tarea corresponde a lectura y verificación bibliográfica. Tampoco calcula PCI desde curvas inexistentes en el paquete. Esto debe resolverse mediante la documentación del método y cálculos reales, conservando su respaldo.
