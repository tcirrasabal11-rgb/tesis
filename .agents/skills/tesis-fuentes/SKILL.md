---
name: tesis-fuentes
description: "Buscar y verificar artículos, tesis y normativa que sustentan esta investigación; crear fichas y trazabilidad de afirmaciones. Usar ante citas, antecedentes, cifras, vigencia o dudas de evidencia."
---

# Fuentes y antecedentes


## Contrato de trabajo
Leer AGENTS.md, ESTADO.md, DECISIONES.md, el contexto del encargo y config/proyecto.yaml. Aplicar el criterio de la fase actual. Citar archivos y fuente Fxxx con localización. Conservar originales y registrar propuestas y faltantes. Usar plantillas/INFORME_AGENTE.md para entregas; escribir solo en la carpeta asignada y dejar al coordinador la integración canónica.
La raíz es la carpeta que contiene AGENTS.md y config/proyecto.yaml. Ejecutar comandos desde ella y resolver los recursos del paquete contra esta raíz; no contra el directorio temporal del agente. Leer la referencia enlazada cuando se inicia el procedimiento o existe una duda sobre sus criterios.

## Procedimiento
1. Leer fuentes/registro.csv y priorizar las referencias que sostienen métodos, normativa y brecha. Tratar las filas iniciales como heredadas y pendientes.
2. Buscar por título/DOI en emisor o repositorio primario; abrir el documento. Registrar la cadena de acceso cuando DOI y URL difieran. Leer alcance, métodos y resultados pertinentes.
3. Conservar una copia legítima en fuentes/documentos y proponer hash, fecha, acceso y estado. Si solo hay resumen o bloqueo, indicar con precisión qué afirmación no puede verificarse.
4. Completar la ficha de fuente y afirmaciones. Distinguir mecanismo plausible, evidencia experimental, diagnóstico descriptivo y asociación estadística; registrar resultados débiles/adversos.
5. Proponer referencias CSL JSON solo desde metadatos comprobados. Pasar cambios al coordinador para integrar registro compartido. Ejecutar audit-citations para estructura, seguido de verificación semántica.
6. Comunicar a los agentes técnicos las diferencias de pavimento, clima, escala y procedimiento que afectan la comparación; no declarar una brecha exhaustiva tras búsquedas limitadas.

## Referencia y recursos
Leer [Criterios del procedimiento](references/criterios.md) al comenzar o revisar decisiones. Usar las plantillas de `plantillas/` y los comandos descritos en `docs/HERRAMIENTAS.md`. Para integración seguir `docs/PROTOCOLO_COLABORACION.md`.

## Criterio de terminado
El informe responde al encargo con evidencia localizada, cambios propuestos y pendientes precisos. El coordinador verifica los requisitos de la fase antes de cerrar.
