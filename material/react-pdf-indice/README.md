# Texto completo del PDF React (Pronoide) por punto del índice

Todo el texto del **documentacion-reactjs.pdf** extraído y dividido en **un archivo por punto del índice** (103 archivos). Cada archivo corresponde a una sección o subsección del índice del PDF y indica **qué páginas del PDF** cubre.

## Origen

- **PDF**: `documentacion-reactjs.pdf` (raíz del repo).
- **Índice usado**: el "Contenidos" del propio PDF (1. ¿Qué es React? … hasta 31.12. Lab: React Router).
- **Herramienta**: `pdftotext` (poppler) por rangos de páginas.

## Estructura

Cada archivo `.md` tiene:

1. **Título** de la sección (p. ej. `# 4. Modelo Declarativo`).
2. **Rango de páginas**: `**PDF: páginas X–Y**` (para poder extraer imágenes en una segunda pasada).
3. **Texto** extraído de esas páginas del PDF (sin reescribir).

Nombre de archivo: `NN-titulo-slug.md` (p. ej. `07-01-lab-create-react-app.md` para la sección 7.1).

## Mapas de páginas

| Archivo | Descripción |
|---------|-------------|
| **indice-paginas.csv** | Listado del índice con `section_id`, `title_slug`, `start_page` (solo página inicial). |
| **indice-paginas-completo.csv** | Mismo índice con **start_page**, **end_page** y nombre de **archivo**; sirve para la segunda pasada de imágenes. |

Columnas de `indice-paginas-completo.csv`:

- `section_id` — Número de sección (1, 7.1, 28.2.1, …).
- `title_slug` — Slug del título.
- `start_page` — Primera página en el PDF.
- `end_page` — Última página en el PDF.
- `archivo` — Nombre del `.md` generado.

## Cómo regenerar el texto

Desde esta carpeta:

```bash
python3 extraer_texto.py
```

Requisitos: Python 3, `pdftotext` (paquete `poppler-utils` en Linux). El PDF debe estar en la raíz del repositorio.

## Segunda pasada (imágenes)

Con `indice-paginas-completo.csv` puedes:

- Saber exactamente **de qué página a qué página** va cada punto del índice.
- Extraer o renderizar imágenes solo de ese rango (p. ej. con `pdftoppm -f N -l M` o recortes) e interpolarlas en el `.md` correspondiente.

## Resumen

| Concepto | Valor |
|----------|--------|
| Archivos generados | 103 |
| Páginas PDF totales | 242 |
| Índice | 1 → 31.12 (incluye Labs y subsecciones) |
