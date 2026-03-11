# 10. Componente sin TSX

**PDF: páginas 37–38** (libro: 33–34)

---

[← Índice](README.md) | [← Anterior: 9. Qué es TSX](09-00-que-es-jsx.md) | [Siguiente: 11. Componentes →](11-00-componentes.md)

---

## Componente sin TSX

Hemos visto anteriormente un poco de TSX, la sintaxis que se utiliza para indicar que tienen que
renderizar los componentes.

Al final el TSX se transforma en JavaScript, por lo que también podríamos escribir el código de
nuestros componentes en JavaScript completamente.

Entonces, ¿cómo se podría hacer esto?

```tsx
Pues utilizando la función createElement que se importa de React.

import React from 'react';

const App = () => {
  return React.createElement(
    'div',
    {id: 'main'},
    React.createElement(
      'h1',
      {className: 'titulo'},
      'Hola mundo!!!'
    )
  )
}
```
En la versión 17 de React ya no es necesario importar React, algo obligatorio hasta ahora porque
```tsx
cuando se transpila el código de TSX a JavaScript es necesario utilizar React.createElement y por tanto si
no se importa no podemos llegar a llamar a la función de createElement.
```
Esto podemos verlo desde https://babeljs.io/repl.

Ahora utilizan otro módulo (react/jsx-runtime) para realizar esta transformación y Babel lo
importará automáticamente a la hora de realizar la transpilación.

Pero si quisieramos crear los componentes con JavaScript en lugar de TSX, ahora el código quedaría como
podemos ver a continuación:

```tsx
import { jsx } from 'react/jsx-runtime';

const App = () => {
  return jsx(
    'div',
    {
      id: 'main',
      children: jsx(
        'h1',
        {
           className: 'titulo',

                    children: 'Hola mundo!!!'
                }
            )
        }
    )
}
```
Como podemos ver con los ejemplos de código de arriba, crear aplicaciones web en React sin
utilizar TSX se vuelve muy complejo.