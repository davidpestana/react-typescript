# 21. Context API con useContext

[← Índice](README.md) | [← Anterior: Fragments](20-fragments.md)

---

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

[Siguiente: 22. Formularios →](22-formularios.md)
