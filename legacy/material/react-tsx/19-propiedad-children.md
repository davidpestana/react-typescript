# 19. Propiedad children

[← Índice](README.md) | [← Anterior: Custom hooks](18-custom-hooks.md)

---

Para componentes que envuelven contenido. Se tipa con `React.ReactNode`.

```tsx
interface LayoutProps {
  title: string;
  children: React.ReactNode;
}

const Layout = ({ title, children }: LayoutProps) => (
  <div>
    <h1>{title}</h1>
    {children}
  </div>
);
```

---

[Siguiente: 20. Fragments →](20-fragments.md)
