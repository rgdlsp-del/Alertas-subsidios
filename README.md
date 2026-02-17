# Visor local de archivos Excel con FastAPI

Aplicación web simple para ejecutar en tu computadora local. Permite subir un archivo `.xlsx`, leerlo y mostrar su contenido en una tabla HTML.

## Requisitos

- Python 3.9 o superior
- pip

## Instalación y ejecución (paso a paso)

1. **Entrar al proyecto**

   ```bash
   cd /workspace/Alertas-subsidios
   ```

2. **Crear entorno virtual (recomendado)**

   ```bash
   python3 -m venv .venv
   ```

3. **Activar entorno virtual**

   - Linux/macOS:

     ```bash
     source .venv/bin/activate
     ```

   - Windows (PowerShell):

     ```powershell
     .venv\Scripts\Activate.ps1
     ```

4. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

5. **Iniciar servidor local**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Abrir en navegador**

   Ve a: [http://127.0.0.1:8000](http://127.0.0.1:8000)

7. **Usar la app**

   - Haz clic en el selector de archivo.
   - Elige un `.xlsx`.
   - Pulsa **Subir y mostrar**.
   - Verás el contenido en forma de tabla.

## Estructura

- `app/main.py`: endpoints FastAPI y lógica de lectura del Excel.
- `templates/index.html`: interfaz y render del resultado.
- `static/style.css`: estilos simples y limpios.
- `requirements.txt`: dependencias.

## Nota

La aplicación lee la primera hoja del archivo Excel por defecto (comportamiento estándar de `pandas.read_excel`).
