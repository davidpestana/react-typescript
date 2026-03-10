# 10. Propiedades (props) con tipos

[← Índice](README.md) | [← Anterior: Componentes funcionales y TSX](09-componentes-funcionales-tsx.md)

---

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

[Siguiente: 11. Listas y key →](11-listas-y-key.md)
