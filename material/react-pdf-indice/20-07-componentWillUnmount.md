# 20.7. Componentwillunmount

**PDF: páginas 91–91** (libro: 87–87)

---

El método componentWillUnmount se ejecuta justo antes de eliminar el componente del DOM.

Este método se suele utilizar para limpiar operaciones que se han inicializado anteriormente y que
de no eliminarlas seguirían ejecutandose o gastando recursos.

Algunos ejemplos en los que se puede utilizar este método:

- Limpiar un timer (setInterval)

- Desuscribirse de observables

- Eliminar elementos HTML manejados por otras librerías (jQuery)

componentWillUnmount() {
```tsx
  observable.unsubscribe();
}
```
