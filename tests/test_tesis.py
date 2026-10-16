import csv
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PROJECT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('tesis',PROJECT/'tools/tesis.py')
tesis=importlib.util.module_from_spec(spec)
spec.loader.exec_module(tesis)

class DataAndStatistics(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='tesis-tests-')
        self.root=Path(self.tmp.name)
        self.patch=patch.object(tesis,'ROOT',self.root)
        self.patch.start()
        self.fields,self.rows=tesis.read_csv(PROJECT/'tests/fixtures/pares_sinteticos.csv')

    def tearDown(self):
        self.patch.stop();self.tmp.cleanup()

    def dataset(self,rows=None):
        path=self.root/'pares.csv'
        with path.open('w',encoding='utf-8-sig',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=self.fields)
            writer.writeheader();writer.writerows(rows or self.rows)
        return path

    def parsed(self):
        return tesis.validate_pairs(self.dataset(),require_real=False,require_evidence=False)

    def plan(self,method='spearman'):
        return {'metodo':method,'alfa':0.05,'ajuste_multiplicidad':'holm',
                'comparaciones':[{'id':'general','x':'deficiencia_drenaje','y':'pci'}]}

    def test_synthetic_rejected_in_real_mode(self):
        with self.assertRaisesRegex(tesis.ProjectError,'campo_real'):
            tesis.validate_pairs(self.dataset())

    def test_duplicates_not_silently_removed(self):
        self.rows[1]['subtramo_id']=self.rows[0]['subtramo_id']
        with self.assertRaisesRegex(tesis.ProjectError,'duplicado'):
            tesis.validate_pairs(self.dataset(),False,False)

    def test_pci_boundaries(self):
        self.rows[0]['pci']='0';self.rows[1]['pci']='100'
        rows=tesis.validate_pairs(self.dataset(),False,False)
        self.assertEqual(rows[0]['pci'],0);self.assertEqual(rows[1]['pci'],100)

    def test_pci_out_of_range(self):
        self.rows[0]['pci']='101'
        with self.assertRaisesRegex(tesis.ProjectError,'fuera'):
            tesis.validate_pairs(self.dataset(),False,False)

    def test_nan_rejected(self):
        self.rows[0]['pci']='NaN'
        with self.assertRaisesRegex(tesis.ProjectError,'no finito'):
            tesis.validate_pairs(self.dataset(),False,False)

    def test_infinity_rejected(self):
        self.rows[0]['deficiencia_drenaje']='inf'
        with self.assertRaisesRegex(tesis.ProjectError,'no finito'):
            tesis.validate_pairs(self.dataset(),False,False)

    def test_bad_date_rejected(self):
        self.rows[0]['fecha']='2026-02-30'
        with self.assertRaisesRegex(tesis.ProjectError,'fecha inválida'):
            tesis.validate_pairs(self.dataset(),False,False)

    def test_zero_is_preserved(self):
        self.rows[0]['deficiencia_drenaje']='0'
        self.assertEqual(tesis.validate_pairs(self.dataset(),False,False)[0]['deficiencia_drenaje'],0)

    def test_missing_is_not_zero(self):
        self.rows[0]['deficiencia_drenaje']=''
        self.assertIsNone(tesis.validate_pairs(self.dataset(),False,False)[0]['deficiencia_drenaje'])

    def test_decimal_comma_requires_explicit_conversion(self):
        self.rows[0]['pci']='50,5'
        with self.assertRaisesRegex(tesis.ProjectError,'pci inválido'):
            tesis.validate_pairs(self.dataset(),False,False)

    def test_missing_evidence_rejected(self):
        for row in self.rows:row['procedencia']='campo_real'
        with self.assertRaisesRegex(tesis.ProjectError,'sin respaldo'):
            tesis.validate_pairs(self.dataset())

    def test_test_evidence_not_accepted_as_field_evidence(self):
        (self.root/'tests').mkdir();(self.root/'tests/fixture.txt').write_text('SOLO PRUEBA')
        for row in self.rows:
            row['procedencia']='campo_real';row['origen_pci']='tests/fixture.txt';row['origen_drenaje']='tests/fixture.txt'
        with self.assertRaisesRegex(tesis.ProjectError,'pruebas'):
            tesis.validate_pairs(self.dataset())

    def test_header_only_is_not_data(self):
        path=self.root/'vacio.csv';path.write_text(','.join(self.fields)+'\n')
        with self.assertRaisesRegex(tesis.ProjectError,'No hay observaciones'):
            tesis.validate_pairs(path)

    def test_bad_csv_width(self):
        path=self.root/'mal.csv';path.write_text('a,b\n1,2,3\n')
        with self.assertRaisesRegex(tesis.ProjectError,'más valores'):
            tesis.read_csv(path)

    def test_duplicate_headers_rejected(self):
        path=self.root/'mal.csv';path.write_text('a,a\n1,2\n')
        with self.assertRaisesRegex(tesis.ProjectError,'Columnas duplicadas'):
            tesis.read_csv(path)

    def test_spearman_known_negative_pattern(self):
        result=tesis.correlations(self.parsed(),self.plan())[0]
        self.assertAlmostEqual(result['coeficiente'],-1,places=12)
        self.assertEqual(result['n'],6)

    def test_pearson_known_linear_pattern(self):
        result=tesis.correlations(self.parsed(),self.plan('pearson'))[0]
        self.assertAlmostEqual(result['coeficiente'],-1,places=12)

    def test_constant_variable_rejected(self):
        rows=self.parsed()
        for row in rows:row['pci']=50
        with self.assertRaisesRegex(tesis.ProjectError,'constante'):
            tesis.correlations(rows,self.plan())

    def test_pair_exclusions_are_recorded(self):
        rows=self.parsed();rows[0]['pci']=None
        result=tesis.correlations(rows,self.plan())[0]
        self.assertEqual(result['n'],5)
        self.assertEqual(result['ids_excluidos_por_faltantes'],['PRUEBA01'])

    def test_too_few_computable_pairs_rejected(self):
        with self.assertRaisesRegex(tesis.ProjectError,'menos de tres'):
            tesis.correlations(self.parsed()[:2],self.plan())

    def test_holm_known_values(self):
        values=tesis.holm_adjust([0.01,0.04,0.03])
        for actual,expected in zip(values,[0.03,0.06,0.06]):
            self.assertAlmostEqual(actual,expected,places=12)

    def test_descriptions_track_missing(self):
        rows=self.parsed();rows[0]['pci']=None
        result=tesis.descriptions(rows)['variables']['pci']
        self.assertEqual(result['n'],5);self.assertEqual(result['faltantes'],1)

    def test_output_originals_protected(self):
        with self.assertRaisesRegex(tesis.ProjectError,'protegida'):
            tesis.output_path('datos/originales/alterar.txt')

    def test_output_traversal_rejected(self):
        with self.assertRaisesRegex(tesis.ProjectError,'dentro del proyecto'):
            tesis.output_path('../salida.txt')

    def test_evidence_traversal_rejected(self):
        with self.assertRaisesRegex(tesis.ProjectError,'sale del proyecto'):
            tesis.source_path('../fuente.txt')

    def test_existing_output_not_silently_overwritten(self):
        file=self.root/'resultado.json';file.write_text('original')
        with self.assertRaisesRegex(tesis.ProjectError,'ya existe'):
            tesis.output_path('resultado.json')
        self.assertEqual(file.read_text(),'original')

    def test_pending_plan_rejected(self):
        with self.assertRaisesRegex(tesis.ProjectError,'plan aprobado'):
            tesis.approved_plan(PROJECT/'config/plan_analisis.yaml')

    def test_declared_approval_requires_evidence(self):
        import yaml
        plan=tesis.yaml_load(PROJECT/'config/plan_analisis.yaml');plan['estado']='aprobado'
        file=self.root/'plan.yaml';file.write_text(yaml.safe_dump(plan))
        with self.assertRaisesRegex(tesis.ProjectError,'Falta un campo'):
            tesis.approved_plan(file)

    def test_field_period_must_match_project(self):
        (self.root/'config').mkdir()
        (self.root/'config/proyecto.yaml').write_text('periodo_estudio: 2026\n')
        for row in self.rows:row['procedencia']='campo_real'
        with self.assertRaisesRegex(tesis.ProjectError,'fuera del periodo'):
            tesis.validate_pairs(self.dataset(),require_evidence=False)

    def test_snapshot_does_not_alter_original(self):
        from contextlib import redirect_stdout
        from io import StringIO
        originals=self.root/'datos/originales';originals.mkdir(parents=True)
        raw=originals/'caso_sintetico.txt';raw.write_text('Evidencia ficticia solo para prueba de integridad.')
        before=tesis.digest(raw)
        with redirect_stdout(StringIO()):
            code=tesis.main(['snapshot-originals'])
        self.assertEqual(code,0)
        record=json.loads((self.root/'datos/manifest_originales.json').read_text())
        self.assertEqual(record['archivos'][0]['sha256'],before)
        self.assertEqual(tesis.digest(raw),before)

    def test_snapshot_empty_folder_is_rejected(self):
        from contextlib import redirect_stderr
        from io import StringIO
        with redirect_stderr(StringIO()):code=tesis.main(['snapshot-originals'])
        self.assertEqual(code,2)
        self.assertFalse((self.root/'datos/manifest_originales.json').exists())

    def test_truncated_render_png_is_rejected(self):
        path=self.root/'pagina.png'
        path.write_bytes(b'\x89PNG\r\n\x1a\n'+b'\x00\x00\x00\rIHDR'+b'incompleto')
        with self.assertRaisesRegex(tesis.ProjectError,'truncado'):
            tesis.validate_png(path)

    def test_invalid_render_png_is_rejected(self):
        path=self.root/'pagina.png';path.write_text('Esto no es una imagen')
        with self.assertRaisesRegex(tesis.ProjectError,'no válida'):
            tesis.validate_png(path)

class ProjectAndCLI(unittest.TestCase):
    def test_custom_agent_permissions_are_inherited(self):
        parse_toml=tesis.tomllib.loads
        def with_unsupported_override(text):
            profile=parse_toml(text)
            if profile.get('name')=='revisor_academico':
                profile['sandbox_mode']='read-only'
            return profile
        with patch.object(tesis.tomllib,'loads',side_effect=with_unsupported_override):
            report=tesis.verify_structure()
        self.assertFalse(report['ok'])
        self.assertTrue(any('sandbox_mode' in message and 'padre' in message for message in report['errores']))

    def test_actual_template_structure(self):
        report=tesis.verify_structure()
        self.assertTrue(report['ok'],report['errores'])
        self.assertTrue(report['avisos'])

    def test_final_export_blocked_for_initial_template(self):
        with self.assertRaisesRegex(tesis.ProjectError,'Entrega final bloqueada'):
            tesis.final_checks()

    def test_chapter_pending_markers_detected(self):
        report=tesis.audit_citations()
        self.assertGreater(len(report['pendientes']),0)
        self.assertEqual(report['errores'],[])

    def test_cli_verify(self):
        result=subprocess.run([sys.executable,str(PROJECT/'tools/tesis.py'),'verify'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertTrue(json.loads(result.stdout)['ok'])

    def test_cli_synthetic_analysis_rejected(self):
        result=subprocess.run([sys.executable,str(PROJECT/'tools/tesis.py'),'analyze','--input',str(PROJECT/'tests/fixtures/pares_sinteticos.csv'),'--output','tests/tmp/prohibido'],capture_output=True,text=True)
        self.assertEqual(result.returncode,2)
        self.assertIn('campo_real',result.stderr)
        self.assertFalse((PROJECT/'tests/tmp/prohibido').exists())

    def test_cli_empty_analysis_rejected(self):
        result=subprocess.run([sys.executable,str(PROJECT/'tools/tesis.py'),'validate-data','--input','datos/campo/pares_analisis.csv'],cwd=PROJECT,capture_output=True,text=True)
        self.assertEqual(result.returncode,2)
        self.assertIn('No hay observaciones',result.stderr)

    def test_cli_doctor_returns_capabilities(self):
        result=subprocess.run([sys.executable,str(PROJECT/'tools/tesis.py'),'doctor'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        report=json.loads(result.stdout)
        self.assertIn('codex',report['herramientas']);self.assertIn('pandoc',report['herramientas'])

if __name__=='__main__':
    unittest.main()
