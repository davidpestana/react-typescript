# 7.5. Lab Vite (React con TypeScript)

**Material añadido para el curso.**

---

En este laboratorio vamos a crear un proyecto de React con TypeScript usando Vite, levantar el servidor de desarrollo y generar el build de producción.

## Paso 1: Crear el proyecto

Crea la carpeta del proyecto con el template **react-ts** (React + TypeScript):

```bash
npm create vite@latest reactjs-vite-lab -- --template react-ts
```

Cuando pregunte por el nombre del proyecto, o si usas el comando anterior, se creará la carpeta `reactjs-vite-lab`. Entra en ella e instala las dependencias:

```bash
cd reactjs-vite-lab
npm install
```

## Paso 2: Estructura generada

El template incluye algo como:

```
reactjs-vite-lab/
├── index.html
├── package.json
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
└── src/
    ├── main.tsx
    ├── App.tsx
    ├── App.css
    ├── index.css
    └── vite-env.d.ts
```

- **index.html**: punto de entrada en la raíz; Vite inyecta el script del bundle.
- **src/main.tsx**: aquí se hace `createRoot` y `render` del componente raíz.
- **src/App.tsx**: componente raíz en TypeScript/TSX.
- **vite-env.d.ts**: referencias de tipos para Vite (por ejemplo para importar `.svg`).
- **tsconfig.json** / **vite.config.ts**: configuración de TypeScript y Vite.

## Paso 3: Servidor de desarrollo

Levanta el servidor de desarrollo:

```bash
npm run dev
```

Abre en el navegador la URL que muestre la consola (por ejemplo http://localhost:5173/). Deberías ver la aplicación por defecto. Los cambios en el código se reflejan al instante (HMR).

## Paso 4: Revisar la entrada y el componente

**Archivo:** `src/main.tsx`

```tsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'
import './index.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

**Archivo:** `src/App.tsx` (ejemplo simplificado)

```tsx
function App() {
  return (
    <div>
      <h1>Hola mundo con Vite + React + TypeScript</h1>
    </div>
  )
}

export default App
```

Puedes editar `App.tsx` y guardar; la página se actualiza sin recargar a mano.

## Paso 5: Build de producción

Genera los archivos estáticos para producción:

```bash
npm run build
```

La salida queda en la carpeta `dist/`. Para probar ese build en local:

```bash
npm run preview
```

Se sirve el contenido de `dist` (por defecto en http://localhost:4173 o similar).

## Resumen de scripts

- **npm run dev**: servidor de desarrollo (HMR).
- **npm run build**: build de producción → carpeta `dist/`.
- **npm run preview**: previsualizar el build en local.

Con esto tienes un proyecto React con TypeScript listo para seguir el curso. Los siguientes capítulos (TSX, componentes, estado, etc.) se aplican igual sobre este proyecto.
