from io import BytesIO

import pandas as pd
from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Visor de Excel")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "table_html": None,
            "filename": None,
            "error": None,
        },
    )


@app.post("/upload", response_class=HTMLResponse)
async def upload_excel(request: Request, file: UploadFile = File(...)) -> HTMLResponse:
    if not file.filename.lower().endswith(".xlsx"):
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "table_html": None,
                "filename": None,
                "error": "Solo se permiten archivos con extensión .xlsx",
            },
            status_code=400,
        )

    contents = await file.read()

    try:
        dataframe = pd.read_excel(BytesIO(contents))
    except Exception:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "table_html": None,
                "filename": None,
                "error": "No se pudo leer el archivo Excel. Verifica que sea válido.",
            },
            status_code=400,
        )

    table_html = dataframe.to_html(
        classes="data-table",
        index=False,
        border=0,
        na_rep="",
    )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "table_html": table_html,
            "filename": file.filename,
            "error": None,
        },
    )
