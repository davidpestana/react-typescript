# 18. Custom hooks

[← Índice](README.md) | [← Anterior: useMemo, useCallback, useReducer](17-usememo-usecallback-usereducer.md)

---

Hooks que encapsulan lógica reutilizable. Deben cumplir las reglas de los Hooks (solo en nivel superior, solo en funciones/componentes de React).

```tsx
function useToggle(initial = false): [boolean, () => void] {
  const [value, setValue] = useState<boolean>(initial);
  const toggle = useCallback(() => setValue((v) => !v), []);
  return [value, toggle];
}

// Uso
const [visible, toggleVisible] = useToggle(false);
```

---

[Siguiente: 19. Propiedad children →](19-propiedad-children.md)
