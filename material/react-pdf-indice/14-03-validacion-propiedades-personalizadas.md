# 14.3. Validacion Propiedades Personalizadas

**PDF: páginas 49–49** (libro: 45–45)

---

A parte de las validaciones que vienen predefinidas, podemos crear nuestras propias validaciones
asignando una función a la propiedad. Cuando no se cumple la validación la función tiene que
devolver un Error con el mensaje a mostrar.

MiComponente.propTypes = {
```tsx
  numero: function(props, propName, componentName) {
    if (props[propName] < 0) {
      return new Error('El número tiene que ser mayor a 0');
    }
  }
}
```
