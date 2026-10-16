---
name: tesis-estadistica
description: "Validar pares de campo y diseñar/ejecutar análisis reproducible de asociación con PCI. Usar para n, supuestos, dependencia, datos faltantes, correlaciones, resultados e interpretación."
---

# Estadística de la tesis


## Contrato de trabajo
Leer AGENTS.md, ESTADO.md, DECISIONES.md, el contexto del encargo y config/proyecto.yaml. Aplicar el criterio de la fase actual. Citar archivos y fuente Fxxx con localización. Conservar originales y registrar propuestas y faltantes. Usar plantillas/INFORME_AGENTE.md para entregas; escribir solo en la carpeta asignada y dejar al coordinador la integración canónica.
La raíz es la carpeta que contiene AGENTS.md y config/proyecto.yaml. Ejecutar comandos desde ella y resolver los recursos del paquete contra esta raíz; no contra el directorio temporal del agente. Leer la referencia enlazada cuando se inicia el procedimiento o existe una duda sobre sus criterios.

## Procedimiento
1. Leer el plan, escala, mapa de unidades y diccionario. Confirmar origen real y versión de datos antes de cálculo.
2. Ejecutar validate-data y describe; revisar IDs, duplicados, fechas, valores, evidencia, dispersión, atípicos y faltantes. No modificar originales.
3. Justificar prueba y familia de comparaciones; evaluar independencia espacial/temporal, escala y ajuste por contexto. Si el motor simple es insuficiente, especificar y verificar un método adicional antes de inferencia.
4. Completar el plan con decisión previa y evidencia de aprobación. Ejecutar analyze únicamente con ese expediente; registrar exclusiones por par, n utilizado y hashes.
5. Revisar coeficientes, p y ajuste de multiplicidad. No concluir ausencia de relación por p grande, causalidad por significación ni fuerza por baremos sin fuente. Añadir incertidumbre adecuada cuando el diseño permita un método defendible.
6. Entregar resultados reproducibles y pasarlos a especialistas y metodología. Mantener cualquier exploración no prevista identificada como tal. La interpretación final debe corresponder a datos y alcance.

## Referencia y recursos
Leer [Criterios del procedimiento](references/criterios.md) al comenzar o revisar decisiones. Usar las plantillas de `plantillas/` y los comandos descritos en `docs/HERRAMIENTAS.md`. Para integración seguir `docs/PROTOCOLO_COLABORACION.md`.

## Criterio de terminado
El informe responde al encargo con evidencia localizada, cambios propuestos y pendientes precisos. El coordinador verifica los requisitos de la fase antes de cerrar.
