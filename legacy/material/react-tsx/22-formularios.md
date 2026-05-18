# 22. Formularios

[← Índice](README.md) | [← Anterior: Context API con useContext](21-context-api-usecontext.md)

---

**Controlados**: el valor vive en estado y se actualiza con `onChange`.

```tsx
const [email, setEmail] = useState<string>('');
<input value={email} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)} />

```

**No controlados**: se usa `useRef` y se lee el valor cuando hace falta (p. ej. en `onSubmit`).

```tsx
const inputRef = useRef<HTMLInputElement>(null);
<input ref={inputRef} defaultValue="" />
// luego: inputRef.current?.value
```

---

[Siguiente: 23. Testing con Vitest →](23-testing-vitest.md)
