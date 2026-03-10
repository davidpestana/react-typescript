# 11. Listas y key

[← Índice](README.md) | [← Anterior: Propiedades (props) con tipos](10-props-con-tipos.md)

---

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

[Siguiente: 12. Renderizado condicional →](12-renderizado-condicional.md)
