#!/usr/bin/env python3
"""
Convierte bloques de código en .md a TSX con tipos:
- props sin tipo → Record<string, unknown>
- Component sin genéricos → Component<Record<string, unknown>>
- useState(...) → useState<Tipo>(...) cuando se puede inferir
- useRef() → useRef<unknown>(null)
Solo modifica bloques ```tsx o ```js/```jsx. No toca bloques que mezclan narrativa.
"""
import re
from pathlib import Path


def looks_like_code(first_lines: str) -> bool:
    """True si el bloque parece código (no narrativa en prosa)."""
    for line in first_lines.split("\n")[:5]:
        line = line.strip()
        if not line:
            continue
        if line.startswith(("import ", "export ", "const ", "let ", "var ", "function ", "class ", "return ", "<", "}")):
            return True
        if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*", line) or re.match(r"^\s*\)\s*=>", line):
            return True
        if re.match(r"^useState|^useEffect|^useRef|^useContext|^useReducer|^useMemo|^useCallback", line):
            return True
    return False


def convert_code_block(code: str, lang: str) -> str:
    """Aplica conversiones TSX dentro del bloque. lang en ('tsx','js','jsx')."""
    if lang not in ("tsx", "js", "jsx"):
        return code
    if not looks_like_code(code):
        return code

    lines = code.split("\n")
    out = []
    for i, line in enumerate(lines):
        s = line

        # Props en funciones: (props) =>  o  (props) =>  o  ( props ) =>
        s = re.sub(r"\(\s*props\s*\)\s*(=>|\))", r"(props: Record<string, unknown>) \1", s)
        # constructor(props)
        s = re.sub(r"constructor\s*\(\s*props\s*\)", r"constructor(props: Record<string, unknown>)", s)
        # class X extends Component {  (sin genéricos)
        s = re.sub(
            r"extends\s+Component\s*\{\s*$",
            "extends Component<Record<string, unknown>> {",
            s,
        )
        s = re.sub(
            r"extends\s+React\.Component\s*\{\s*$",
            "extends React.Component<Record<string, unknown>> {",
            s,
        )

        # useState con valor inicial inferible
        s = re.sub(r"useState\s*\(\s*''\s*\)", "useState<string>('')", s)
        s = re.sub(r'useState\s*\(\s*""\s*\)', 'useState<string>("")', s)
        s = re.sub(r"useState\s*\(\s*(\d+)\s*\)", r"useState<number>(\1)", s)
        s = re.sub(r"useState\s*\(\s*true\s*\)", "useState<boolean>(true)", s)
        s = re.sub(r"useState\s*\(\s*false\s*\)", "useState<boolean>(false)", s)
        s = re.sub(r"useState\s*\(\s*\[\s*\]\s*\)", "useState<unknown[]>([])", s)
        s = re.sub(r"useState\s*\(\s*\{\s*\}\s*\)", "useState<Record<string, unknown>>({})", s)
        s = re.sub(r"useState\s*\(\s*null\s*\)", "useState<unknown>(null)", s)

        # useRef() -> useRef<unknown>(null)
        s = re.sub(r"useRef\s*\(\s*\)\s*", "useRef<unknown>(null) ", s)
        s = re.sub(r"useRef\s*\(\s*\)\s*;", "useRef<unknown>(null);", s)
        s = re.sub(r"useRef\s*\(\s*\)\s*$", "useRef<unknown>(null)", s)

        # Event handlers típicos (opcional, para que compile)
        s = re.sub(
            r"onChange=\{\s*\(\s*e\s*\)\s*=>",
            "onChange={(e: React.ChangeEvent<HTMLInputElement>) =>",
            s,
        )
        s = re.sub(
            r"onClick=\{\s*\(\s*e\s*\)\s*=>",
            "onClick={(e: React.MouseEvent<HTMLButtonElement>) =>",
            s,
        )

        out.append(s)
    return "\n".join(out)


def process_file(path: Path) -> bool:
    """Procesa un .md y reescribe bloques de código. Devuelve True si hubo cambios."""
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r"^```(\w+)\s*\n(.*?)^```", re.MULTILINE | re.DOTALL)
    new_text = text
    changed = False

    for m in pattern.finditer(text):
        lang, code = m.group(1).lower(), m.group(2)
        converted = convert_code_block(code, lang)
        if converted != code:
            new_text = new_text.replace(m.group(0), f"```tsx\n{converted}\n```", 1)
            changed = True
        elif lang in ("js", "jsx") and looks_like_code(code):
            new_text = new_text.replace(m.group(0), f"```tsx\n{converted}\n```", 1)
            changed = True

    if changed:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main():
    import sys
    base = Path(__file__).resolve().parent
    dirs = sys.argv[1:] if len(sys.argv) > 1 else ["react-tsx-full", "react-tsx"]
    for d in dirs:
        folder = base / d
        if not folder.is_dir():
            print(f"  Omitido (no existe): {folder}")
            continue
        count = 0
        for path in sorted(folder.glob("*.md")):
            if path.name == "README.md":
                continue
            if process_file(path):
                count += 1
                print(f"  {d}/{path.name}")
        print(f"  {d}: {count} archivos actualizados.")


if __name__ == "__main__":
    main()
