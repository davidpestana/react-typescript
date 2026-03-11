# 12. Expresiones

**PDF: páginas 43–43** (libro: 39–39)

---

[← Índice](README.md) | [← Anterior: 11.2. Componentes Funcionales](11-02-componentes-funcionales.md) | [Siguiente: 13. Estilos →](13-00-estilos.md)

---

## Expresiones

Dentro de React, usaremos {} para mostrar datos que tenemos en variables en nuestra aplicación,
darle valores a los atributos de las etiquetas o propiedades de los componentes…

Dentro de las llaves, podemos añadir cualquier expresión de JavaScript, como una variable, una
condición, llamadas a funciones…

```tsx
<button type="button" disabled={btnDisabled}>Botón {btnDisabled ? 'deshabilitado' : 'habilitado'}</button>
```