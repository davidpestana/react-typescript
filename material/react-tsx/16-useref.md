# 16. useRef

[← Índice](README.md) | [← Anterior: useEffect](15-useeffect.md)

---

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

[Siguiente: 17. useMemo, useCallback, useReducer →](17-usememo-usecallback-usereducer.md)
