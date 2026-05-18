# Imágenes para react-pdf-indice

Las figuras de los `.md` referencian `images/placeholder-fig-N.png`.

## Estado actual

Mapeo por capítulo (solo imágenes embebidas de la página indicada):

| Archivo | Capítulo | Página PDF |
|---------|----------|------------|
| placeholder-fig-1.png, placeholder-fig-2.png | 3. Composición | 7, 8 |
| placeholder-fig-6.png | 5. Virtual DOM | 13 |
| placeholder-fig-3.png, placeholder-fig-4.png, placeholder-fig-5.png | 6. React vs jQuery | 14, 15 |

## Cómo obtener más figuras (recorte correcto)

Las figuras del manual suelen estar en el PDF como **objetos de imagen**; así se obtienen sin texto:

1. Ver en el PDF en qué página está la figura y anotar el número de página (del PDF; si usas el índice del libro, suma 4).
2. Listar imágenes: `pdfimages -list documentacion-reactjs.pdf` (columna `page`).
3. Extraer: `pdfimages -f PAG -l PAG documentacion-reactjs.pdf prefix` (en una carpeta temporal).
4. Convertir los `.ppm` a PNG (p. ej. con ImageMagick: `convert prefix-XXX.ppm prefix-XXX.png`) y copiar el que corresponda a `images/placeholder-fig-N.png`.

## Añadir más figuras

1. Obtener la imagen (extracción del PDF, screenshot, o desde `../react-tsx/images/`).
2. Guardarla aquí como `placeholder-fig-N.png` (N = número de figura en el texto).
3. Los `.md` ya enlazan con `![Figura N — Título](images/placeholder-fig-N.png)`; no hace falta cambiar los archivos.

Para automatizar con un mapeo (figura → archivo origen), usar el script `interpolar_imagenes.py` en la carpeta padre.
