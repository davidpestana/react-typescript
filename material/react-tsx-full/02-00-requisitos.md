# 2. Requisitos

**PDF: páginas 6–6** (libro: 2–2)

---

[← Índice](README.md) | [← Anterior: 1. Que Es React](01-00-que-es-react.md) | [Siguiente: 3. Composicion →](03-00-composicion.md)

---

## Requisitos

Para seguir este curso vamos a usar un **entorno uniforme** basado en **GitHub Codespaces**: harás un fork de este repo y trabajarás dentro de un Codespace. Así no tendrás que instalar Node ni el editor en tu máquina (aunque también puedes clonar y usar VS Code en local).

### Opción recomendada: Fork + GitHub Codespaces

1. **Haz fork del repositorio**  
   En la página del repo en GitHub, clic en **Fork**. Tendrás una copia en tu cuenta (por ejemplo `tu-usuario/react-tsx-full`).

2. **Abre un Codespace**  
   En tu fork: botón **Code** → pestaña **Codespaces** → **Create codespace on main**. GitHub crea un contenedor con Linux, Node.js y VS Code en el navegador (o en la app Codespaces).

3. **Espera a que termine de cargar**  
   La primera vez puede tardar un minuto. Cuando veas el explorador de archivos y el terminal, ya puedes seguir el curso.

4. **Dónde practicar**  
   En el mismo Codespace puedes crear tu proyecto React (por ejemplo con Vite, cap. 7.5) en una carpeta nueva (`mi-app`, `labs`, etc.) y seguir los labs.

### Configurar el Codespace (extensiones recomendadas)

Al abrir el repo, VS Code / Codespaces puede sugerir instalar extensiones recomendadas. Si no aparece el aviso:

- Abre la paleta de comandos (`Ctrl+Shift+P` / `Cmd+Shift+P`) y ejecuta **Extensions: Show Recommended Extensions**.
- Instala las que aparezcan para este workspace (o las que listamos abajo).

**Extensiones recomendadas** (incluidas en `.vscode/extensions.json` del repo):

- **ESLint** (`dbaeumer.vscode-eslint`): reglas y formato de JavaScript/TypeScript.
- **Prettier** (`esbenp.prettier-vscode`): formato automático (opcional).
- **TypeScript / TSX**: ya incluido en VS Code; resaltado y tipos para `.ts` / `.tsx`.
- **ES7+ React snippets** (`dsznajder.es7-react-js-snippets`): snippets para React (opcional).

En Codespaces muchas de estas se instalan automáticamente si están en `extensions.json`. El repo incluye también un **devcontainer** (`.devcontainer/devcontainer.json`) para que el Codespace use Node 22 y las extensiones anteriores por defecto.

### Requisitos si trabajas en local (sin Codespaces)

- **Editor**: [VS Code](https://code.visualstudio.com/) (recomendado) u otro editor con soporte para TypeScript/TSX.
- **Node y npm**: [Node.js](https://nodejs.org/) LTS (incluye npm). Comprueba con `node -v` y `npm -v`.
- **Navegador**: Chrome, Firefox o Edge actualizado (para probar los proyectos de los labs).
- **Git**: para clonar el repo y, si usas fork, para subir cambios.

### Resumen

- **Con Codespaces**: solo necesitas cuenta en GitHub; el fork y el Codespace te dan el entorno listo.
- **En local**: Node.js, VS Code (o similar), navegador y Git.
