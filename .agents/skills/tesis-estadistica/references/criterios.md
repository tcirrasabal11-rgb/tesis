# Criterios del procedimiento

## Decisión del análisis
Pearson resume asociación lineal y requiere examinar condiciones pertinentes para su inferencia. Spearman resume asociación por rangos y tampoco elimina dependencia ni problemas de diseño. Justificar elección con escala, forma, n y condiciones, no con una única prueba automática. La plantilla ofrece ambas como implementaciones disponibles, no como decisión ya tomada.
## Alcance del motor
Produce descripciones, contraste bilateral y ajuste Holm o none según plan. No calcula IC automáticamente ni implementa modelos espaciales o regresión. Desarrollar y validar un script adicional si esas condiciones son necesarias; no sustituirlo por n artificial o bootstrap iid inapropiado. Tres pares es solo un límite de cómputo.
## Reproducibilidad
Guardar input_sha256, plan_sha256, script_sha256, versiones de Python/SciPy, IDs por comparación, valores usados, exclusiones y comandos. Evitar redondear antes de calcular. Reportar precisión al presentar resultados, conservando datos numéricos completos. Casos sintéticos deben permanecer en tests y ser rechazados en modo real.
