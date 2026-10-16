# Cómo usar este proyecto

Esta carpeta contiene la configuración para trabajar la tesis y una auditoría inicial ya ejecutada, R001. La auditoría identifica lo que puede aprovecharse del avance y las decisiones que faltan. No contiene mediciones de campo ni una tesis terminada.

## Qué abrir primero

1. `coordinacion/revisiones/auditoria_inicial.md`: informe integrado con prioridades y próximos entregables.
2. `coordinacion/salidas/`: informes reales de fuentes, drenaje, pavimentos, metodología, estadística y revisión académica.
3. `ESTADO.md`: punto exacto para continuar.

El PDF que proporcionaste como **avance de tesis.pdf** está incluido sin cambios en `requisitos/avance_original.pdf`. Su texto extraído está en `requisitos/avance_texto_extraido.txt`.

## Dónde están los agentes y las skills

| Carpeta | Qué contiene |
|---|---|
| `.codex/agents/` | Seis perfiles TOML con responsabilidades e instrucciones. |
| `.agents/skills/` | Nueve procedimientos con sus referencias y metadatos. |
| `coordinacion/salidas/<agente>/` | Informes y propuestas que entrega cada especialista. |
| `capitulos/` | Estructura de redacción; los capítulos pendientes se completan con evidencia y decisiones. |
| `datos/originales/` | Evidencia de campo cuando sea recolectada. |

Un archivo `.gitkeep` solo conserva una carpeta. Una carpeta de resultados o de datos vacía no significa que falte la configuración del agente. Los informes de R001 ya se incluyen en esta versión; las carpetas de datos seguirán vacías mientras no haya mediciones.

## Continuar en tu Codex

Abre la carpeta completa, la que contiene `AGENTS.md`, y sigue `docs/INSTALACION.md` una sola vez. Usa `prompts/00_INICIAR_PROYECTO.md` para comprobar tu instalación y cargar el estado existente. Después usa `prompts/07_CONTINUAR_SESION.md`.

La auditoría R001 se ejecutó mediante subagentes de esta sesión, aplicando los perfiles y skills del proyecto. El paquete registra esa ejecución; no afirma que ya se haya probado el descubrimiento automático en el Codex de tu PC.

## Añadir documentos

Guarda artículos, tesis, libros y normas en `fuentes/documentos/`. Guarda guía universitaria, rúbrica, observaciones del asesor y nuevas versiones del manuscrito en `requisitos/`. Después pide a Codex: **Incorpora los documentos nuevos siguiendo `prompts/08_INCORPORAR_DOCUMENTOS.md`.**

El coordinador registra y verifica los documentos. No necesitas editar CSV, perfiles o skills por cada archivo. Los pasos y límites están en `docs/AGREGAR_DOCUMENTOS.md`.
