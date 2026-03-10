# 20.6. Componentdidupdate

**PDF: páginas 90–90** (libro: 86–86)

---

El componendDidUpdate es un método que se ejecuta justo después de que el componente se
actualice.

Este método se puede utilizar para volver a pedir unos datos del exterior (una API) o para
actualizar elementos del DOM gestionados por otras librerías.

Este método recibe las propiedades anteriores para poder compararlas con las actuales y saber por
ejemplo si es necesario volver a pedir unos datos. Quizás el dato por el cual pediríamos los datos
sigue siendo el mismo, no haría falta realizar la petición de nuevo.

Recibe un parámetro más, el snapshot que se lo manda el método getSnapshotBeforeUpdate con
la info necesaria para modificar algo en el DOM (por ejemplo el scroll).

componentDidUpdate(prevProps, snapshot) {
```tsx
  if (prevProps.textoFiltro !== this.props.textoFiltro) {
    // Pedimos los datos filtrados por el nuevo texto
  }
}
```
Cuidado con modificar dentro de este método el estado sin añadir una condición,
 ya que entraremos en un bucle infinito de renderizados.
