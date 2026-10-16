# Auditoría inicial de estadística — R001

**Perfil:** estadistico. **Fecha:** 2026-10-14. **Fase:** F0/F2 provisional. **Entradas:** versión 1.0.0, manifiestos `R001_insumos.json` y `R001_ronda2_inicial.json`, informes técnicos y versión final de fuentes. Las propuestas siguientes requieren integración y validación; no son aprobación académica.

## Respuesta al encargo

El análisis correlacional es una intención coherente con el avance, pero su factibilidad todavía no está demostrada. No existen observaciones de campo en las tablas, ni geometría, escala de drenaje o regla de emparejamiento suficientes para construir pares válidos. No corresponde calcular coeficientes, potencia o un tamaño mínimo inventado. Sí queda preparado un plan de decisiones verificables, adjunto en `propuesta_plan_analisis.md`.

Esta revisión la ejecutó un **subagente de esta sesión**, leyendo el perfil y la skill. El coordinador recibió y transmitió las observaciones; no se presupone conversación autónoma entre especialistas. No se ejecutó Codex CLI del usuario ni se comprobó el descubrimiento local de perfiles y skills. `doctor` no encontró ese ejecutable.

## Evidencia y versiones

Se leyó la extracción completa del avance de 15 páginas y se contrastaron directamente las páginas PDF 3, 6, 8–9 y 12–13. Se revisaron matriz, operacionalización, configuración, plan, escala, diccionario, cabeceras de campo, código y pruebas pertinentes. También ambos informes técnicos y sus propuestas, y el informe final de fuentes junto con `propuesta_verificacion.json`.

El SHA-256 del informe de fuentes leído es `14e84e248d44b5db59c2ca5558a0ff68f54c545f1d57a88ac5f5d371f02aea66`. Se contrastaron directamente en F005 el método estadístico y las tablas 8–11 del PDF español conservado por bibliografía. `manifest_revision.json` identifica estos insumos, versiones y hashes; todas las entradas originales congeladas coincidieron.

## Hallazgos priorizados

| ID y severidad | Evidencia y efecto | Resolución y criterio de cierre |
|---|---|---|
| EST-01 — Bloqueante | Avance p. 8 y PAV-02/DRE-02: subtramos equivalentes sin límites ni mapa de exposición. No se conoce cuántas unidades aportan información distinguible ni cómo dependen. | Croquis, geometría, material y tabla unidad PCI–subtramo–componentes–conexiones; justificar unidad y población de referencia. Cerrar con expediente de viabilidad, sin dividir para obtener un n deseado. |
| EST-02 — Bloqueante | Escala pendiente, operacionalización vacía y DRE-01/03/06: no hay puntuación reproducible. Pesos, denominadores y ausencias pueden alterar artificialmente asociaciones. | Definir indicadores, sentido, aplicabilidad, agregación y faltantes antes del campo definitivo; revisión de contenido y piloto documentados. |
| EST-03 — Bloqueante | PAV-03/04/06: falta procedimiento operativo PCI y correspondencia espacial/temporal. Un valor entre 0 y 100 no demuestra cálculo válido. | Elegir edición accesible y material; reconstruir cálculo y correspondencia desde originales. Aprobar reglas para múltiples unidades y visitas. |
| EST-04 — Mayor | Plan pendiente y `correlations`: Pearson/Spearman bilaterales, sin modelos espaciales ni intervalos. Una aprobación declarada no demuestra supuestos. | Elegir estimando, método e inferencia según diseño y escala; extender y verificar el motor cuando sea necesario. No habilitarlo mediante casillas sin evidencia. |
| EST-05 — Mayor | `validate_pairs` valida pares, fechas, rangos y respaldo existente; no verifica íntegramente relaciones entre tablas, puntuación ni denominadores. | Revisar trazabilidad técnica, cobertura y consistencia con originales; añadir controles cuando el instrumento se cierre. Un `ok` informático no certifica medición. |
| EST-06 — Mayor | F005 §3.2 y tabla 10: compara medias de constructos y usa umbral 0.5; no es contraste de asociación. | Mantener el antecedente con lectura crítica; no importar ese contraste, categorías, cero por ausencia o muestra como reglas de Jaén. |

## Respuestas a los especialistas, una por una

**1. Pavimentos: ¿cuál es la observación cuando hay drenaje compartido?** El subtramo continúa como candidato analítico del avance, condicionado a una exposición definida y una medición PCI compatible. Compartir componentes puede inducir dependencia; no obliga automáticamente a fusionar toda conexión. Deben identificarse grupos y variación local. Copiar un puntaje global no crea nuevas exposiciones. Si la puntuación es constante en todo el frente, esa correlación no está definida, aunque existan numerosas fotos.

**2. Pavimentos: ¿cómo integrar varias unidades PCI y visitas?** Exigir mapa y cobertura; decidir integración conforme al procedimiento consultado, homogeneidad y objetivo. No promediar por comodidad ni duplicar una unidad que cruza límites. Una segunda visita, foto o falla no constituye otro sujeto independiente. En el diseño transversal se acordará campaña y ventana común; visitas complementarias respaldan la misma medición o exigen una regla temporal previa. Un diseño de medidas repetidas supondría una modificación explícita.

**3. Drenaje: ¿qué hacer con falta de variación y denominadores distintos?** Describir primero medidas brutas y aplicabilidad. Si las condiciones difieren, estudiar qué comparación tiene significado; no normalizar para fabricar variación. Porcentajes calculados con componentes o coberturas distintos pueden representar objetos distintos. No asignar cero a desconocidos ni excluirlos silenciosamente.

**4. Drenaje y fuentes: ¿ausencia, no aplicable y deficiencia?** Registrar por separado existencia, alternativa observada, inaccesibilidad y condición medida. Ausencia no equivale automáticamente a incumplimiento o máximo defecto. La regla depende de la solución y del sustento técnico. No aplicable exige ruta del instrumento; dato faltante exige motivo. La tabla 8 de F005 no valida una regla universal para Pakamuros.

**5. Metodología: ¿son suficientes las propuestas de dos dimensiones y empozamiento como contexto?** Son coherentes como punto de partida, no bastan para validar una escala. Conservar dos dimensiones respeta p. 6; ubicar continuidad y conexión de evacuación en captación/conducción evita crear una tercera sin justificación. Separar gestión documental y condición observable impide deducir historial desde limpieza. Empozamiento como contexto inicial reduce circularidad con deformaciones usadas en PCI; su incorporación posterior necesitará justificación, reglas y análisis de sensibilidad previo. Ninguna propuesta está aprobada.

**6. Metodología: ¿hipótesis bilaterales y n?** Una formulación de asociación distinta de cero, sin dirección anticipada, es compatible con las preguntas. Debe precisar población y coeficiente tras cerrar escala. No se conoce n analítico: fotos, tipos de falla, componentes y visitas no lo sustituyen. Un censo del frente permite descripción del ámbito; inferencia a otras vías requiere justificar población y mecanismo de generalización. No se adopta 19 por F005 ni tres por el software como suficiencia.

**7. Pavimentos: ¿cómo interpretar PCI?** Mantenerlo como condición creciente, conforme p. 13. Con drenaje creciente en deficiencia, coeficiente negativo significaría que mayores deficiencias se acompañan de menor PCI; positivo, que se acompañan de mayor PCI. Son interpretaciones condicionales, no resultados predichos. No transformar automáticamente a `100−PCI` ni rotular PCI como deterioro creciente.

## Método y lectura crítica del antecedente

Pearson resume asociación lineal; Spearman, asociación monótona por rangos. No elegirlos solo por una prueba de normalidad, ni tratar Spearman como remedio de dependencia. Revisar escala, dispersión, empates, valores influyentes y diseño. La documentación oficial SciPy 1.17.0 de `spearmanr` advierte que su p asintótica necesita especial cautela en muestras pequeñas; el motor utiliza esa opción predeterminada. Una permutación exige justificar intercambiabilidad; permutar filas espaciales dependientes indiscriminadamente no resuelve el problema. Pearson predeterminado también requiere justificar sus condiciones inferenciales.

En F005, §3.2 pp. 227–228 considera datos no apareados aunque las variables se observan por tramo. Tabla 10 p. 232 concluye rechazo porque diferencias de medias superan 0.5; esa operación no demuestra asociación ni documenta un contraste inferencial suficiente. Igualar escalas mediante PCI/25 (§4.3 p. 230) no vuelve comparables los constructos. Para Pearson, ese reescalado positivo por sí mismo no cambia el coeficiente. Tabla 11 sí informa r=0.14 y r=0.39; son resultados del antecedente, no de Jaén. Sus etiquetas de fuerza no se adoptan automáticamente. La tabla 8 p. 231 incluye ausencia=0, decisión que requiere crítica técnica antes de transferirse.

## Verificación, límites y cierre

`doctor` y `verify` fueron satisfactorios para estructura, con avisos esperados. `validate-data` y `describe` sobre pares reales terminaron con código 2: «No hay observaciones»; no se generaron descriptivos. Once pruebas seleccionadas de procedencia, duplicados, faltantes, constantes, correlaciones conocidas, Holm y aprobación pasaron. Los casos sintéticos permanecieron como pruebas, sin convertirse en evidencia de la tesis. Python 3.12.14 y SciPy 1.17.0; registro en `pruebas_selectivas.txt`.

No se ejecutó inferencia real. Mantener F2/F3/F5 pendientes hasta unidades y viabilidad justificadas, instrumento y PCI reproducibles, campaña definida, originales reales y aprobación documentada. El coordinador integrará hallazgos y devolverá las decisiones técnicas a sus responsables; el asesor deberá resolver cambios de ámbito o diseño si el reconocimiento muestra insuficiencia. `propuesta_plan_analisis.md` detalla las alternativas sin suplir datos ausentes.

**Documentación primaria consultada, 2026-10-14:** [SciPy 1.17.0 spearmanr](https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.stats.spearmanr.html), descripción y ejemplo de permutación; [pearsonr](https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.stats.pearsonr.html), descripción y condiciones de la p predeterminada. Son respaldo de software; no fuentes incorporadas al marco de la tesis ni aprobación de diseño.
