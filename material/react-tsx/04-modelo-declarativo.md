# 4. Modelo declarativo

[← Índice](README.md) | [← Anterior: Composición](03-composicion.md)

---

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

[Siguiente: 5. Virtual DOM →](05-virtual-dom.md)
