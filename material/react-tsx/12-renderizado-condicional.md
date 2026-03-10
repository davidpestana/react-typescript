# 12. Renderizado condicional

[← Índice](README.md) | [← Anterior: Listas y key](11-listas-y-key.md)

---

Condiciones dentro del JSX con `&&` o ternarios:

```tsx
const Mensaje = ({ estaLogado, nombre }: { estaLogado: boolean; nombre?: string }) => (
  <div>
    {estaLogado ? (
      <p>Bienvenido, {nombre}</p>
    ) : (
      <p>Debes iniciar sesión</p>
    )}
    {nombre && <span>Usuario: {nombre}</span>}
  </div>
);
```

---

[Siguiente: 13. Eventos →](13-eventos.md)
