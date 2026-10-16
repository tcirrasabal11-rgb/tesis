$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (Get-Command py -ErrorAction SilentlyContinue) { & py -3 -c "import sys; assert sys.version_info >= (3,11), 'Python >= 3.11 requerido'"; if ($LASTEXITCODE -ne 0) { throw 'Python incompatible' }; if (!(Test-Path '.venv')) { & py -3 -m venv .venv } }
elseif (Get-Command python -ErrorAction SilentlyContinue) { & python -c "import sys; assert sys.version_info >= (3,11), 'Python >= 3.11 requerido'"; if ($LASTEXITCODE -ne 0) { throw 'Python incompatible' }; if (!(Test-Path '.venv')) { & python -m venv .venv } }
else { throw 'Instala Python 3.11 o posterior.' }
if ($LASTEXITCODE -ne 0) { throw 'No se pudo crear el entorno' }
$TaskPython = Join-Path $PSScriptRoot '.venv/Scripts/python.exe'
if (!(Test-Path $TaskPython)) { throw 'La carpeta .venv no contiene el intérprete esperado.' }
& $TaskPython -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw 'No se pudieron instalar dependencias.' }
& $TaskPython tools/tesis.py verify
if ($LASTEXITCODE -ne 0) { throw 'Falló la verificación del proyecto.' }
& $TaskPython tools/tesis.py doctor
Write-Host 'Abre esta carpeta en Codex y usa prompts/00_INICIAR_PROYECTO.md.'
