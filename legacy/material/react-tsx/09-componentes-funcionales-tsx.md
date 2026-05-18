# 9. Componentes funcionales y TSX

[← Índice](README.md) | [← Anterior: ¿Qué es JSX/TSX?](08-jsx-tsx.md)

---

Los componentes son funciones que devuelven JSX/TSX. Con TypeScript definimos una interfaz para las props.

```tsx
interface SaludoProps {
  nombre: string;
  edad?: number;
}

const Saludo = ({ nombre, edad = 18 }: SaludoProps) => (
  <p>Hola {nombre}, edad {edad}</p>
);

// Uso
<Saludo nombre="Laura" />
<Saludo nombre="Pedro" edad={25} />
```

Sintaxis TSX: llaves para expresiones, `className` en lugar de `class`, etc.

---

[Siguiente: 10. Propiedades (props) con tipos →](10-props-con-tipos.md)
