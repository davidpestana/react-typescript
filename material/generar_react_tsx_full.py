#!/usr/bin/env python3
"""
Genera material/react-tsx-full a partir de react-pdf-indice:
- Contenido completo (sin resumir), mismo texto y bloques de código.
- Navegación anterior/siguiente en cada archivo.
- README con índice de todos los puntos.
- Carpeta images/ copiada para que las figuras funcionen.

El código en los bloques se mantiene como en el original (JSX/JS del manual);
la conversión explícita a TSX se puede hacer después como paso aparte.

Al generar, se adapta el texto y las rutas a TSX: JSX→TSX en la prosa,
.jsx→.tsx en rutas de archivo, y títulos como "Qué es TSX".
"""
import re
import shutil
from pathlib import Path

INDICE = Path(__file__).resolve().parent / "react-pdf-indice"
FULL = Path(__file__).resolve().parent / "react-tsx-full"


def adapt_jsx_to_tsx(content: str) -> str:
    """Adapta prosa y rutas de JSX a TSX; mantiene nombres de API (ej. jsx-runtime)."""
    # Rutas de archivo: .jsx → .tsx
    content = re.sub(r"(\*\*Archivo:\*\*[^\n]*?)\.jsx\b", r"\1.tsx", content)
    content = re.sub(r"(`[^`]*?)\.jsx\b", r"\1.tsx", content)
    # Prosa: JSX / Jsx / JXS → TSX (luego restauramos jsx-runtime)
    content = content.replace("JSX", "TSX").replace("JXS", "TSX").replace("Jsx", "TSX")
    content = content.replace("tsx-runtime", "jsx-runtime")  # módulo real de React
    # Frases concretas donde "JS" = JavaScript (lenguaje de salida)
    content = re.sub(r"\b(a JS)\b", r"a JavaScript", content, flags=re.IGNORECASE)
    content = re.sub(r"código de TSX a JS\b", "código de TSX a JavaScript", content)
    content = re.sub(r"código TSX a JS\b", "código TSX a JavaScript", content)
    content = re.sub(r"transforma el código TSX a JS\b", "transforma el código TSX a JavaScript", content)
    content = re.sub(r"\ben JS completamente\b", "en JavaScript completamente", content)
    content = re.sub(r"\ben JS\b", "en JavaScript", content)  # p. ej. "incrustado en JS"
    content = re.sub(r"\bcon JS en lugar de TSX\b", "con JavaScript en lugar de TSX", content)
    # Títulos de capítulo (normalizar mayúsculas)
    content = re.sub(r"# 9\. Que Es TSX\b", "# 9. Qué es TSX", content)
    content = re.sub(r"# 10\. Componente Sin TSX\b", "# 10. Componente sin TSX", content)
    content = re.sub(r"9\. Que Es TSX\b", "9. Qué es TSX", content)
    content = re.sub(r"10\. Componente Sin TSX\b", "10. Componente sin TSX", content)
    return content


def get_sorted_md_files():
    """Lista de .md en react-pdf-indice (orden natural), sin README."""
    files = sorted(INDICE.glob("*.md"), key=lambda p: (p.name != "README.md", p.name))
    return [f for f in files if f.name != "README.md"]


def extract_title(content: str) -> str:
    """Primera línea # como título para la navegación."""
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    return ""


def add_navigation(content: str, prev_file: str | None, prev_title: str, next_file: str | None, next_title: str) -> str:
    """Inserta línea de navegación después del primer ---."""
    parts = content.split("---", 2)
    if len(parts) < 2:
        return content
    header = parts[0].strip()
    body = (parts[2] if len(parts) > 2 else parts[1]).strip()
    nav_parts = ["[← Índice](README.md)"]
    if prev_file:
        nav_parts.append(f"[← Anterior: {prev_title}]({prev_file})")
    if next_file:
        nav_parts.append(f"[Siguiente: {next_title} →]({next_file})")
    nav_line = " | ".join(nav_parts)
    return header + "\n\n---\n\n" + nav_line + "\n\n---\n\n" + body


def main():
    FULL.mkdir(exist_ok=True)
    if (INDICE / "images").exists():
        dest_images = FULL / "images"
        if dest_images.exists():
            shutil.rmtree(dest_images)
        shutil.copytree(INDICE / "images", dest_images)
        print("  Copiada carpeta images/")

    files = get_sorted_md_files()
    titles = {}
    for path in files:
        content = adapt_jsx_to_tsx(path.read_text(encoding="utf-8"))
        titles[path.name] = extract_title(content)

    for i, path in enumerate(files):
        content = adapt_jsx_to_tsx(path.read_text(encoding="utf-8"))
        prev_file = files[i - 1].name if i > 0 else None
        prev_title = titles.get(prev_file, "") if prev_file else ""
        next_file = files[i + 1].name if i + 1 < len(files) else None
        next_title = titles.get(next_file, "") if next_file else ""
        new_content = add_navigation(content, prev_file, prev_title, next_file, next_title)
        (FULL / path.name).write_text(new_content, encoding="utf-8")
        print(f"  {path.name}")

    # README con índice
    readme_lines = [
        "# React con TypeScript — Contenido completo (manual)",
        "",
        "Manual en Markdown con **105 capítulos**: desde qué es React hasta React Router, pasando por Hooks, Redux y TypeScript/TSX. Cada archivo tiene navegación anterior/siguiente.",
        "",
        "## Cómo seguir el curso",
        "",
        "1. **Haz un fork** de este repositorio en tu cuenta de GitHub.",
        "2. Abre tu fork en **GitHub Codespaces** (botón *Code* → *Codespaces* → *Create codespace on main*).",
        "3. En el Codespace tendrás Node, el editor y las extensiones recomendadas; los detalles están en [Requisitos](02-00-requisitos.md).",
        "4. Sigue el [Índice](#índice) en orden. Para practicar, crea proyectos con Vite (cap. 7.5) o desde cero (cap. 8.1).",
        "",
        "## Índice",
        "",
    ]
    for path in files:
        title = titles.get(path.name, path.stem)
        readme_lines.append(f"- [{title}]({path.name})")
    readme_lines.append("")
    (FULL / "README.md").write_text("\n".join(readme_lines), encoding="utf-8")
    print("  README.md (índice)")

    print(f"\nHecho: {len(files)} archivos en {FULL}")


if __name__ == "__main__":
    main()
