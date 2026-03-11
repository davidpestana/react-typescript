# 23. Fragments

**PDF: páginas 115–116** (libro: 111–112)

---

[← Índice](README.md) | [← Anterior: 22.1. Lab Propiedad Children](22-01-lab-propiedad-children.md) | [Siguiente: 24. Context Api →](24-00-context-api.md)

---

## Fragments

En React no podemos devolver dos elementos HTML o componentes si no están envueltos por otro
elemento.

```tsx
import { useState } from 'react';

const App = () => {
  const [productos, setProductos] = useState(['Tripode para teléfono', 'Gafas de sol cuadradas', 'Sombrero de pescador',
'Tira LED RGB de 5m']);

const listaProductos = productos.map((producto, pos) => (
   // ERROR
   <p>{producto}</p>
   {pos !== productos.length - 1 && <hr/>}
))

    return (
      <div>
        {listaProductos}
      </div>
    )
}

export default App
```
El problema de esto es que el código puede quedar sucio si nos encontramos elementos envueltos
por otros que no necesitamos. Al final acabamos con muchas etiquetas div innecesarias.

```tsx
Los Fragments son la solución a este problema que se añaden en la versión 16 de React.
```
Lo que nos permiten hacer es envolver las etiquetas con una etiqueta especial
```tsx
(<React.Fragment></React.Fragment>), y que a la hora de renderizar estos elementos no se
```
mostrará en el DOM.

```tsx
import { useState, Fragment } from 'react';

const App = () => {
  const [productos, setProductos] = useState(['Trípode para teléfono', 'Gafas de sol cuadradas', 'Sombrero de pescador',
'Tira LED RGB de 5m']);

const listaProductos = productos.map((producto, pos) => (
   <Fragment key={pos}>
     <p>{producto}</p>
     {pos !== productos.length - 1 && <hr/>}
   </Fragment>
))

    return (
      <div>
        {listaProductos}
      </div>
    )
}

export default App
```
En lugar de utilizar la etiqueta de React Fragment, podemos utilizar una etiqueta vacía siempre
que esta transformación esté contemplada por nuestro transpilador de TSX a JavaScript, es decir, Babel.

```tsx
import { useState } from 'react';

const App = () => {
  const [productos, setProductos] = useState(['Tripode para teléfono', 'Gafas de sol cuadradas', 'Sombrero de pescador',
'Tira LED RGB de 5m']);

const listaProductos = productos.map((producto, pos) => (
   <>
     <p>{producto}</p>
     {pos !== productos.length - 1 && <hr/>}
   </>
))

    return (
      <div>
        {listaProductos}
      </div>
    )
}

export default App
```
En la configuración de Babel se le indica con la opción de "runtime": "automatic".

/.babelrc

```tsx
[
    "@babel/preset-react",
    {
      "runtime": "automatic"
    }
]
```