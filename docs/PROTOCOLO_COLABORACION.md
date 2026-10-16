# Protocolo de colaboración de especialistas

## Orquestación
El hilo principal coordina. Los subagentes producen propuestas y revisiones acotadas. La colaboración se hace pasando explícitamente resultados y observaciones por el coordinador; no se presupone un chat autónomo entre pares ni una integración automática de sus archivos.

## Preparar cada encargo
Crea un contexto desde `plantillas/ENCARGO_AGENTE.md` en `coordinacion/contextos/`. Indica pregunta, fase, fuentes con estado y hashes, decisiones vigentes, entregable, dependencias y carpeta permitida. Un encargo sin entradas suficientes debe pedir la evidencia precisa y devolver el resto del trabajo útil.
Registra la tarea en `coordinacion/tareas.csv`. Estados permitidos: propuesta, en_curso, esperando_dependencia, revision, terminada, bloqueada. `terminada` exige que el coordinador lea el entregable y confirme su criterio de aceptación; no basta un mensaje del agente.

## Rondas para el diseño inicial
1. Bibliografía, drenaje y pavimentos revisan de manera independiente el mismo alcance. La bibliografía entrega fuentes comprobadas; drenaje y pavimentos producen observaciones técnicas, sin inventar información del tramo.
2. El coordinador integra las propuestas. Metodología examina su consistencia y estadística revisa muestreo, emparejamiento, escala y dependencia. Ambos reciben el expediente técnico; no comienzan la inferencia antes de cerrar sus dependencias.
3. Devuelve observaciones a sus autores. Drenaje corrige su ficha; pavimentos corrige unidades y registro PCI; metodología actualiza la matriz; estadística actualiza el plan.
4. Revisión académica audita una versión consolidada. El coordinador incorpora únicamente cambios sustentados y deja pendientes identificados para el asesor.

## Resultado obligatorio de cada agente
Utiliza `plantillas/INFORME_AGENTE.md`: objetivo respondido, evidencia y ubicación, hallazgos, propuesta, supuestos, limitaciones, archivos, comandos, prueba y preguntas concretas para otros perfiles. Cada observación declara severidad: bloqueante, mayor o menor; explica el efecto real y cómo resolverlo.

## Conflictos y revisiones
Registra desacuerdos en `coordinacion/desacuerdos.csv`. Indica ambas propuestas, evidencias y decisión pendiente. No decidas por mayoría de agentes. Solicita el documento, cálculo o criterio que resuelva el punto. Si requiere criterio académico del asesor, registra la pregunta y continúa en aspectos independientes. Realiza hasta dos rondas de corrección sobre el mismo punto; después informa el bloqueo con sus alternativas. Esto limita bucles, no obliga a aceptar una solución incompleta.

## Archivos y concurrencia
Los subagentes no editan simultáneamente registros, estado o capítulos compartidos. Cada uno usa su carpeta asignada. El coordinador compara propuestas, verifica fuentes y aplica el cambio al archivo canónico. Si un agente es de solo lectura, su salida se persiste por el coordinador. Todos los subagentes heredan el sandbox y los permisos de la sesión principal. Las restricciones de carpeta y lectura son instrucciones operativas, no sandboxes separados; el coordinador debe comprobar el cumplimiento y los permisos efectivos.

## Revisión de resultados
Estadística produce resultados desde los datos congelados y el plan aprobado. Drenaje y pavimentos revisan su interpretación física; metodología comprueba que responden preguntas; bibliografía aporta comparación con antecedentes; revisión académica detecta sobreinterpretación y citas insuficientes. El coordinador redacta discusión y conclusiones y devuelve el texto a revisión.

## Continuidad
Cada ronda tiene ID, entradas, salidas, hashes, decisiones y pendientes. Los hallazgos heredados se vuelven a contrastar si cambian datos, instrumentos o método. Una fuente descargada no se vuelve a buscar sin una razón; una fuente reemplazada debe conservar su versión previa y actualizar su trazabilidad.
