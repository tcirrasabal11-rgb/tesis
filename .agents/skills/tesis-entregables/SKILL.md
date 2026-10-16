---
name: tesis-entregables
description: "Exportar Word/PDF y preparar una entrega académica revisada con fuentes, anexos y trazabilidad. Usar para compilar capítulos, aplicar plantilla institucional, renderizar y cerrar la entrega."
---

# Entregables Word y PDF


## Contrato de trabajo
Leer AGENTS.md, ESTADO.md, DECISIONES.md, el contexto del encargo y config/proyecto.yaml. Aplicar el criterio de la fase actual. Citar archivos y fuente Fxxx con localización. Conservar originales y registrar propuestas y faltantes. Usar plantillas/INFORME_AGENTE.md para entregas; escribir solo en la carpeta asignada y dejar al coordinador la integración canónica.
La raíz es la carpeta que contiene AGENTS.md y config/proyecto.yaml. Ejecutar comandos desde ella y resolver los recursos del paquete contra esta raíz; no contra el directorio temporal del agente. Leer la referencia enlazada cuando se inicia el procedimiento o existe una duda sobre sus criterios.

## Procedimiento
1. Leer docs/ENTREGABLES_Y_FORMATO.md y la guía institucional disponible. Revisar config/proyecto.yaml, bibliografía y orden de capítulos.
2. Ejecutar doctor y controles de citas. Exportar en draft cuando falten validaciones; final solo con el expediente real completo.
3. Ejecutar export con Pandoc, plantilla Word y CSL configurados. Evitar sobrescribir archivos existentes sin una versión nueva o --overwrite autorizado para una salida reproducible.
4. Convertir y renderizar con LibreOffice/pdftoppm cuando existan. Revisar cada página; registrar defectos, corregir el origen y repetir render de la versión final.
5. Actualizar índices/campos y verificar ecuaciones, tablas, gráficos, referencias cruzadas y anexos en el motor de entrega. Si hay revisión manual, registrar quién, versión y cobertura.
6. Preparar expediente final, control de versiones y registro de revisión. Entregar solo los archivos solicitados; preservar originales y QA para auditoría interna.

## Referencia y recursos
Leer [Criterios del procedimiento](references/criterios.md) al comenzar o revisar decisiones. Usar las plantillas de `plantillas/` y los comandos descritos en `docs/HERRAMIENTAS.md`. Para integración seguir `docs/PROTOCOLO_COLABORACION.md`.

## Criterio de terminado
El informe responde al encargo con evidencia localizada, cambios propuestos y pendientes precisos. El coordinador verifica los requisitos de la fase antes de cerrar.
