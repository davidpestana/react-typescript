# miapp-ts — ejemplos del curso React + TypeScript

Aplicación de referencia con varios **demos** enlazados a capítulos del manual.

## Comandos

```bash
npm install
npm start    # http://localhost:3000
npm test     # tests del menú principal
npm run build
```

## Estructura

```
src/
├── App.tsx              # Menú y navegación entre demos
├── demos/
│   ├── HolaMundo/       # Props y tipos (cap. 14)
│   ├── PanelCodigoSecreto/  # useState (lab 18.1)
│   ├── Click.tsx        # Eventos (cap. 17)
│   ├── MiComponente.tsx # Ciclo de vida — clase (cap. 20)
│   └── ContadorRedux.tsx    # useReducer + store (caps. 28–29)
├── models/              # Tipos compartidos
└── store/               # Reducer y contexto del contador
```

## Añadir un demo

1. Crea el componente en `src/demos/`.
2. Regístralo en el array `DEMOS` de `src/App.tsx`.
