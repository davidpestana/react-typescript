# 7. Configuración con Vite

[← Índice](README.md) | [← Anterior: React vs jQuery](06-react-vs-jquery.md)

---

En este curso usamos **Vite** en lugar de Create React App o Webpack manual.

## Crear proyecto

```bash
npm create vite@latest mi-app -- --template react-ts
cd mi-app
npm install
npm run dev
```

## Estructura típica

```
mi-app/
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
└── src/
    ├── main.tsx          # Entrada: createRoot + render
    ├── App.tsx
    ├── App.css
    └── vite-env.d.ts
```

## Scripts

- `npm run dev` — servidor de desarrollo
- `npm run build` — build de producción
- `npm run preview` — previsualizar el build

Los archivos de componentes usan extensión **`.tsx`** cuando incluyen JSX.

---

[Siguiente: 8. ¿Qué es JSX/TSX? →](08-jsx-tsx.md)
