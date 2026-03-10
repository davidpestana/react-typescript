#!/usr/bin/env python3
"""
Extrae el texto del PDF de React (Pronoide) por punto del índice.
Un archivo .md por sección, con cabecera que indica rango de páginas PDF.
Uso: python3 extraer_texto.py
"""
import csv
import subprocess
import os
from pathlib import Path

PDF = Path(__file__).resolve().parent.parent.parent / "documentacion-reactjs.pdf"
OUT_DIR = Path(__file__).resolve().parent
CSV_PATH = Path(__file__).resolve().parent / "indice-paginas.csv"
TOTAL_PAGES = 242
# El índice del PDF usa la numeración del libro (1, 2, 3, 7, 9, 10…).
# Las primeras páginas del PDF son portada + índice, así que página libro N = PDF página N+4.
PDF_OFFSET = 4


def section_to_sort_key(section_id: str):
    """Convierte '7.1' en (7, 1), '28.2.1' en (28, 2, 1) para ordenar."""
    parts = section_id.replace(",", ".").split(".")
    return tuple(int(p) for p in parts if p.isdigit() or (p.strip() and p.strip().isdigit()))


def section_to_filename_prefix(section_id: str) -> str:
    """7.1 -> 07-01, 28.2.1 -> 28-02-01, 1 -> 01."""
    parts = section_id.replace(",", ".").split(".")
    num_parts = [p.strip() for p in parts if p.strip().replace("-", "").isdigit()]
    if not num_parts:
        return section_id.replace(".", "-")
    # Primer número con cero a la izquierda si es un solo dígito
    first = num_parts[0]
    if len(first) == 1:
        first = first.zfill(2)
    rest = [p.zfill(2) if len(p) <= 2 else p for p in num_parts[1:]]
    return "-".join([first] + rest)


def main():
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # Ordenar por (start_page, section_key)
    for r in rows:
        r["start_page"] = int(r["start_page"])
        r["_key"] = (r["start_page"], section_to_sort_key(str(r["section_id"])))
    rows.sort(key=lambda r: r["_key"])
    # Calcular end_page
    for i, r in enumerate(rows):
        if i + 1 < len(rows):
            r["end_page"] = rows[i + 1]["start_page"] - 1
        else:
            r["end_page"] = TOTAL_PAGES
        if r["end_page"] < r["start_page"]:
            r["end_page"] = r["start_page"]
    # Extraer texto por cada sección
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for r in rows:
        sid = str(r["section_id"]).strip()
        slug = r["title_slug"].strip()
        start = r["start_page"] + PDF_OFFSET
        end = min(r["end_page"] + PDF_OFFSET, TOTAL_PAGES)
        prefix = section_to_filename_prefix(sid)
        fname = f"{prefix}-{slug}.md"
        out_path = OUT_DIR / fname
        try:
            result = subprocess.run(
                ["pdftotext", "-layout", "-f", str(start), "-l", str(end), str(PDF), "-"],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(OUT_DIR),
            )
            text = result.stdout or ""
            if result.returncode != 0:
                text = f"<!-- Error pdftotext: {result.stderr} -->\n\n" + text
        except Exception as e:
            text = f"<!-- Error: {e} -->\n\n"
        title_heading = sid.replace(",", ".")
        header = f"# {title_heading}. {slug.replace('-', ' ').title()}\n\n"
        header += f"**PDF: páginas {start}–{end}** (libro: {r['start_page']}–{r['end_page']})\n\n---\n\n"
        content = header + text
        out_path.write_text(content, encoding="utf-8")
        print(f"  {fname}  (p. {start}-{end})")
    # Escribir CSV con rangos para segunda pasada (imágenes)
    completo_path = OUT_DIR / "indice-paginas-completo.csv"
    with open(completo_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["section_id", "title_slug", "libro_start", "libro_end", "pdf_start", "pdf_end", "archivo"])
        for r in rows:
            sid = str(r["section_id"]).strip()
            prefix = section_to_filename_prefix(sid)
            fname = f"{prefix}-{r['title_slug'].strip()}.md"
            pdf_start = r["start_page"] + PDF_OFFSET
        pdf_end = min(r["end_page"] + PDF_OFFSET, TOTAL_PAGES)
        w.writerow([sid, r["title_slug"], r["start_page"], r["end_page"], pdf_start, pdf_end, fname])
    print(f"\nHecho: {len(rows)} archivos en {OUT_DIR}")
    print(f"Mapa completo: {completo_path}")


if __name__ == "__main__":
    main()
