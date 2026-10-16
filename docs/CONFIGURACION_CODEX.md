# Configuración de Codex para el proyecto

## Alcance de la configuración
Esta plantilla se dirige a Codex local en CLI o extensión IDE. Los archivos del proyecto no configuran automáticamente un chat web hospedado. Abre la raíz del proyecto, revisa los archivos y acepta confiar en este proyecto cuando Codex lo solicite. Comprueba el estado efectivo con `/status`.

## Opciones del proyecto
`model_reasoning_effort="high"` propone un esfuerzo alto. Elige con `/model` un modelo disponible que admita ese nivel; cambia el ajuste si tu cliente no lo permite. No hay modelos, proveedores ni credenciales fijados.
`web_search="live"` solicita búsqueda actual. No demuestra por sí solo la veracidad de resultados ni elimina restricciones de acceso a un artículo.
`sandbox_mode="workspace-write"` permite comandos con escritura en el espacio autorizado. `network_access=true` habilita red para esos comandos dentro de las restricciones efectivas. La búsqueda web y la red de comandos son capacidades diferentes.
`approval_policy="on-request"` mantiene solicitudes para acciones que las necesiten. Las instrucciones del proyecto no exigen confirmaciones para cada borrador o revisión. Las políticas del equipo o del cliente pueden prevalecer.
`[agents] enabled=true` habilita colaboración. `max_concurrent_threads_per_session=3` limita subagentes abiertos, sin contar el principal. Los seis perfiles son un catálogo, no una orden de ejecutarlos todos simultáneamente.

## Perfiles personalizados
Cada `.codex/agents/*.toml` declara `name`, `description`, `developer_instructions` y esfuerzo. Las instrucciones obligan a leer el protocolo y la skill del dominio. Todos los subagentes heredan los permisos, proveedor y MCP de la sesión principal: `sandbox_mode` y `approval_policy` dentro de un perfil no crean permisos separados. Por eso se omitieron de los seis perfiles. Los encargos de lectura y las carpetas permitidas son restricciones de procedimiento, no aislamiento del sistema operativo. El coordinador debe verificar los permisos efectivos de la sesión y revisar las propuestas antes de integrarlas.

## Skills del repositorio
Se ubican en `.agents/skills/<nombre>/SKILL.md`, con metadatos de nombre y descripción. `agents/openai.yaml` contiene etiquetas de interfaz, no una definición de subagente. Las referencias de cada skill desarrollan rúbricas y ejemplos; las herramientas comunes están en `tools/tesis.py` para evitar duplicar código.
Abre `/skills` y comprueba los nueve nombres. Si no aparecen, reinicia desde la raíz y revisa el encabezado YAML. Invoca una con `$tesis-orquestar`. Usa `/agent` en CLI para inspeccionar hilos cuando esté disponible.

## Verificación real de descubrimiento
`verify` valida formatos locales contra las claves documentadas, sin ejecutar el runtime de Codex. Pide a Codex enumerar las instrucciones, las skills y los seis perfiles cargados. Después encarga una lectura corta a `investigador_fuentes` y otra a `revisor_academico`; confirma en la UI que son hilos distintos y que sus resultados se reúnen. Si la versión instalada no admite el formato actual, actualiza con el método oficial o ejecuta temporalmente pases secuenciales declarados. No añadas flags o comandos supuestos para solucionar el problema.

## Integraciones opcionales
El kit no necesita MCP ni claves API para arrancar con archivos locales. Añade un MCP únicamente si una herramienta real que utilizarás lo requiere, con configuración y documentación de su proveedor. No se incluyen servidores imaginarios de Zotero, ASTM o bases académicas. El servidor de documentación OpenAI sirve para Codex/API, no como biblioteca de ingeniería civil.

## Fuentes oficiales consultadas
Fecha de revisión: 2026-10-13. Consulta `docs/FUENTES_OFICIALES_CODEX.md` antes de modificar esquemas. Las opciones pueden cambiar entre versiones; anota el resultado de `codex --version` y revisa los permisos efectivos.

## Revisión de compatibilidad 2026-10-14
Se volvieron a abrir las páginas oficiales de Subagents, Configuration Reference y Build skills. Se confirmó el formato de agentes independientes, las claves de concurrencia y el descubrimiento de `.agents/skills`. Se corrigió la asignación de sandbox en perfiles, que no redefine los permisos heredados. La comprobación es documental y estructural; el descubrimiento real en el CLI/IDE del usuario sigue pendiente.
