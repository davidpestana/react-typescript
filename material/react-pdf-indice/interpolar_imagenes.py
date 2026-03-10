#!/usr/bin/env python3
"""
Interpola imágenes en los .md de react-pdf-indice.

Copia o enlaza archivos desde un mapeo (figura N → ruta origen) a
material/react-pdf-indice/images/placeholder-fig-N.png, para que los
enlaces existentes en los .md funcionen.

Uso:
  python3 interpolar_imagenes.py

El mapeo FIGURA_ORIGEN se puede editar en este script para añadir
nuevas figuras (p. ej. desde material/react-tsx/images/ o desde
imágenes extraídas del PDF).
"""
from pathlib import Path

INDICE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = INDICE_DIR / "images"
REACT_TSX_IMAGES = (INDICE_DIR / ".." / "react-tsx" / "images").resolve()

# Mapeo: número de figura → ruta del archivo origen (relativa a este script o absoluta).
# fig-1 y fig-2 ya están rellenadas con imágenes extraídas del PDF (pdfimages -f 7 -l 10).
# Para nuevas figuras: extraer del PDF, convertir a PNG, añadir aquí y ejecutar el script.
FIGURA_ORIGEN = {
    # 1, 2: ya en images/ (extraídas del PDF cap. 3)
    # 3: Path("/ruta/a/fig-003.png"),
}


def main():
    IMAGES_DIR.mkdir(exist_ok=True)
    for num, origen in FIGURA_ORIGEN.items():
        origen = Path(origen)
        if not origen.is_absolute():
            origen = INDICE_DIR / origen
        if not origen.exists():
            print(f"  AVISO: no existe {origen} para figura {num}")
            continue
        dest = IMAGES_DIR / f"placeholder-fig-{num}.png"
        if dest.exists() and dest.resolve().samefile(origen.resolve()):
            continue
        import shutil
        shutil.copy2(origen, dest)
        print(f"  {dest.name} <- {origen.name}")
    print("Hecho. Revisa material/react-pdf-indice/images/")


if __name__ == "__main__":
    main()
