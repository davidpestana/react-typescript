# 20.5. Getsnapshotbeforeupdate

**PDF: páginas 89–89** (libro: 85–85)

---

[← Índice](README.md) | [← Anterior: 20.4. Shouldcomponentupdate](20-04-shouldComponentUpdate.md) | [Siguiente: 20.6. Componentdidupdate →](20-06-componentDidUpdate.md)

---

El método getSnapshotBeforeUpdate se ejecuta después del método render, pero antes de que los
cambios se realicen sobre el DOM real. Este es uno de los métodos del ciclo de vida menos
utilizados.

Este método recibe las propiedades y el estado anteriores y con el podemos devolver datos que
llegarán al siguiente método del ciclo de vida componentDidUpdate.

Este método se usa cuando necesitamos información de la vista o del componente justo antes del
cambio para compararla con la misma información después del cambio y saber si hay que realizar
alguna modificación.

Un caso donde se podría utilizar es cuando tenemos un chat y escribimos un mensaje. Podríamos
calcular si es necesario hacer un scroll automático para que el mensaje se muestre en caso de que
no entre en la pantalla.

getSnapshotBeforeUpdate(prevProps, prevState) {
```tsx
  if (prevProps.mensajes.length < this.props.mensajes.length) {
    const listaMensajes = this.mensajesRef.current;
    return listaMensajes.scrollHeight - listaMensajes.scrollTop;
  }
  return null;
}
```