#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -c 'import sys; assert sys.version_info >= (3,11), "Python >= 3.11 requerido"'
if [ ! -d .venv ]; then python3 -m venv .venv; fi
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python tools/tesis.py verify
.venv/bin/python tools/tesis.py doctor
echo 'Abre esta carpeta en Codex y usa prompts/00_INICIAR_PROYECTO.md.'
