#!/usr/bin/env python3
"""
Formatea los .md extraídos del PDF:
- Quita pies de página (números sueltos, líneas TOC).
- Convierte "Chapter X. Title" en ##.
- Detecta bloques de código y los envuelve en ```tsx.
- Normaliza líneas en blanco.
- Prepara "Figure N." como placeholder para imágenes.
"""
import re
from pathlib import Path

INDICE_DIR = Path(__file__).resolve().parent


def is_toc_line(line: str) -> bool:
    """Línea que es entrada del índice (X.Y. Título . . . . . . . . . . . . . . . N)."""
    stripped = line.strip()
    if not stripped:
        return False
    # Patrón: "20.4. shouldComponentUpdate . . . . . . . . . . . . . . . . . . . 84"
    if re.match(r"^\d+(\.\d+)*\.\s+.+\.\s*\.\s*\.\s*\.\s*\.\s*\d+\s*$", stripped):
        return True
    if re.match(r"^\d+(\.\d+)*\.\s+.+\s{2,}\d+\s*$", stripped) and " . . " in line:
        return True
    # Línea que termina en muchos puntos y un número
    if re.search(r"\.\s*\.\s*\.\s*\.\s*\.\s*\d+\s*$", stripped):
        return True
    return False


def is_page_number_line(line: str) -> bool:
    """Línea que es solo un número (pie de página)."""
    stripped = line.strip()
    if not stripped:
        return False
    # Solo dígitos, posiblemente con espacios delante (alineado a la derecha)
    if re.match(r"^\d+\s*$", stripped):
        return True
    # Línea que son casi solo espacios y un número al final
    if re.match(r"^\s+\d+\s*$", line) and len(line.strip()) <= 4:
        return True
    return False


def is_orphan_brace(line: str) -> bool:
    """Línea que es solo una llave suelta (fragmento del PDF)."""
    s = line.strip()
    return s in ("}", "{", "});", "},", "};", ")", ");")


def is_code_line(line: str) -> bool:
    """Heurística: línea que parece código (indentada o continuación de código)."""
    s = line.strip()
    if not s or s.startswith("#"):
        return False
    # Llaves y cierres sueltos → siempre código (evita } huérfanos en el texto)
    if is_orphan_brace(line):
        return True
    # Línea que es solo una cadena entre comillas (continuación de createElement, etc.)
    if re.match(r"^['\"].*['\"]\s*,?\s*$", s):
        return True
    # Líneas muy cortas que son claramente código: ), ),  , etc.
    if re.match(r"^[)\]\},;\s]+$", s) or s in ("),", "},", ");", ");"):
        return True
    # Patrones de código (comprobar antes que la indentación; el PDF a veces no indenta)
    code_starts = (
        "import ", "const ", "var ", "let ", "return ", "return(", "function ", "class ",
        "export ", "from ", "React.", "createElement", "createRoot", "render(",
        "<", "  </", "  <", ");", "});", "},", "  }", "  {", "$ ", "  * ",
        "npm ", "  • ", "  - ", "  ◦ ", "if (", "for (", "switch (", "case ",
        "=>", "null)", "true", "false", "module.", "path.",
        "type ", "interface ", "useState", "useEffect", "useContext",
    )
    if any(s.startswith(p) or p in s for p in code_starts):
        return True
    # Debe tener indentación (2+ espacios) para el resto, o ser continuación
    has_indent = line.startswith("  ") or line.startswith("\t")
    if not has_indent and len(s) > 3:
        return False
    # Línea que termina en ; o ) o } o contiene =
    if re.search(r"[;{}()=>\[\]</>]$", s) or ("=" in s and "==" not in s[:3]):
        return True
    # Rutas tipo /path/to/file (las tratamos como referencia de archivo, no como código)
    if is_file_path_line(line):
        return False
    if s.startswith("/") and ("." in s or "/" in s):
        return True
    # Propiedades de objeto (key: value) con indentación
    if has_indent and re.search(r"^\s*\w+\s*:\s*", line):
        return True
    return False


def is_bullet_line(line: str) -> bool:
    """Línea que es viñeta ( • o - ) y no código."""
    s = line.strip()
    if s.startswith("•") or (s.startswith("-") and len(s) > 2 and not s.startswith("--")):
        return True
    return False


def is_file_path_line(line: str) -> bool:
    """Línea que es solo una ruta de archivo (ej. /proyecto/src/Component.jsx)."""
    s = line.strip()
    if not s or " " in s:
        return False
    return bool(re.match(r"^/[a-zA-Z0-9/_.-]+\.(jsx?|tsx?|css|json|html?)$", s))


# Caracteres típicos de artefactos PDF (símbolos, marcas de referencia, etc.)
PDF_ARTIFACTS = re.compile(r"[\uf05a\uf0b7\u200b\u200c\u200d\ufeff\u00ad]|\s{3,}")


def clean_text_line(line: str) -> str:
    """Limpia una línea de texto: espacios excesivos y artefactos PDF."""
    s = line.strip()
    s = PDF_ARTIFACTS.sub(" ", s)
    return " ".join(s.split())


def process_body(body: str) -> str:
    lines = body.split("\n")
    out = []
    i = 0
    in_code = False
    code_buffer = []
    code_lang = "tsx"

    def flush_code():
        nonlocal code_buffer, code_lang
        if code_buffer:
            # Dedentar: quitar la indentación común mínima (no dejar código mal indentado)
            lines = [l.rstrip() for l in code_buffer if l.strip() or l == ""]
            if not any(l.strip() for l in lines):
                code_buffer = []
                return
            min_indent = min(
                (len(l) - len(l.lstrip()) for l in lines if l.strip()),
                default=0
            )
            code_text = "\n".join(
                l[min_indent:] if len(l) > min_indent else l
                for l in lines
            ).rstrip()
            # Si el bloque es solo una llave de cierre, añadirla al último bloque de código
            if code_text.strip() in ("}", "});", "},", "};", ")"):
                for j in range(len(out) - 1, -1, -1):
                    if out[j] == "```":
                        # Insertar antes del cierre: después del último ```tsx y su contenido
                        k = j - 1
                        while k >= 0 and out[k] != "```":
                            k -= 1
                        if k >= 0 and "tsx" in out[k]:
                            out[j - 1] = out[j - 1] + "\n" + code_text.strip()
                        break
                code_buffer = []
                return
            if code_text.strip() == "{":
                code_buffer = []
                return
            if code_text:
                out.append("```" + code_lang)
                out.append(code_text)
                out.append("```")
                out.append("")
            code_buffer = []
        code_lang = "tsx"

    while i < len(lines):
        line = lines[i]
        raw = line

        # Quitar form feed
        line = line.replace("\f", "")

        # Saltar líneas TOC
        if is_toc_line(line):
            i += 1
            continue

        # Saltar pies de página (solo número)
        if is_page_number_line(line):
            i += 1
            continue

        # Línea que es solo espacios + número (alineado derecha)
        if re.match(r"^\s{20,}\d+\s*$", line):
            i += 1
            continue

        # Ruta de archivo sola → **Archivo:** `ruta`
        if is_file_path_line(line):
            flush_code()
            path = line.strip()
            out.append("")
            out.append("**Archivo:** `" + path + "`")
            out.append("")
            i += 1
            continue

        # Chapter X. Title → ##
        if re.match(r"^Chapter\s+\d+(\.\d+)*\.\s+", line, re.IGNORECASE):
            flush_code()
            title = re.sub(r"^Chapter\s+\d+(\.\d+)*\.\s+", "", line, flags=re.IGNORECASE).strip()
            out.append("")
            out.append("## " + title)
            out.append("")
            i += 1
            continue

        # N.N. Título (sin puntos al final como en el índice) → ###
        if re.match(r"^\d+(\.\d+)*\.\s+\S+", line.strip()) and not is_toc_line(line):
            flush_code()
            out.append("")
            out.append("### " + line.strip())
            out.append("")
            i += 1
            continue

        # Figure N. Title → placeholder para imagen
        if re.match(r"^Figure\s+\d+\.\s+", line, re.IGNORECASE):
            flush_code()
            title = re.sub(r"^Figure\s+\d+\.\s+", "", line, flags=re.IGNORECASE).strip()
            num = re.search(r"^Figure\s+(\d+)\.", line, re.IGNORECASE)
            num = num.group(1) if num else ""
            out.append("")
            out.append(f"**Figura {num} — {title}**")
            out.append("")
            out.append(f"![Figura {num} — {title}](images/placeholder-fig-{num}.png)")
            out.append("")
            i += 1
            continue

        # Viñetas: normalizar a -
        if is_bullet_line(line) and not in_code:
            flush_code()
            s = line.strip().lstrip("•").strip().lstrip("-").strip()
            if s:
                out.append("- " + s)
            i += 1
            continue

        # ¿Código?
        if is_code_line(line):
            if not in_code:
                flush_code()
                in_code = True
            # Mantener la línea con su indentación para dedentar después
            code_buffer.append(line)
            i += 1
            continue
        else:
            if in_code:
                in_code = False
                flush_code()

        # No sacar llaves sueltas como texto (fragmentos del PDF)
        if is_orphan_brace(line):
            i += 1
            continue

        # Ignorar delimitadores de bloques de código (evitar duplicar al re-formatear)
        if line.strip() in ("```", "```tsx", "```js", "```javascript", "```css"):
            i += 1
            continue

        # Normalizar: no más de una línea en blanco
        if not line.strip():
            if out and out[-1].strip() != "":
                out.append("")
            i += 1
            continue

        out.append(clean_text_line(line))
        i += 1

    flush_code()
    return "\n".join(out)


def merge_consecutive_code_blocks(text: str) -> str:
    """Une bloques ```tsx (o ```js, etc.) consecutivos separados solo por líneas en blanco."""
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Apertura de bloque (```tsx, ```js, etc.)
        if stripped.startswith("```") and stripped != "```":
            fence = stripped
            out.append(line)
            i += 1
            all_content = []
            while True:
                while i < len(lines) and lines[i].strip() != "```":
                    all_content.append(lines[i])
                    i += 1
                if i >= len(lines):
                    break
                i += 1  # consumir ```
                while i < len(lines) and not lines[i].strip():
                    i += 1
                if i < len(lines) and lines[i].strip() == fence:
                    all_content.append("")
                    i += 1  # consumir siguiente ```tsx
                else:
                    break
            out.extend(all_content)
            out.append("```")
        else:
            out.append(line)
            i += 1
    return "\n".join(out)


def is_fragment_code_block(lines: list) -> bool:
    """True si el bloque son solo cierres/export (fragmento del PDF)."""
    if not lines or len(lines) > 8:
        return False
    allowed = re.compile(
        r"^\s*[)}\]]\s*;?\s*$|^\s*export\s+default\s+\w+\s*$|^\s*\)\s*$"
    )
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if not allowed.match(s) and s not in ("}", ");", "},", "});"):
            return False
    return any(l.strip() for l in lines)


def merge_fragment_code_blocks(text: str) -> str:
    """Une bloques que son solo fragmentos ( ) } export default) al bloque de código anterior."""
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```") and stripped != "```":
            fence = stripped
            out.append(line)
            i += 1
            block = []
            while i < len(lines) and lines[i].strip() != "```":
                block.append(lines[i])
                i += 1
            if i >= len(lines):
                out.extend(block)
                break
            i += 1  # consumir ```
            # Consumir todos los bloques fragmento siguientes (solo ) } export default)
            while i < len(lines):
                j = i
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j >= len(lines) or lines[j].strip() != fence:
                    break
                next_block = []
                j += 1
                while j < len(lines) and lines[j].strip() != "```":
                    next_block.append(lines[j])
                    j += 1
                if not is_fragment_code_block(next_block):
                    break
                block.append("")
                block.extend(next_block)
                i = j + 1 if j < len(lines) else j
            out.extend(block)
            out.append("```")
        else:
            out.append(line)
            i += 1
    return "\n".join(out)


def format_file(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    if "---" not in content:
        return
    parts = content.split("---", 2)
    if len(parts) < 2:
        return
    header = parts[0].strip()
    body = (parts[2] if len(parts) > 2 else parts[1]).strip()
    body_processed = process_body(body)
    # Normalizar múltiples líneas en blanco
    body_processed = re.sub(r"\n{3,}", "\n\n", body_processed).strip()
    # Quitar título ### duplicado del inicio (mismo número que el # del encabezado)
    section_match = re.match(r"#\s+([\d.]+)\s+", header)
    if section_match:
        section_id = section_match.group(1)
        lines = body_processed.split("\n")
        for idx, ln in enumerate(lines):
            stripped = ln.strip()
            if stripped.startswith("### " + section_id + ".") or stripped.startswith("### " + section_id + " "):
                lines.pop(idx)
                while idx < len(lines) and not lines[idx].strip():
                    lines.pop(idx)
                body_processed = "\n".join(lines)
                break
    body_processed = merge_consecutive_code_blocks(body_processed)
    body_processed = merge_fragment_code_blocks(body_processed)
    new_content = header + "\n\n---\n\n" + body_processed + "\n"
    path.write_text(new_content, encoding="utf-8")


def main():
    md_files = sorted(INDICE_DIR.glob("*.md"))
    md_files = [f for f in md_files if f.name != "README.md"]
    for path in md_files:
        try:
            format_file(path)
            print(f"  {path.name}")
        except Exception as e:
            print(f"  ERROR {path.name}: {e}")
    print(f"\nFormateados: {len(md_files)} archivos.")


if __name__ == "__main__":
    main()
