# Proyecto Codex para la tesis de drenaje y pavimento en Pakamuros

Este proyecto permite continuar la tesis con un coordinador, seis agentes especializados y nueve skills, conservando fuentes, decisiones y datos. Incluye el avance original del usuario sin modificaciones. Las plantillas y herramientas están completas para el flujo definido; la información institucional, la validación académica y el trabajo de campo se incorporan cuando existan.

## Antes de empezar
Lee `EMPEZAR_AQUI.md`. Esta versión incluye los informes de la auditoría inicial R001 y una guía para incorporar documentos nuevos. La auditoría de entrada no equivale a resultados de campo ni a aprobación del asesor.

## Primer arranque
1. Extrae el paquete en una carpeta local, por ejemplo `C:\Tesis\Pakamuros`. Conserva toda la estructura, incluidas `.codex` y `.agents`.
2. Instala o actualiza Codex mediante la documentación oficial. En VS Code abre la carpeta completa e inicia sesión con la cuenta disponible; en CLI entra en la carpeta y ejecuta `codex`.
3. Instala Python 3.11 o posterior. Ejecuta en PowerShell `./setup.ps1`; en Linux/macOS usa `bash setup.sh`. Los scripts crean `.venv` local y solo instalan las dependencias de ese entorno; no instalan ni modifican Codex globalmente.
4. Elige con `/model` un modelo que admita el esfuerzo configurado. Confía en el proyecto cuando Codex lo solicite y consulta `/status`.
5. Comprueba `/skills` y los seis agentes. Sigue `docs/CONFIGURACION_CODEX.md` para una prueba real de descubrimiento. La plantilla no incluye credenciales, claves ni servicios externos.
6. Copia en Codex el contenido de `prompts/00_INICIAR_PROYECTO.md` para cargar el estado y comprobar tu instalación. Como R001 ya está ejecutada en esta versión, continúa con `prompts/07_CONTINUAR_SESION.md`. Usa `01_AUDITORIA_INICIAL.md` solo para una nueva ronda justificada por cambios de entradas.

## Componentes
El hilo principal coordina. Drenaje y pavimentos revisan sus instrumentos; metodología y estadística contrastan diseño y viabilidad; bibliografía verifica evidencia; revisión académica controla coherencia y entrega. Las instrucciones de colaboración están en `AGENTS.md` y `docs/PROTOCOLO_COLABORACION.md`.
Las skills son `tesis-orquestar`, `tesis-fuentes`, `tesis-drenaje`, `tesis-pavimentos-pci`, `tesis-metodologia`, `tesis-estadistica`, `tesis-redaccion`, `tesis-auditar` y `tesis-entregables`. Cada una contiene procedimiento, referencia de trabajo y metadatos de interfaz.

## Archivos de entrada
`requisitos/avance_original.pdf` es el documento de partida. La guía, rúbrica y plantilla institucional se colocan en requisitos y se registran en `config/proyecto.yaml`. Las referencias citadas por el avance se encuentran en `fuentes/registro.csv` con estados diferenciados de verificación; consulta el alcance y los límites de cada ficha. Los datos de campo usan CSV con diccionario en `datos/DICCIONARIO.md`. Para agregar documentos basta colocarlos en la carpeta correspondiente y encargar a Codex `prompts/08_INCORPORAR_DOCUMENTOS.md`; sigue `docs/AGREGAR_DOCUMENTOS.md`.

## Trabajo por fases
F0 audita; F1 verifica fuentes; F2 cierra diseño; F3 valida instrumentos; F4 incorpora campo; F5 analiza; F6 redacta; F7 revisa y entrega. `docs/FASES_Y_CRITERIOS.md` define cuándo puede cerrarse cada fase. El proyecto comienza en F0; no presupone que mediciones, normas o validaciones ya existen.

## Comandos y dependencias
Consulta `docs/HERRAMIENTAS.md`. Las verificaciones y CSV usan Python; análisis requiere SciPy; extracción PDF requiere pypdf; Word requiere Pandoc; render automático requiere LibreOffice y pdftoppm. Las dependencias opcionales ausentes se informan. Ver `docs/INSTALACION.md` y `docs/ENTREGABLES_Y_FORMATO.md`.

## Persistencia
Crea un repositorio Git local si no existe: `git init`. Antes de confirmar revisa `git status` y agrega solo archivos del proyecto. Cada sesión actualiza estado, decisiones y tareas. Conserva respaldos de datos originales y versiones de documentos. El paquete no presupone un repositorio remoto ni publica datos.

## Alcance de las verificaciones
`VALIDACION_PAQUETE.md` registra lo que se ha probado al generar esta versión. Los controles de software no certifican la tesis ni sustituyen la revisión del asesor. La ejecución real de Codex en tu PC, la visualización de Word/PDF y el análisis científico se confirman con los archivos y herramientas disponibles allí.
