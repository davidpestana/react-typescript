# 17. useMemo, useCallback, useReducer

[← Índice](README.md) | [← Anterior: useRef](16-useref.md)

---

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

[Siguiente: 18. Custom hooks →](18-custom-hooks.md)
