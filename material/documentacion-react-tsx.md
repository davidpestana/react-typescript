# React con TypeScript (TSX)

Versión del manual de React adaptada a **TypeScript** y **TSX**, con configuración mediante **Vite**.  
Basado en la documentación React (Pronoide).

---

## Contenidos

1. [¿Qué es React?](#1-qué-es-react)
2. [Requisitos](#2-requisitos)
3. [Composición](#3-composición)
4. [Modelo declarativo](#4-modelo-declarativo)
5. [Virtual DOM](#5-virtual-dom)
6. [React vs jQuery](#6-react-vs-jquery)
7. [Configuración con Vite](#7-configuración-con-vite)
8. [¿Qué es JSX/TSX?](#8-qué-es-jsxtsx)
9. [Componentes funcionales y TSX](#9-componentes-funcionales-y-tsx)
10. [Propiedades (props) con tipos](#10-propiedades-props-con-tipos)
11. [Listas y key](#11-listas-y-key)
12. [Renderizado condicional](#12-renderizado-condicional)
13. [Eventos](#13-eventos)
14. [Estado con useState](#14-estado-con-usestate)
15. [useEffect](#15-useeffect)
16. [useRef](#16-useref)
17. [useMemo, useCallback, useReducer](#17-usememo-usecallback-usereducer)
18. [Custom hooks](#18-custom-hooks)
19. [Propiedad children](#19-propiedad-children)
20. [Fragments](#20-fragments)
21. [Context API con useContext](#21-context-api-con-usecontext)
22. [Formularios controlados y no controlados](#22-formularios)
23. [Testing con Vitest](#23-testing-con-vitest)

---

## 1. ¿Qué es React?

React es una librería open source de JavaScript/TypeScript para crear interfaces de usuario que sigue el paradigma de la programación orientada a componentes.

- No es un framework: se centra en la **UI**; el resto (rutas, estado global, etc.) se elige aparte.
- Desarrollada por Meta (Facebook). Muy usada en la industria (Netflix, Instagram, Airbnb, etc.).

---

## 2. Requisitos

- **Node.js** y **npm** (o pnpm/yarn)
- **Editor**: VSCode recomendado (buen soporte TypeScript y React)
- Navegador actualizado

---

## 3. Composición

En React todo son **componentes**: piezas reutilizables que encapsulan vista, comportamiento y estado. Se componen unos dentro de otros para construir la interfaz.

Con TypeScript, los componentes reciben **props tipadas** y el IDE ofrece autocompletado y comprobación en tiempo de compilación.

![Componente card](react-tsx/images/card-007.png)  
*Figura 1 — Componente card*

![Composición del componente card](react-tsx/images/card-008.png)  
*Figura 2 — Composición del componente card*

---

## 4. Modelo declarativo

React es **declarativo**: describes *qué* debe verse según el estado, no *cómo* manipular el DOM paso a paso.

**Imperativo (DOM directo):**

```ts
const app = document.getElementById('app')!;
const div = document.createElement('div');
const h1 = document.createElement('h1');
h1.innerText = 'Hola mundo';
div.appendChild(h1);
app.appendChild(div);
```

**Declarativo con TSX:**

```tsx
const HolaMundo = () => (
  <div id="contenedor-saludo">
    <h1>Hola mundo</h1>
  </div>
);

createRoot(document.getElementById('app')!).render(<HolaMundo />);
```

---

## 5. Virtual DOM

React mantiene una representación en memoria del DOM (Virtual DOM). Ante cambios de estado:

1. Actualiza el Virtual DOM.
2. Compara con la versión anterior (diff).
3. Aplica solo los cambios mínimos al DOM real.

Trabajamos con componentes y estado; React se encarga de actualizar el DOM de forma eficiente.

![Virtual DOM — flujo](react-tsx/images/react-pdf-004.png)

---

## 6. React vs jQuery

- **jQuery**: manipulación imperativa del DOM, eventos y datos repartidos.
- **React**: modelo declarativo, componentes, flujo de datos unidireccional y Virtual DOM. Con TypeScript añadimos tipos a props y estado.

![React vs jQuery](react-tsx/images/fig-010.png)

---

## 7. Configuración con Vite

En este curso usamos **Vite** en lugar de Create React App o Webpack manual.

### Crear proyecto

```bash
npm create vite@latest mi-app -- --template react-ts
cd mi-app
npm install
npm run dev
```

### Estructura típica

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

### Scripts

- `npm run dev` — servidor de desarrollo
- `npm run build` — build de producción
- `npm run preview` — previsualizar el build

Los archivos de componentes usan extensión **`.tsx`** cuando incluyen JSX.

---

## 8. ¿Qué es JSX/TSX?

**JSX** es una extensión de sintaxis que permite escribir marcado tipo HTML en JavaScript. **TSX** es lo mismo en archivos TypeScript.

- Las etiquetas en minúscula son elementos HTML.
- Las que empiezan por mayúscula son **componentes** de React.
- Las expresiones van entre `{ }`.

```tsx
const nombre = 'Ana';
const element = <h1>Hola, {nombre}</h1>;
```

En TSX, las props y el retorno del componente se pueden tipar.

---

## 9. Componentes funcionales y TSX

Los componentes son funciones que devuelven JSX/TSX. Con TypeScript definimos una interfaz para las props.

```tsx
interface SaludoProps {
  nombre: string;
  edad?: number;
}

const Saludo = ({ nombre, edad = 18 }: SaludoProps) => (
  <p>Hola {nombre}, edad {edad}</p>
);

// Uso
<Saludo nombre="Laura" />
<Saludo nombre="Pedro" edad={25} />
```

Sintaxis TSX: llaves para expresiones, `className` en lugar de `class`, etc.

---

## 10. Propiedades (props) con tipos

Las props se tipan con una **interface** (o `type`). Así evitamos errores y tenemos autocompletado.

```tsx
interface CardProps {
  titulo: string;
  descripcion: string;
  onVerMas?: () => void;
}

const Card = ({ titulo, descripcion, onVerMas }: CardProps) => (
  <div className="card">
    <h2>{titulo}</h2>
    <p>{descripcion}</p>
    {onVerMas && <button onClick={onVerMas}>Ver más</button>}
  </div>
);
```

Valores por defecto con desestructuración:

```tsx
interface BotonProps {
  texto: string;
  tipo?: 'primario' | 'secundario';
}

const Boton = ({ texto, tipo = 'primario' }: BotonProps) => (
  <button className={`btn btn-${tipo}`}>{texto}</button>
);
```

En TypeScript **no usamos PropTypes**: los tipos sustituyen esa validación en tiempo de compilación.

---

## 11. Listas y key

Al renderizar listas, cada elemento debe tener una **key** estable y única (idealmente un id).

```tsx
interface Noticia {
  id: number;
  titulo: string;
  resumen: string;
}

interface ListaNoticiasProps {
  noticias: Noticia[];
}

const ListaNoticias = ({ noticias }: ListaNoticiasProps) => (
  <ul>
    {noticias.map((noticia) => (
      <li key={noticia.id}>
        <strong>{noticia.titulo}</strong> — {noticia.resumen}
      </li>
    ))}
  </ul>
);
```

No uses el índice como `key` si la lista puede reordenarse o modificarse.

---

## 12. Renderizado condicional

Condiciones dentro del JSX con `&&` o ternarios:

```tsx
const Mensaje = ({ estaLogado, nombre }: { estaLogado: boolean; nombre?: string }) => (
  <div>
    {estaLogado ? (
      <p>Bienvenido, {nombre}</p>
    ) : (
      <p>Debes iniciar sesión</p>
    )}
    {nombre && <span>Usuario: {nombre}</span>}
  </div>
);
```

---

## 13. Eventos

Los eventos en React son **sintéticos** (SyntheticEvent). Se tipan con los tipos de React.

```tsx
const FormularioEjemplo = () => {
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // ...
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value);
  };

  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.currentTarget.disabled = true;
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" onChange={handleChange} />
      <button type="button" onClick={handleClick}>Enviar</button>
    </form>
  );
};
```

Tipos habituales: `React.ChangeEvent<HTMLInputElement>`, `React.MouseEvent<HTMLButtonElement>`, `React.FormEvent<HTMLFormElement>`.

---

## 14. Estado con useState

`useState` devuelve un valor y su setter. En TypeScript se infiere el tipo o se indica explícitamente.

```tsx
const Contador = () => {
  const [count, setCount] = useState<number>(0);
  const [nombre, setNombre] = useState<string>('');

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount((c) => c + 1)}>+1</button>
      <input value={nombre} onChange={(e) => setNombre(e.target.value)} />
    </div>
  );
};
```

Para objetos o arrays, define una interfaz:

```tsx
interface Usuario {
  nombre: string;
  email: string;
}

const [usuario, setUsuario] = useState<Usuario | null>(null);
```

---

## 15. useEffect

Para efectos secundarios (peticiones, suscripciones, timers). El tipo del efecto es `() => void | (() => void)` (cleanup opcional).

```tsx
useEffect(() => {
  const subscription = api.subscribe();
  return () => subscription.unsubscribe();
}, []);

// Con dependencias
useEffect(() => {
  fetch(`/api/user/${id}`)
    .then((res) => res.json())
    .then(setUser);
}, [id]);
```

---

## 16. useRef

Para referencias a nodos del DOM o para guardar un valor mutable que no dispare re-renders.

```tsx
const InputConFoco = () => {
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  return <input ref={inputRef} type="text" />;
};
```

Formularios no controlados: leer valor con `inputRef.current?.value`.

---

## 17. useMemo, useCallback, useReducer

- **useMemo**: memorizar un valor calculado.
- **useCallback**: memorizar una función (p. ej. para pasarla a hijos).
- **useReducer**: estado complejo con lógica de actualización centralizada.

```tsx
const [items, setItems] = useState<Item[]>([]);
const total = useMemo(() => items.reduce((acc, i) => acc + i.precio, 0), [items]);

const handleAdd = useCallback((item: Item) => {
  setItems((prev) => [...prev, item]);
}, []);

type Action = { type: 'increment' } | { type: 'decrement' };
const reducer = (state: number, action: Action) => {
  switch (action.type) {
    case 'increment': return state + 1;
    case 'decrement': return state - 1;
    default: return state;
  }
};
const [state, dispatch] = useReducer(reducer, 0);
```

---

## 18. Custom hooks

Hooks que encapsulan lógica reutilizable. Deben cumplir las reglas de los Hooks (solo en nivel superior, solo en funciones/componentes de React).

```tsx
function useToggle(initial = false): [boolean, () => void] {
  const [value, setValue] = useState(initial);
  const toggle = useCallback(() => setValue((v) => !v), []);
  return [value, toggle];
}

// Uso
const [visible, toggleVisible] = useToggle(false);
```

---

## 19. Propiedad children

Para componentes que envuelven contenido. Se tipa con `React.ReactNode`.

```tsx
interface LayoutProps {
  title: string;
  children: React.ReactNode;
}

const Layout = ({ title, children }: LayoutProps) => (
  <div>
    <h1>{title}</h1>
    {children}
  </div>
);
```

---

## 20. Fragments

Agrupar varios elementos sin añadir un nodo al DOM. En TSX se usa `<></>` o `<Fragment>`.

```tsx
const Lista = () => (
  <>
    <li>A</li>
    <li>B</li>
    <li>C</li>
  </>
);
```

---

## 21. Context API con useContext

Para compartir datos sin pasar props en cada nivel. El valor del contexto se tipa con un tipo o interfaz.

```tsx
interface TemaContextType {
  tema: 'claro' | 'oscuro';
  toggleTema: () => void;
}

const TemaContext = createContext<TemaContextType | null>(null);

export const useTema = () => {
  const ctx = useContext(TemaContext);
  if (!ctx) throw new Error('useTema debe usarse dentro de TemaProvider');
  return ctx;
};

export const TemaProvider = ({ children }: { children: React.ReactNode }) => {
  const [tema, setTema] = useState<'claro' | 'oscuro'>('claro');
  const toggleTema = () => setTema((t) => (t === 'claro' ? 'oscuro' : 'claro'));
  return (
    <TemaContext.Provider value={{ tema, toggleTema }}>
      {children}
    </TemaContext.Provider>
  );
};
```

---

## 22. Formularios

**Controlados**: el valor vive en estado y se actualiza con `onChange`.

```tsx
const [email, setEmail] = useState('');
<input value={email} onChange={(e) => setEmail(e.target.value)} />
```

**No controlados**: se usa `useRef` y se lee el valor cuando hace falta (p. ej. en `onSubmit`).

```tsx
const inputRef = useRef<HTMLInputElement>(null);
<input ref={inputRef} defaultValue="" />
// luego: inputRef.current?.value
```

---

## 23. Testing con Vitest

Vitest se integra bien con Vite y React. Para componentes se suele usar **React Testing Library**.

```bash
npm install -D vitest @testing-library/react @testing-library/jest-dom jsdom
```

Ejemplo de prueba de un componente TSX:

```tsx
import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { Saludo } from './Saludo';

describe('Saludo', () => {
  it('muestra el nombre', () => {
    render(<Saludo nombre="Ana" />);
    expect(screen.getByText(/Hola Ana/)).toBeInTheDocument();
  });
});
```

Configuración en `vite.config.ts`: añadir `test: { environment: 'jsdom', globals: true }` y en `tsconfig` los tipos de Vitest si usas `expect` global.

---

## Resumen

- **Vite** para crear y ejecutar el proyecto React + TypeScript.
- Componentes como **funciones** con **props tipadas** (interface/type).
- **Hooks** tipados: `useState<T>`, `useRef<T>`, `useContext` con contexto tipado.
- **Eventos**: `React.ChangeEvent<HTMLInputElement>`, etc.
- **Context**: `createContext<T>`, `useContext` y provider con `value` tipado.
- **Testing**: Vitest + React Testing Library con componentes TSX.

Con esto tienes el manual de React traducido a **TSX** y alineado con el contenido del curso (Vite, Hooks, Context, formularios, testing).
