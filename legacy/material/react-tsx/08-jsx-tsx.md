# 8. ¿Qué es JSX/TSX?

[← Índice](README.md) | [← Anterior: Configuración con Vite](07-configuracion-vite.md)

---

**JSX** es una extensión de sintaxis que permite escribir marcado tipo HTML en JavaScript. **TSX** es lo mismo en archivos TypeScript.

- Las etiquetas en minúscula son elementos HTML.
- Las que empiezan por mayúscula son **componentes** de React.
- Las expresiones van entre `{ }`.

```tsx
const nombre = 'Ana';
const element = <h1>Hola, {nombre}</h1>;
```

En TSX, las props y el retorno del componente se pueden tipar.

---

[Siguiente: 9. Componentes funcionales y TSX →](09-componentes-funcionales-tsx.md)
