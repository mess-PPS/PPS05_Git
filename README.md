# Proyecto Unidad1

## Descripción del proyecto

Este proyecto ha sido desarrollado en Python y permite obtener la cadena más larga dentro de una lista de palabras introducidas por el usuario. En caso de existir varias palabras con la misma longitud, el programa devuelve la primera según el orden alfabético, ignorando diferencias entre mayúsculas, minúsculas y caracteres acentuados.

Además del programa principal, el proyecto incluye pruebas automatizadas desarrolladas con unittest para comprobar distintos casos de funcionamiento y validar el comportamiento del código.

## Tecnologías utilizadas

- Python 3.14
- Librería estándar unittest
- Visual Studio Code
- Git 2.54.0
  
## Guía de despliegue

Para ejecutar el proyecto, primero es necesario disponer de Python instalado en el sistema. Una vez descargados los archivos del repositorio, se puede abrir una terminal dentro de la carpeta del proyecto y ejecutar el programa principal mediante:

```bash
python mychar.py
```

El programa solicitará la introducción de cinco palabras y mostrará posteriormente cuál es la cadena más larga según los criterios definidos en el código.

Para ejecutar las pruebas automatizadas incluidas en el proyecto, se puede utilizar el siguiente comando:

```bash
python -m unittest test_mychar.py
```

## Tabla de trazabilidad

| Fecha | Versión | Descripción |
|---|---|---|
| 15/05/2026 | v1.0 | Creación inicial del repositorio Git y subida del proyecto Unidad1 |
| 15/05/2026 | v1.1 | Creación de la rama desarrollo-seguro y modificación de mychar.py |
| 15/05/2026 | v1.2 | Creación del fichero README.md y documentación inicial del proyecto |

## Checklist de seguridad

Durante la configuración inicial del repositorio se ha decidido proteger e ignorar determinados archivos y carpetas para evitar la exposición accidental de información innecesaria o sensible.

- `*.log` para impedir la subida de archivos de registro y depuración.
- `__pycache__/` para evitar incluir archivos temporales generados automáticamente por Python.
- `.venv/` y `env/` para no subir entornos virtuales locales al repositorio.
- `*.sqlite3` para impedir la subida de posibles bases de datos locales o temporales.
- `secrets.env` para evitar fugas de credenciales o claves sensibles utilizadas en pruebas de seguridad.