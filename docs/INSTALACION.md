# Instalación y recuperación

## Windows
Abre PowerShell en la raíz y ejecuta `./setup.ps1`. Si la política de ejecución impide un script local, puedes ejecutar manualmente:
```powershell
py -3 -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.txt
./.venv/Scripts/python.exe tools/tesis.py doctor
./.venv/Scripts/python.exe tools/tesis.py verify
```
No es necesario cambiar la política global de PowerShell. Los comandos usan el Python explícito de la carpeta, sin activar el entorno.

## Linux o macOS
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python tools/tesis.py doctor
.venv/bin/python tools/tesis.py verify
```
El script `setup.sh` realiza esos pasos y detiene el arranque si encuentra un error. Si faltan red o repositorios de paquetes, conserva la carpeta y resuelve la instalación con los paquetes autorizados en tu entorno.

## Codex
Usa el método de instalación oficial para tu plataforma, registrado en `docs/FUENTES_OFICIALES_CODEX.md`. El kit no ejecuta comandos remotos de instalación ni instala extensiones automáticamente. Comprueba `codex --version` y arranca desde esta raíz. No sobrescribas `~/.codex/config.toml`: este proyecto usa una capa local.

## Word y renderizado
Pandoc debe estar en PATH para la exportación. LibreOffice y pdftoppm deben estar disponibles para la conversión automática; el doctor comprueba su presencia. En Windows puedes usar Word para actualizar campos y exportar PDF, y documentar una revisión visual manual de cada página. Un DOCX generado no es prueba de que su paginación final esté revisada.

## Fallos y recuperación
- Skills ausentes: verifica carpeta raíz, nombres, YAML y `/skills`; reinicia Codex.
- Agentes ausentes: revisa versión y la documentación actual; comprueba `.codex/agents` y nombres. No simules actividad de subagentes.
- Modelo/esfuerzo no admitido: elige un modelo accesible y ajusta la opción; no uses un nombre inventado.
- Hash del original diferente: detén edición de ese archivo, compara versiones y restaura desde el adjunto; no actualices el hash para ocultar cambios.
- Datos rechazados: corrige el problema con trazabilidad; no desactives controles para conseguir un resultado.
- Exportación final bloqueada: revisa el informe de faltantes; continúa en modo borrador hasta cerrar requisitos reales.
