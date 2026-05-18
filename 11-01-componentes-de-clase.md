# 11.1. Componentes De Clase

**PDF: páginas 40–41** (libro: 36–37)

---

[← Índice](README.md) | [← Anterior: 11. Componentes](11-00-componentes.md) | [Siguiente: 11.2. Componentes Funcionales →](11-02-componentes-funcionales.md)

---

```tsx
Los componentes de clase son clases de JavaScript que extienden de React.Component.
```
Dentro de la clase tenemos que añadir un método render que tiene que devolver la estructura del
componente (el código TSX) para que React sepa que tiene que pintar.

```tsx
import { Component } from 'react';

class MiComponente extends Component {
  render() {
    return (
      <h1>Hola mundo</h1>
    )
  }
}

export default MiComponente;
```
Al ser una clase, podemos añadir un constructor, el cual recibe unas propiedades desde el exterior.
Más adelante veremos para que usar las propiedades. Y al estar extendiendo de Component
tenemos que llamar al super pasandole estas propiedades para que las añada al objeto this.

```tsx
import { Component } from 'react';

class MiComponente extends Component {
  constructor(props) {
    super(props)
  }

    render() {
      return (
        <h1>Hola mundo</h1>
      )
    }
}

export default MiComponente;
```
Dentro del constructor es donde inicializaremos el estado del componente, pero esto ya lo veremos
más adelante.

Desde la aparición de los React Hooks, este tipo de componentes se están dejando
de usar a favor de los componentes funcionales.

Antes no había otra opción ya que en los componentes de clase era el único sitio
donde podíamos añadir un estado y los métodos del ciclo de vida de los

componentes.