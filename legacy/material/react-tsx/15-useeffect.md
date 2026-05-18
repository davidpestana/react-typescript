# 15. useEffect

[← Índice](README.md) | [← Anterior: Estado con useState](14-estado-usestate.md)

---

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

[Siguiente: 16. useRef →](16-useref.md)
