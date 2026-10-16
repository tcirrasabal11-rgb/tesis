#!/usr/bin/env python3
"""Herramientas de proyecto. Los controles estructurales no certifican una tesis."""
from __future__ import annotations
import argparse
import csv
import hashlib
import importlib.metadata
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import struct
import zlib
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = {'investigador_fuentes', 'especialista_drenaje', 'especialista_pavimentos',
          'metodologo', 'estadistico', 'revisor_academico'}
SKILLS = {'tesis-orquestar', 'tesis-fuentes', 'tesis-drenaje', 'tesis-pavimentos-pci',
          'tesis-metodologia', 'tesis-estadistica', 'tesis-redaccion', 'tesis-auditar',
          'tesis-entregables'}
REQUIRED_PAIR = {'subtramo_id', 'fecha', 'pci', 'deficiencia_drenaje',
                 'origen_pci', 'origen_drenaje', 'procedencia'}
NUMERIC_PAIR = ['pci', 'deficiencia_drenaje', 'deficiencia_captacion_conduccion',
                'deficiencia_operatividad_mantenimiento']

class ProjectError(Exception):
    pass

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def yaml_load(path: Path):
    try:
        import yaml
    except ImportError as exc:
        raise ProjectError('Falta PyYAML. Instala requirements.txt en el entorno local.') from exc
    try:
        return yaml.safe_load(path.read_text(encoding='utf-8'))
    except (OSError, yaml.YAMLError) as exc:
        raise ProjectError(f'YAML no legible: {path}: {exc}') from exc

def within(path: Path, base: Path | None = None) -> bool:
    base = ROOT if base is None else base
    return path.resolve().is_relative_to(base.resolve())

def source_path(value: str) -> Path:
    p = Path(value)
    if p.is_absolute():
        raise ProjectError(f'La evidencia debe usar una ruta relativa a la raíz: {value}')
    p = (ROOT / p).resolve()
    if not within(p):
        raise ProjectError(f'La ruta de evidencia sale del proyecto: {value}')
    if not p.is_file() or p.stat().st_size == 0:
        raise ProjectError(f'Falta evidencia local o está vacía: {value}')
    return p

def output_path(value: str, overwrite: bool = False, directory: bool = False) -> Path:
    p = Path(value)
    if not p.is_absolute():
        p = ROOT / p
    p = p.resolve()
    if not within(p):
        raise ProjectError('Las salidas deben estar dentro del proyecto.')
    protected = [ROOT/'requisitos', ROOT/'datos/originales', ROOT/'datos/campo',
                 ROOT/'.codex', ROOT/'.agents', ROOT/'fuentes/documentos']
    if any(within(p, x) for x in protected):
        raise ProjectError(f'Ruta de salida protegida para estas herramientas: {p}')
    if p.exists() and not overwrite:
        raise ProjectError(f'La salida ya existe: {p}. Usa otra versión o --overwrite para una salida reproducible.')
    if directory:
        p.mkdir(parents=True, exist_ok=True)
    else:
        p.parent.mkdir(parents=True, exist_ok=True)
    return p

def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False))

def save_json(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8')

def validate_png(path: Path):
    """Verifica estructura y CRC. No sustituye la inspección visual ni decodifica píxeles."""
    with path.open('rb') as file:
        if file.read(8)!=b'\x89PNG\r\n\x1a\n':
            raise ProjectError('Imagen PNG no válida: '+str(path))
        has_header=False;has_data=False
        while True:
            header=file.read(8)
            if len(header)!=8:
                raise ProjectError('PNG truncado o sin IEND: '+str(path))
            length,kind=struct.unpack('>I4s',header)
            # Un chunk no puede superar el tamaño del archivo de salida.
            if length>path.stat().st_size:
                raise ProjectError('Longitud de chunk PNG no válida: '+str(path))
            content=file.read(length);crc=file.read(4)
            if len(content)!=length or len(crc)!=4:
                raise ProjectError('PNG truncado: '+str(path))
            if zlib.crc32(kind+content)&0xffffffff != struct.unpack('>I',crc)[0]:
                raise ProjectError('CRC de PNG no válido: '+str(path))
            if kind==b'IHDR':
                if has_header or length!=13:
                    raise ProjectError('IHDR no válido: '+str(path))
                has_header=True
            elif kind==b'IDAT':has_data=True
            elif kind==b'IEND':
                if length!=0 or not has_header or not has_data or file.read(1):
                    raise ProjectError('Estructura PNG incompleta: '+str(path))
                return

def read_csv(path: Path):
    try:
        with path.open(encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            fields = reader.fieldnames or []
            if len(fields) != len(set(fields)):
                raise ProjectError(f'Columnas duplicadas en {path}')
            rows = []
            for line, row in enumerate(reader, 2):
                if None in row:
                    raise ProjectError(f'Fila {line}: más valores que columnas. Comprueba separador y comillas.')
                if any(v is None for v in row.values()):
                    raise ProjectError(f'Fila {line}: menos valores que columnas.')
                if not any(v.strip() for v in row.values()):
                    continue
                rows.append({k: v.strip() for k, v in row.items()})
            return fields, rows
    except (OSError, UnicodeError, csv.Error) as exc:
        raise ProjectError(f'CSV no legible: {path}: {exc}') from exc

def read_input(value: str) -> Path:
    p = Path(value)
    return p.resolve() if p.is_absolute() else (ROOT/p).resolve()

def validate_pairs(path: Path, require_real=True, require_evidence=True):
    fields, rows = read_csv(path)
    missing = REQUIRED_PAIR - set(fields)
    if missing:
        raise ProjectError('Faltan columnas: '+', '.join(sorted(missing)))
    if not rows:
        raise ProjectError('No hay observaciones. La plantilla vacía no contiene datos de campo.')
    errors, seen, parsed = [], set(), []
    expected_year = None
    project_path = ROOT/'config/proyecto.yaml'
    if require_real and project_path.is_file():
        expected_year = yaml_load(project_path).get('periodo_estudio')
    for lineno, row in enumerate(rows, 2):
        ident = row['subtramo_id']
        if not ident:
            errors.append(f'Fila {lineno}: subtramo_id vacío.')
        elif ident in seen:
            errors.append(f'Fila {lineno}: ID duplicado {ident}; revisa la unidad, no lo elimines automáticamente.')
        seen.add(ident)
        try:
            observed_date = date.fromisoformat(row['fecha'])
            if expected_year is not None and observed_date.year != expected_year:
                errors.append(f'Fila {lineno}: fecha fuera del periodo de estudio {expected_year}.')
        except ValueError:
            errors.append(f'Fila {lineno}: fecha inválida; usar AAAA-MM-DD.')
        if require_real and row['procedencia'] != 'campo_real':
            errors.append(f'Fila {lineno}: procedencia {row["procedencia"]!r}; se requieren datos de campo_real.')
        if not require_real and row['procedencia'] not in {'campo_real', 'sintetico_prueba'}:
            errors.append(f'Fila {lineno}: procedencia desconocida.')
        result = dict(row)
        for col in NUMERIC_PAIR:
            val = row.get(col, '')
            if val == '':
                result[col] = None
                continue
            try:
                value = float(val)
                if not math.isfinite(value):
                    raise ValueError('valor no finito')
                if col == 'pci' and not 0 <= value <= 100:
                    raise ValueError('fuera de [0,100]')
                if col != 'pci' and value < 0:
                    raise ValueError('puntuación de deficiencia negativa')
                result[col] = value
            except ValueError as exc:
                errors.append(f'Fila {lineno}: {col} inválido {val!r}: {exc}.')
        if require_evidence:
            for col in ['origen_pci', 'origen_drenaje']:
                if not row[col]:
                    errors.append(f'Fila {lineno}: {col} sin respaldo.')
                else:
                    try:
                        evidence = source_path(row[col])
                        if within(evidence, ROOT/'tests'):
                            raise ProjectError('La evidencia de pruebas no respalda datos reales.')
                    except ProjectError as exc:
                        errors.append(f'Fila {lineno}: {exc}')
        parsed.append(result)
    if errors:
        raise ProjectError('\n'.join(errors))
    return parsed

def verify_structure():
    errors, warnings = [], []
    config_path = ROOT/'.codex/config.toml'
    try:
        conf = tomllib.loads(config_path.read_text(encoding='utf-8'))
        if conf.get('web_search') not in {'live','cached','indexed','disabled'}:
            errors.append('web_search no tiene un valor documentado.')
        if conf.get('sandbox_mode') != 'workspace-write':
            warnings.append('Sandbox distinto del previsto; revisa el permiso efectivo.')
        agents_conf = conf.get('agents',{})
        if agents_conf.get('enabled') is not True:
            errors.append('La colaboración del proyecto está deshabilitada.')
        cap = agents_conf.get('max_concurrent_threads_per_session')
        if not isinstance(cap,int) or isinstance(cap,bool) or cap < 1:
            errors.append('Límite de agentes inválido.')
        if conf.get('approval_policy') not in {'on-request','never'}:
            errors.append('Política inesperada; el kit admite on-request o never, revisa documentación.')
    except (OSError,tomllib.TOMLDecodeError) as exc:
        errors.append(f'config.toml: {exc}')
    found_agents = set()
    for file in sorted((ROOT/'.codex/agents').glob('*.toml')):
        try:
            cfg=tomllib.loads(file.read_text(encoding='utf-8'))
            for field in ['name','description','developer_instructions']:
                if not isinstance(cfg.get(field),str) or not cfg[field].strip():
                    errors.append(f'{file.name}: falta {field}.')
            name=cfg.get('name')
            if name in found_agents:
                errors.append(f'Nombre de agente duplicado: {name}')
            found_agents.add(name)
            for field in ['sandbox_mode','approval_policy','model_provider','mcp_servers']:
                if field in cfg:
                    errors.append(f'{file.name}: {field} no redefine los permisos/proveedor del padre en un agente personalizado; configúralo en la sesión principal.')
        except (OSError,tomllib.TOMLDecodeError) as exc:
            errors.append(f'{file.name}: {exc}')
    if found_agents != AGENTS:
        errors.append(f'Catálogo de agentes diferente. Esperados: {sorted(AGENTS)}; encontrados: {sorted(found_agents)}')
    found_skills=set()
    import yaml
    for file in sorted((ROOT/'.agents/skills').glob('*/SKILL.md')):
        text=file.read_text(encoding='utf-8')
        match=re.match(r'^---\s*\n(.*?)\n---\s*\n',text,re.S)
        if not match:
            errors.append(f'{file.parent.name}: falta frontmatter YAML.');continue
        try:
            meta=yaml.safe_load(match.group(1))
            if not isinstance(meta,dict):
                raise ValueError('metadatos deben ser un mapa')
            if set(meta) != {'name','description'}:
                errors.append(f'{file.parent.name}: metadatos inesperados.')
            name=meta.get('name','')
            if not re.fullmatch(r'[a-z0-9-]{1,64}',name) or name!=file.parent.name:
                errors.append(f'{file.parent.name}: nombre inválido.')
            if name in found_skills:
                errors.append(f'Skill duplicada: {name}')
            found_skills.add(name)
            if not str(meta.get('description','')).strip():
                errors.append(f'{file.parent.name}: descripción vacía.')
            interface=yaml_load(file.parent/'agents/openai.yaml')['interface']
            if '$'+name not in interface.get('default_prompt',''):
                errors.append(f'{name}: default_prompt no invoca su skill.')
            length=len(interface.get('short_description',''))
            if not 25 <= length <= 64:
                errors.append(f'{name}: descripción de interfaz fuera de 25-64 caracteres.')
            for target in re.findall(r'\]\((references/[^)]+)\)',text):
                if not (file.parent/target).is_file():
                    errors.append(f'{name}: referencia ausente: {target}')
        except (yaml.YAMLError,ValueError,KeyError,TypeError,ProjectError) as exc:
            errors.append(f'{file.parent.name}: {exc}')
    if found_skills != SKILLS:
        errors.append('Catálogo de nueve skills incompleto o diferente.')
    try:
        project=yaml_load(ROOT/'config/proyecto.yaml')
        plan=yaml_load(ROOT/'config/plan_analisis.yaml')
        yaml_load(ROOT/'metodologia/escala_drenaje.yaml')
        for path in project['archivos_capitulos']:
            if not (ROOT/path).is_file():
                errors.append(f'Capítulo ausente: {path}')
        if plan['estado'] != 'aprobado':
            warnings.append('Plan de análisis pendiente: estado esperado en una plantilla sin campo.')
        integrity=json.loads((ROOT/'requisitos/integridad_original.json').read_text(encoding='utf-8'))
        if digest(ROOT/integrity['archivo']) != integrity['sha256']:
            errors.append('El PDF original cambió. No actualices el hash para ocultar la modificación.')
        _,refs=read_csv(ROOT/'fuentes/registro.csv')
        ids=[r['fuente_id'] for r in refs]
        if len(ids)!=len(set(ids)):
            errors.append('IDs bibliográficos duplicados.')
        if any(r['estado']!='verificada' for r in refs):
            warnings.append('Hay referencias heredadas pendientes; no usarlas como verificadas.')
        original_manifest=ROOT/'datos/manifest_originales.json'
        if original_manifest.is_file():
            original_record=json.loads(original_manifest.read_text(encoding='utf-8'))
            registered=set()
            for item in original_record['archivos']:
                file=source_path(item['archivo'])
                if not within(file,ROOT/'datos/originales'):
                    errors.append('Manifest de originales incluye una ruta que no pertenece a originales.')
                if digest(file)!=item['sha256']:
                    errors.append('Un original registrado cambió: '+item['archivo'])
                registered.add(file)
            current={p.resolve() for p in (ROOT/'datos/originales').rglob('*') if p.is_file() and p.name!='.gitkeep'}
            if current-registered:
                warnings.append('Hay archivos originales nuevos sin registrar; conservar el manifest previo y registrar nueva versión.')
        else:
            warnings.append('Originales de campo aún no registrados; esperado antes de la recolección.')
    except (OSError,KeyError,ValueError,ProjectError) as exc:
        errors.append(str(exc))
    for file in ['AGENTS.md','README.md','ESTADO.md','DECISIONES.md','docs/PROTOCOLO_COLABORACION.md','docs/FASES_Y_CRITERIOS.md','datos/DICCIONARIO.md']:
        if not (ROOT/file).is_file():
            errors.append('Archivo esencial ausente: '+file)
    return {'ok':not errors,'errores':errors,'avisos':warnings,
            'alcance':'Validación estructural propia. No ejecuta Codex ni certifica la investigación.'}

def approved_plan(path: Path):
    plan=yaml_load(path)
    if not isinstance(plan,dict) or plan.get('estado')!='aprobado':
        raise ProjectError('La inferencia requiere un plan aprobado con evidencia real.')
    for key in ['aprobado_por','fecha_aprobacion','evidencia_aprobacion','evidencia_independencia',
                'evidencia_instrumento','justificacion_metodo']:
        if not isinstance(plan.get(key),str) or not plan[key].strip():
            raise ProjectError('Falta un campo de aprobación/justificación: '+key)
    try:
        date.fromisoformat(plan['fecha_aprobacion'])
    except ValueError as exc:
        raise ProjectError('Fecha de aprobación no válida.') from exc
    for key in ['evidencia_aprobacion','evidencia_independencia','evidencia_instrumento']:
        evidence=source_path(plan[key])
        if within(evidence,ROOT/'tests'):
            raise ProjectError('Evidencia de pruebas no es aprobación real.')
    if plan.get('independencia_justificada') is not True:
        raise ProjectError('Independencia no justificada. Revisar dependencia y método con estadística.')
    if plan.get('escala_drenaje_validada') is not True:
        raise ProjectError('La escala de drenaje no consta como validada.')
    if plan.get('metodo') not in {'pearson','spearman'}:
        raise ProjectError('Este motor admite pearson o spearman; desarrollar otro método si el diseño lo exige.')
    alpha=plan.get('alfa')
    if not isinstance(alpha,(int,float)) or isinstance(alpha,bool) or not 0 < alpha < 1:
        raise ProjectError('alfa debe estar entre 0 y 1.')
    if plan.get('ajuste_multiplicidad') not in {'holm','none'}:
        raise ProjectError('Ajuste soportado: holm o none; justificar la elección.')
    if plan.get('faltantes') != 'excluir_por_par_con_registro':
        raise ProjectError('El motor solo implementa exclusión por par registrada.')
    if plan.get('intervalo_confianza','none') != 'none':
        raise ProjectError('El motor no implementa ese intervalo. Usar un script justificado y validado.')
    if plan.get('unidad_analisis')!='subtramo_id':
        raise ProjectError('El archivo de pares requiere subtramo_id como unidad.')
    comps=plan.get('comparaciones')
    if not isinstance(comps,list) or not comps:
        raise ProjectError('No hay comparaciones previstas.')
    seen=set()
    for comp in comps:
        if not isinstance(comp,dict) or set(comp) != {'id','x','y'}:
            raise ProjectError('Cada comparación requiere id, x e y.')
        if not re.fullmatch(r'[a-z0-9_]+',str(comp['id'])) or comp['id'] in seen:
            raise ProjectError('ID de comparación inválido o duplicado.')
        seen.add(comp['id'])
        if comp['x'] not in NUMERIC_PAIR[1:] or comp['y']!='pci':
            raise ProjectError('Variables no soportadas por el motor de correlaciones con PCI.')
    return plan

def descriptions(rows):
    output={'n_subtramos':len(rows),'sentido_pci':'Mayor PCI representa mejor condición superficial.','variables':{}}
    for key in NUMERIC_PAIR:
        vals=sorted(r[key] for r in rows if r.get(key) is not None)
        n=len(vals)
        median=(vals[(n-1)//2]+vals[n//2])/2 if n else None
        output['variables'][key]={'n':n,'faltantes':len(rows)-n,'min':min(vals) if n else None,
                                  'max':max(vals) if n else None,'media':sum(vals)/n if n else None,
                                  'mediana':median}
    return output

def holm_adjust(pvalues):
    n=len(pvalues)
    order=sorted(range(n),key=lambda i:pvalues[i])
    result=[0.0]*n
    previous=0.0
    for rank,idx in enumerate(order):
        previous=max(previous,min(1.0,(n-rank)*pvalues[idx]))
        result[idx]=previous
    return result

def correlations(rows,plan):
    try:
        from scipy import stats
    except ImportError as exc:
        raise ProjectError('Falta SciPy para analizar.') from exc
    results=[]
    for comp in plan['comparaciones']:
        used=[r for r in rows if r.get(comp['x']) is not None and r.get(comp['y']) is not None]
        excluded=[r['subtramo_id'] for r in rows if r not in used]
        if len(used)<3:
            raise ProjectError(f'{comp["id"]}: menos de tres pares computables. Esto no define suficiencia de muestra.')
        x=[r[comp['x']] for r in used];y=[r[comp['y']] for r in used]
        if len(set(x))<2 or len(set(y))<2:
            raise ProjectError(f'{comp["id"]}: una variable es constante; correlación no definida.')
        if plan['metodo']=='pearson':
            result=stats.pearsonr(x,y,alternative='two-sided')
        else:
            result=stats.spearmanr(x,y,alternative='two-sided')
        coefficient,p=float(result.statistic),float(result.pvalue)
        if not math.isfinite(coefficient) or not math.isfinite(p):
            raise ProjectError(f'{comp["id"]}: resultado no finito.')
        results.append({'id':comp['id'],'x':comp['x'],'y':comp['y'],'metodo':plan['metodo'],
                        'n':len(used),'coeficiente':coefficient,'p_cruda':p,
                        'ids_usados':[r['subtramo_id'] for r in used],'ids_excluidos_por_faltantes':excluded,
                        'pares':[{'subtramo_id':r['subtramo_id'],'x':r[comp['x']],'y':r[comp['y']]} for r in used]})
    adjusted=holm_adjust([r['p_cruda'] for r in results]) if plan['ajuste_multiplicidad']=='holm' else [r['p_cruda'] for r in results]
    for r,p in zip(results,adjusted):
        r['p_ajustada']=p;r['alfa']=plan['alfa'];r['ajuste']=plan['ajuste_multiplicidad']
    return results

def audit_citations():
    _,rows=read_csv(ROOT/'fuentes/registro.csv')
    registry={r['fuente_id']:r for r in rows}
    refs=json.loads((ROOT/'fuentes/referencias.json').read_text(encoding='utf-8'))
    if not isinstance(refs,list):
        raise ProjectError('referencias.json debe ser una lista CSL JSON.')
    bib_ids=[r.get('id') for r in refs if isinstance(r,dict)]
    bib=set(bib_ids)
    errors=[];pending=[];used=set()
    if len(bib_ids)!=len(bib) or None in bib:
        errors.append('IDs CSL JSON duplicados o ausentes.')
    project=yaml_load(ROOT/'config/proyecto.yaml')
    for value in project['archivos_capitulos']:
        file=ROOT/value;text=file.read_text(encoding='utf-8')
        for lineno,line in enumerate(text.splitlines(),1):
            for ident in re.findall(r'(?<![\w@])@([A-Za-z][A-Za-z0-9_-]*)',line):
                used.add(ident)
                if ident not in registry:
                    errors.append(f'{value}:{lineno}: fuente desconocida {ident}.')
                else:
                    row=registry[ident]
                    if row['estado']!='verificada':
                        errors.append(f'{value}:{lineno}: fuente pendiente {ident}.')
                    else:
                        try:
                            for key in ['titulo','autores','anio','acceso','archivo','sha256','fecha_consulta']:
                                if not row.get(key):
                                    raise ProjectError(f'{ident}: falta {key} en una fuente declarada verificada.')
                            evidence=source_path(row['archivo'])
                            if digest(evidence)!=row['sha256']:
                                raise ProjectError(f'{ident}: el hash de la fuente no corresponde a la copia registrada.')
                            date.fromisoformat(row['fecha_consulta'])
                        except (ProjectError,ValueError) as exc:
                            errors.append(f'{value}:{lineno}: {exc}')
                    if ident not in bib:
                        errors.append(f'{value}:{lineno}: falta CSL JSON para {ident}.')
            if re.search(r'\[PENDIENTE\b|\bTODO\b|\bPENDIENTE_FORMULACION\b',line,re.I):
                pending.append(f'{value}:{lineno}: contenido pendiente.')
    return {'errores':errors,'pendientes':pending,'fuentes_citadas':sorted(used),
            'alcance':'Detector estructural. Debe completarse con lectura semántica de fuentes y capítulos.'}

def final_checks():
    project=yaml_load(ROOT/'config/proyecto.yaml');errors=[]
    if project.get('estado_requisitos')!='aprobado' or project.get('formato_validado') is not True:
        errors.append('Requisitos o formato institucional pendientes.')
    for key in ['guia_institucional','plantilla_word']:
        try:
            if not project.get(key):
                raise ProjectError(f'Falta {key}.')
            source_path(project[key])
        except ProjectError as exc:
            errors.append(str(exc))
    audit=audit_citations();errors.extend(audit['errores']);errors.extend(audit['pendientes'])
    if not (ROOT/'datos/manifest_originales.json').is_file():
        errors.append('Falta el manifest de integridad de los originales de campo.')
    else:
        structure=verify_structure();errors.extend(structure['errores'])
    try:
        approved_plan(ROOT/'config/plan_analisis.yaml')
        validate_pairs(ROOT/'datos/campo/pares_analisis.csv')
    except ProjectError as exc:
        errors.append(str(exc))
    try:
        if not project.get('expediente_analisis'):
            raise ProjectError('Falta expediente_analisis con el manifest de resultados reales.')
        manifest_path=source_path(project['expediente_analisis'])
        manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
        for key,path in [('input_sha256',ROOT/'datos/campo/pares_analisis.csv'),
                         ('plan_sha256',ROOT/'config/plan_analisis.yaml')]:
            if manifest.get(key)!=digest(path):
                raise ProjectError('El análisis no corresponde a la versión actual: '+key)
        source_path(str(manifest_path.with_name('resultados.json').relative_to(ROOT)))
    except (ProjectError,OSError,ValueError,KeyError) as exc:
        errors.append(str(exc))
    review=ROOT/'coordinacion/revisiones/cierre_final.yaml'
    if not review.is_file():
        errors.append('Falta cierre_final.yaml con revisión académica real registrada.')
    else:
        data=yaml_load(review)
        if not isinstance(data,dict) or data.get('estado')!='aprobado' or not data.get('responsable') or not data.get('evidencia'):
            errors.append('Registro de cierre final incompleto.')
        else:
            try:source_path(data['evidencia'])
            except ProjectError as exc:errors.append(str(exc))
    if errors:
        raise ProjectError('Entrega final bloqueada por requisitos pendientes:\n'+'\n'.join(errors))
    return project

def doctor():
    versions={}
    for name in ['PyYAML','pypdf','numpy','scipy','python-docx']:
        try:versions[name]=importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:versions[name]=None
    tools={name:shutil.which(name) for name in ['codex','git','pandoc','libreoffice','soffice','pdftoppm']}
    version=None
    if tools['codex']:
        try:
            result=subprocess.run([tools['codex'],'--version'],capture_output=True,text=True,timeout=15,check=True)
            version=result.stdout.strip()
        except (subprocess.SubprocessError,OSError):version='No se pudo consultar.'
    return {'python':sys.version.split()[0],'python_compatible':sys.version_info>=(3,11),'dependencias':versions,
            'herramientas':tools,'codex_version':version,'avisos':[
                'Codex debe confirmar descubrimiento de skills y perfiles en la instalación real.',
                'Pandoc es opcional hasta exportar; LibreOffice y pdftoppm hasta renderizar.',
                'Los controles del kit no certifican validación académica ni suficiencia de la muestra.']}

def export_docx(mode, output, overwrite=False):
    project=final_checks() if mode=='final' else yaml_load(ROOT/'config/proyecto.yaml')
    pandoc=shutil.which('pandoc')
    if not pandoc:
        raise ProjectError('Falta Pandoc en PATH. Instálalo por el método oficial o usa el motor autorizado.')
    out=output_path(output,overwrite)
    if out.suffix.lower()!='.docx':
        raise ProjectError('export genera DOCX; usar render para PDF.')
    chapters=[source_path(p) for p in project['archivos_capitulos']]
    for chapter in chapters:
        if out==chapter:
            raise ProjectError('La salida no puede sobrescribir un capítulo.')
    args=[pandoc,'--from=markdown','--to=docx','--standalone','--toc',
          '--metadata','lang=es-PE','--metadata','toc-title=Índice',
          '--metadata',f'title={project["tema"]}','--metadata',f'author={project["autora"]}']
    if not project.get('plantilla_word'):
        base=ROOT/'plantillas/referencia_base.docx'
        if not base.is_file():
            raise ProjectError('Falta referencia_base.docx para borrador o una plantilla_word institucional.')
        args += ['--reference-doc',str(base)]
    for key,flag in [('plantilla_word','--reference-doc'),('archivo_csl','--csl')]:
        if project.get(key):args += [flag,str(source_path(project[key]))]
    refs_path=ROOT/'fuentes/referencias.json'
    refs=json.loads(refs_path.read_text(encoding='utf-8'))
    if refs:
        args += ['--citeproc','--bibliography',str(refs_path)]
    elif any(re.search(r'@F\d+',p.read_text(encoding='utf-8')) for p in chapters):
        raise ProjectError('Hay citas pero falta bibliografía CSL JSON utilizable; no exportar citas sin resolver.')
    args += [str(p) for p in chapters]+['--output',str(out)]
    result=subprocess.run(args,capture_output=True,text=True,timeout=180)
    if result.returncode:
        raise ProjectError('Pandoc falló: '+result.stderr.strip())
    if not out.is_file() or out.stat().st_size==0:
        raise ProjectError('Pandoc no produjo un DOCX válido.')
    record={'archivo':str(out.relative_to(ROOT)),'sha256':digest(out),'modo':mode,'comando':args,
            'fecha_utc':datetime.now(timezone.utc).isoformat(),'revision_visual':'pendiente','avisos_pandoc':result.stderr.strip()}
    save_json(out.with_suffix('.manifest.json'),record)
    return record

def render_docx(input_value,output,overwrite=False):
    file=read_input(input_value)
    if not file.is_file() or file.suffix.lower()!='.docx':
        raise ProjectError('Se requiere un DOCX existente.')
    office=shutil.which('libreoffice') or shutil.which('soffice')
    poppler=shutil.which('pdftoppm')
    if not office or not poppler:
        raise ProjectError('Render requiere LibreOffice/soffice y pdftoppm. Registrar revisión manual con Word si faltan.')
    dest=output_path(output,overwrite,directory=True)
    with tempfile.TemporaryDirectory(prefix='tesis-office-') as tmp:
        profile=Path(tmp)/'perfil';profile.mkdir()
        result=subprocess.run([office,f'-env:UserInstallation={profile.as_uri()}','--headless','--convert-to','pdf',
                               '--outdir',str(dest),str(file)],capture_output=True,text=True,timeout=180)
        pdf=dest/(file.stem+'.pdf')
        if result.returncode or not pdf.is_file() or pdf.stat().st_size==0:
            raise ProjectError('Conversión PDF falló: '+result.stderr.strip()+' '+result.stdout.strip())
    result=subprocess.run([poppler,'-r','120','-png',str(pdf),str(dest/'pagina')],capture_output=True,text=True,timeout=180)
    if result.returncode:
        raise ProjectError('Render PNG falló: '+result.stderr.strip())
    pages=sorted(dest.glob('pagina-*.png'))
    if not pages:
        raise ProjectError('No se generaron páginas PNG.')
    for page in pages:validate_png(page)
    record={'docx_sha256':digest(file),'pdf':str(pdf.relative_to(ROOT)),'pdf_sha256':digest(pdf),
            'paginas_png':len(pages),'revision_visual':'pendiente; inspeccionar todas las páginas'}
    save_json(dest/'render_manifest.json',record)
    return record

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    for name in ['doctor','verify','audit-citations']:sub.add_parser(name)
    cmd=sub.add_parser('snapshot-originals');cmd.add_argument('--output',default='datos/manifest_originales.json');cmd.add_argument('--overwrite',action='store_true')
    for name in ['validate-data','describe','analyze']:
        cmd=sub.add_parser(name);cmd.add_argument('--input',required=True)
        if name!='validate-data':
            cmd.add_argument('--output',required=True);cmd.add_argument('--overwrite',action='store_true')
        if name=='analyze':cmd.add_argument('--plan',default='config/plan_analisis.yaml')
    cmd=sub.add_parser('extract-pdf');cmd.add_argument('--input',required=True);cmd.add_argument('--output',required=True);cmd.add_argument('--overwrite',action='store_true')
    cmd=sub.add_parser('export');cmd.add_argument('--mode',choices=['draft','final'],default='draft');cmd.add_argument('--output',required=True);cmd.add_argument('--overwrite',action='store_true')
    cmd=sub.add_parser('render');cmd.add_argument('--input',required=True);cmd.add_argument('--output',required=True);cmd.add_argument('--overwrite',action='store_true')
    args=parser.parse_args(argv)
    try:
        if args.command=='doctor':emit(doctor())
        elif args.command=='verify':
            result=verify_structure();emit(result);return 0 if result['ok'] else 2
        elif args.command=='audit-citations':
            result=audit_citations();emit(result);return 2 if result['errores'] or result['pendientes'] else 0
        elif args.command=='snapshot-originals':
            files=sorted(p for p in (ROOT/'datos/originales').rglob('*') if p.is_file() and p.name!='.gitkeep')
            if not files:
                raise ProjectError('No hay originales de campo para registrar. No crear un manifest vacío.')
            for file in files:
                if not within(file,ROOT/'datos/originales'):
                    raise ProjectError('Un enlace de originales apunta fuera de su carpeta.')
            out=output_path(args.output,args.overwrite)
            record={'fecha_utc':datetime.now(timezone.utc).isoformat(),'archivos':[
                {'archivo':str(p.relative_to(ROOT)),'sha256':digest(p),'bytes':p.stat().st_size} for p in files]}
            save_json(out,record);emit({'salida':str(out),'archivos_registrados':len(files)})
        elif args.command=='validate-data':
            rows=validate_pairs(read_input(args.input));emit({'ok':True,'n_subtramos':len(rows),'limite':'No verifica veracidad de campo, escala ni independencia.'})
        elif args.command=='describe':
            file=read_input(args.input);rows=validate_pairs(file);out=output_path(args.output,args.overwrite)
            result=descriptions(rows);result['input_sha256']=digest(file);save_json(out,result);emit({'salida':str(out),'n':len(rows)})
        elif args.command=='analyze':
            file=read_input(args.input);plan_path=read_input(args.plan)
            input_hash,plan_hash=digest(file),digest(plan_path)
            rows=validate_pairs(file);plan=approved_plan(plan_path);results=correlations(rows,plan)
            evidence_hashes={r[k]:digest(source_path(r[k])) for r in rows for k in ['origen_pci','origen_drenaje']}
            if digest(file)!=input_hash or digest(plan_path)!=plan_hash:
                raise ProjectError('Los datos o el plan cambiaron durante el análisis. Congelar insumos y repetir.')
            dest=output_path(args.output,args.overwrite,directory=True)
            payload={'descripciones':descriptions(rows),'comparaciones':results,'advertencia':'Asociación estadística; el motor no establece causalidad ni certifica supuestos.'}
            save_json(dest/'resultados.json',payload)
            manifest={'fecha_utc':datetime.now(timezone.utc).isoformat(),'input_sha256':input_hash,
                      'plan_sha256':plan_hash,'script_sha256':digest(Path(__file__)),
                      'python':sys.version.split()[0],'scipy':importlib.metadata.version('scipy'),
                      'numpy':importlib.metadata.version('numpy'),
                      'comando':[sys.executable]+(argv if argv is not None else sys.argv[1:]),
                      'evidencias':evidence_hashes,
                      'aprobaciones':{k:digest(source_path(plan[k])) for k in ['evidencia_aprobacion','evidencia_independencia','evidencia_instrumento']}}
            save_json(dest/'manifest.json',manifest)
            with (dest/'pares_usados.csv').open('w',encoding='utf-8-sig',newline='') as f:
                writer=csv.DictWriter(f,fieldnames=['comparacion_id','subtramo_id','x','y']);writer.writeheader()
                for result in results:
                    for pair in result['pares']:writer.writerow({'comparacion_id':result['id'],**pair})
            emit({'salida':str(dest),'comparaciones':len(results)})
        elif args.command=='extract-pdf':
            try:from pypdf import PdfReader
            except ImportError as exc:raise ProjectError('Falta pypdf.') from exc
            file=read_input(args.input)
            if not file.is_file():raise ProjectError('PDF no encontrado.')
            out=output_path(args.output,args.overwrite)
            if out==file:raise ProjectError('La extracción no puede sobrescribir el PDF.')
            reader=PdfReader(file);parts=[f'# Texto extraído\n\nOrigen: {file.name}\nSHA256: {digest(file)}\n'];needs_ocr=[]
            for idx,page in enumerate(reader.pages,1):
                text=page.extract_text() or ''
                if len(text.strip())<30:needs_ocr.append(idx)
                parts.append(f'\n## Página {idx}\n\n{text}')
            out.write_text('\n'.join(parts),encoding='utf-8')
            emit({'salida':str(out),'paginas':len(reader.pages),'paginas_con_poco_texto_revisar_ocr':needs_ocr})
        elif args.command=='export':emit(export_docx(args.mode,args.output,args.overwrite))
        elif args.command=='render':emit(render_docx(args.input,args.output,args.overwrite))
        return 0
    except (ProjectError,OSError,ValueError,KeyError,TypeError,subprocess.SubprocessError) as exc:
        print('ERROR: '+str(exc),file=sys.stderr);return 2

if __name__=='__main__':
    raise SystemExit(main())
