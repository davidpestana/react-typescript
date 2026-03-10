# React con TypeScript

Curso de desarrollo de SPAs con React y TypeScript. Nivel básico.

---

## Datos del curso

| | |
|---|---|
| **Duración** | 24 horas |
| **Nivel** | Básico |
| **Objetivo** | Desarrollar SPAs usando React con TypeScript |

---

## Dirigido a

Personas que quieran aprender a crear Single Page Applications (SPAs) con la librería React.

## Requisitos previos

- Conocimientos de **HTML**, **CSS** y **JavaScript (ES6)**.

---

## Contenido

### 1. Introducción y configuración
- ¿Qué es una SPA?
- Diferencia entre React y otras librerías (jQuery)
- Fundamentos de React: Virtual DOM, flujo de datos unidireccional
- ¿Qué es JSX?
- Configuración de un proyecto con **Vite**

### 2. TypeScript en React: componentes funcionales y TSX
- Componentes funcionales
- Sintaxis TSX
- Propiedades (props)
- Listas y la clave `key`
- Composición de componentes
- Propiedad `children`

### 3. Estado y React Hooks principales
- Manejo del estado con `useState`
- Efectos colaterales con `useEffect`
- Reutilización de lógica con custom hooks
- Hooks: `useMemo`, `useCallback` y `useReducer`

### 4. Eventos y formularios
- Eventos sintéticos y personalizados de React
- Formularios con componentes controlados
- Formularios con componentes no controlados (`useRef`)

### 5. Context API
- Uso de `useContext`

### 6. Testing
- Testing con **Vitest**

---

## Material de referencia

En este repositorio encontrarás:

- **documentacion-reactjs.pdf** — Documentación de React (Pronoide)
- **documentacion-typescript.pdf** — Documentación de TypeScript (Pronoide)
- **material/documentacion-react-tsx.md** — Versión del manual de React con ejemplos en **TSX** y configuración con **Vite**

---

## Estructura del curso

```
react-typescript/
├── README.md
├── documentacion-reactjs.pdf
├── documentacion-typescript.pdf
├── React con TypeScript (rev) (1).docx   # Programa del curso
├── material/
│   ├── README.md
│   ├── documentacion-react-tsx.md         # React con TypeScript (TSX + Vite), documento único
│   └── react-tsx/                          # Un .md por capítulo (01 a 23)
│       ├── README.md                       # Índice de capítulos
│       ├── 01-que-es-react.md
│       ├── ... (23 archivos)
│       └── 23-testing-vitest.md
│
├── 01-introduccion-configuracion/        # SPA, React, Virtual DOM, JSX, Vite
│   └── README.md
├── 02-componentes-tsx/                   # Componentes funcionales, props, key, children
│   └── README.md
├── 03-estado-hooks/                      # useState, useEffect, custom hooks, useMemo, useCallback, useReducer
│   └── README.md
├── 04-eventos-formularios/               # Eventos, formularios controlados y useRef
│   └── README.md
├── 05-context-api/                       # useContext
│   └── README.md
└── 06-testing/                           # Vitest
    └── README.md
```

Cada carpeta corresponde a un bloque del temario y contiene un `README.md` con el contenido del módulo y espacio para ejercicios o labs.
