# Diseño y datos de la investigación

## Información inicial
El objetivo inicial es establecer una asociación entre deficiencias de drenaje y condición superficial, con dos preguntas específicas. La investigación debe conservar una medición de exposición independiente de la medición de daños. El PCI se registra con su sentido de mejor condición cuando aumenta; cualquier transformación a deterioro debe justificarse y nombrarse claramente.

## Unidades y alcance
Define inicio, fin, coordenadas, progresivas, longitudes, anchos, material y variación de condiciones. Distingue segmento de gestión, subtramo correlacional, unidad de inspección PCI y elemento de drenaje. Un sumidero compartido o escorrentía que pasa por varios subtramos puede inducir dependencia. Dividir físicamente una vía no crea observaciones estadísticamente independientes. Presenta opciones de diseño al asesor si el frente vial no aporta información suficiente; no amplíes el ámbito silenciosamente.

## Instrumento de drenaje
Registra observaciones directas antes de puntuar. Distingue obstrucción, ausencia de componente, deterioro, continuidad, condición de descarga y evidencia de empozamiento. Una ausencia puede responder al diseño y debe interpretarse con contexto. Las pendientes aparentes son indicios; si se emplean como medición deben tener método y precisión. Identifica exposición a lluvia reciente y diferencias de visita. Justifica la escala, unidades, reglas, pesos y no aplicables con fuentes y expertos; guarda versiones del instrumento y del piloto.

## Procedimiento PCI
Comprueba tipo de pavimento y edición del procedimiento disponible. Usa códigos, severidades, densidades, curvas y valores de descuento de la norma consultada. No se incorpora un motor PCI de memoria. Guarda el cálculo verificable en `datos/originales/` y registra `origen_pci` en el archivo de pares. Decide con fundamento cómo emparejar una o varias unidades PCI con cada subtramo; no uses una media arbitraria o de unidades incompatibles.

## Archivo de pares de análisis
`datos/campo/pares_analisis.csv` tiene una fila por subtramo en la campaña transversal elegida. Columnas obligatorias: `subtramo_id`, `fecha`, `pci`, `deficiencia_drenaje`, `origen_pci`, `origen_drenaje`, `procedencia`. Las dos columnas de dimensiones están previstas para objetivos específicos. No dupliques el mismo subtramo por visitas o unidades PCI como si fueran nuevos sujetos.
`procedencia` debe ser `campo_real` en análisis real. Las rutas de origen son relativas a la raíz y apuntan a evidencia local existente. CSV usa UTF-8, coma como separador y punto decimal. No escribas textos como "no aplica" en columnas numéricas; usa vacío y documenta su motivo en el registro de faltantes.

## Recolección
Conserva archivos originales y sus hashes. Anota quién, cuándo y cómo midió, clima, lluvia reciente, seguridad y evidencias georreferenciadas cuando procedan. Gestiona permisos reales requeridos para inspección e información no pública, y evita captar datos personales innecesarios frente al hospital. No se fabrican fotografías ni validaciones.
Después de incorporar los originales ejecuta `python tools/tesis.py snapshot-originals`. Conserva cada manifest y registra nuevas versiones si se añaden originales; no actualices un hash para ocultar cambios de un archivo existente. `verify` contrasta el manifest canónico `datos/manifest_originales.json`. La campaña de pares debe corresponder al periodo declarado en el proyecto.

## Análisis
El script calcula descripciones antes de inferencia. La inferencia requiere un plan aprobado con evidencia local, justificación de independencia, instrumento validado y método elegido. Las propuestas alfa y Holm del YAML son modificables antes de su aprobación; no son mandatos de la universidad. El motor ofrece Pearson o Spearman con contraste bilateral y ajuste Holm o sin ajuste, según plan. No implementa modelos espaciales, regresión, cálculo de potencia o intervalos especiales; el estadístico debe desarrollar y validar un script adicional si el diseño los exige. Esta delimitación evita presentar una correlación estándar como suficiente para cualquier muestra.
El umbral de tres pares del script es solo computacional, nunca una justificación de tamaño de muestra. No clasifica automáticamente una asociación como débil o fuerte. Registra faltantes por comparación y multiplicidad; examina tamaños de efecto, incertidumbre y limitaciones. Una p pequeña no establece causalidad; una p grande no prueba ausencia de relación.
