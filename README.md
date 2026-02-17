# Aplicación local: visor de Excel con FastAPI

Esta aplicación permite:
- Subir un archivo Excel `.xlsx`.
- Leer su contenido (hoja activa).
- Mostrarlo en una tabla HTML simple y limpia en el navegador.

## 1) Requisitos previos
- Python 3.10+ instalado.
- Terminal (PowerShell, CMD, bash o similar).

## 2) Crear y activar entorno virtual
En la carpeta del proyecto:

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3) Instalar dependencias
```bash
pip install -r requirements.txt
```

## 4) Ejecutar la app
```bash
uvicorn main:app --reload
```

## 5) Abrir en el navegador
Ir a:

- http://127.0.0.1:8000

## 6) Usar la aplicación
1. Clic en **"Seleccionar archivo"**.
2. Elige un archivo `.xlsx`.
3. Clic en **"Subir y mostrar"**.
4. Verás los datos en una tabla.

## Notas
- Solo acepta archivos `.xlsx`.
- Se muestra la **hoja activa** del archivo Excel.
- La primera fila se toma como encabezado de la tabla.
