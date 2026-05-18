# 28.8.1. Lab Crear Hook

**PDF: páginas 183–186** (libro: 179–182)

---

[← Índice](README.md) | [← Anterior: 28.7. Usereducer](28-07-useReducer.md) | [Siguiente: 28.8. Crear Hook →](28-08-crear-hook.md)

---

En este laboratorio vamos a ver como crear nuestro propio hook para mantener los campos de un
formulario.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial y vamos a cambiarle el nombre del proyecto a reactjs-hooks-custom-hook-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Vamos a empezar creando un componente Form dentro de la carpeta components en el que
añadiremos un campo de texto y un parrafor para mostrar si el campo es válido o no.

**Archivo:** `/reactjs-hooks-custom-hook-lab/src/components/Form.tsx`

```tsx
import React from 'react'

const Form = () => {
  return (
    <div>
      <input type="text" />
      <p>Válido o inválido</p>
    </div>
  )
}

export default Form
```
Una vez que tenemos el componente, vamos a añadirlo a nuestra aplicación, dentro del
componente App.

**Archivo:** `/reactjs-hooks-custom-hook-lab/src/components/App.tsx`

```tsx
import React, { Component } from 'react'
import Form from './Form'

class App extends Component {
  render() {
    return (
      <div>
        <Form />
      </div>
    )

    }
}

export default App
```
Ahora ya deberíamos de ver el componente en el navegador, pero no tiene ninguna funcionalidad.

Lo siguiente que vamos a hacer es empezar a crear nuestro propio hook en hooks/index.js.

El hook es una función que vamos a llamar useInputForm y exportaremos para usarlo en nuestra
aplicación.

**Archivo:** `/reactjs-hooks-custom-hook-lab/src/hooks/index.js`

```tsx
export const useInputForm = () => {
```
Dentro de la función vamos a crear un estado que inicializaremos con un valor que vamos a recibir
como parámetro en la función del hook.

**Archivo:** `/reactjs-hooks-custom-hook-lab/src/hooks/index.js`

```tsx
import { useState } from 'react';

export const useInputForm = (initValue) => {
  const [value, setValue] = useState(initValue)
}
```
Con esto ya tendríamos el valor de cada input, pero para poder pasarlo al input correspondiente
vamos a devolver:

- El value, que añadiremos como valor del input

- Y un método onChange, que se encargará de cambiar el estado cuando se detecte dicho evento
en el input.

**Archivo:** `/reactjs-hooks-custom-hook-lab/src/hooks/index.js`

```tsx
import { useState } from 'react';

export const useInputForm = (initValue, regexps) => {
  const [value, setValue] = useState(initValue)

return {
```
value,
```tsx
      onChange: (e) => setValue(e.target.value)
    }
}
```
Ahora vamos a añadir estas propiedades al campo de texto que tenemos en el componente, y lo
primero que hay que hacer es importar el hook y ejecutarlo para obtener las propiedades que
hemos devuelto.

**Archivo:** `/reactjs-hooks-custom-hook-lab/src/components/Form.tsx`

```tsx
import React from 'react'
import { useInputForm } from '../hooks'

const Form = () => {
  const hexadecimal = useInputForm('#ffffff');

    return (
      <div>
        <input type="text" value={hexadecimal.value} onChange={hexadecimal.onChange} />
        <p>Válido o inválido</p>
      </div>
    )
}

export default Form
```
Con esto ya deberíamos de poder modificar el valor del campo de texto.

Pero no nos vamos a quedar aquí, ahora vamos a añadir algunas validaciones al campo. Estas
validaciones las pasaremos como segundo parámetro del hook. Dentro de nuestro hook usaremos
```tsx
useEffect para pasar todas las validaciones cada vez que el value cambie de valor.
```
Tenemos que añadir un nuevo estado para controlar si el campo es válido o no lo es. Este valor lo
vamos a devolver para poder mostrar el mensaje correcto en el campo de texto.

**Archivo:** `/reactjs-hooks-custom-hook-lab/src/hooks/index.js`

```tsx
import { useState, useEffect } from 'react';

export const useInputForm = (initValue, regexps) => {
  const [value, setValue] = useState(initValue)
  const [isValid, setValid] = useState(false)

useEffect(() => {
  const valid = regexps.every(r => {
     const rexp = new RegExp(r);
     return rexp.test(value);
  })
  setValid(valid)
}, [value])

return {
```
value,
```tsx
onChange: (e) => setValue(e.target.value),
```
isValid
```tsx
    }
}
```
Una vez que tenemos el hook, vamos a pasar las validaciones a nuestro hook, y mostraremos el
mensaje que indica si las pasa o no.

**Archivo:** `/reactjs-hooks-custom-hook-lab/src/components/Form.tsx`

```tsx
import React from 'react'
import { useInputForm } from '../hooks'

const Form = () => {
  const hexadecimal = useInputForm('#ffffff', ['^#.*$', '^#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$']);

    return (
      <div>
        <input type="text" value={hexadecimal.value} onChange={hexadecimal.onChange} />
        <p>{ hexadecimal.isValid ? 'Válido' : 'Inválido' }</p>
      </div>
    )
}

export default Form
```
Una vez añadidas las validaciones, ya debe de mostrarnos si el valor introducido es válido.