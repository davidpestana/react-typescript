# 14. Estado con useState

[← Índice](README.md) | [← Anterior: Eventos](13-eventos.md)

---

`useState` devuelve un valor y su setter. En TypeScript se infiere el tipo o se indica explícitamente.

```tsx
const Contador = () => {
  const [count, setCount] = useState<number>(0);
  const [nombre, setNombre] = useState<string>('');

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount((c) => c + 1)}>+1</button>
      <input value={nombre} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setNombre(e.target.value)} />
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

[Siguiente: 15. useEffect →](15-useeffect.md)
