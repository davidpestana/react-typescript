# 14.3. Validacion Propiedades Personalizadas

**PDF: páginas 49–49** (libro: 45–45)

---

[← Índice](README.md) | [← Anterior: 14.2. Proptypes Validacion](14-02-proptypes-validacion.md) | [Siguiente: 14.4. Lab Propiedades →](14-04-lab-propiedades.md)

---

En el enfoque original con **PropTypes**, además de los validadores predefinidos se podían crear
validaciones personalizadas asignando una función a la propiedad: si la validación fallaba, la
función devolvía un `Error` con el mensaje a mostrar.

En este curso trabajamos con **TypeScript**, así que estas validaciones personalizadas las haremos
con **tipos** y, cuando haga falta lógica en tiempo de ejecución, con **funciones de validación**
(`type guards`), en lugar de usar `MiComponente.propTypes`.

Por ejemplo, en lugar de:

```tsx
MiComponente.propTypes = {
  numero: function(props, propName, componentName) {
    if (props[propName] < 0) {
      return new Error('El número tiene que ser mayor a 0');
    }
  }
}
```

podemos escribir en TypeScript:

```tsx
type NumeroPositivo = number;

function esNumeroPositivo(value: number): value is NumeroPositivo {
  if (value < 0) {
    console.error('El número tiene que ser mayor a 0');
    return false;
  }
  return true;
}
```

De esta forma movemos la validación personalizada al mundo de los **tipos** y de las **funciones
de ayuda en TypeScript**, sin depender de la librería `prop-types`.