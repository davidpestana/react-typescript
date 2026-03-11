# 28.5.1. Lab Usememo

**PDF: páginas 163–167** (libro: 159–163)

---

[← Índice](README.md) | [← Anterior: 28.4. Usecontext](28-04-useContext.md) | [Siguiente: 28.5. Usememo →](28-05-useMemo.md)

---

En este laboratorio vamos a ver como usar el hook de useMemo para crear una propiedad
nombreCompleto formada a partir de las propiedades nombre y apellido del estado y que solo se
calcule cuando cambie alguna de estas dos propiedades.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial y vamos a cambiarle el nombre del proyecto a reactjs-hooks-usememo-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Lo siguiente es crear el componente Persona en el que vamos a añadir tres estados (nombre,
apellido y email), los vamos a mostrar y añadiremos también tres inputs para poder cambiar estos
datos.

**Archivo:** `/reactjs-hooks-usememo-lab/src/components/Persona.tsx`

```tsx
import React, { useState } from 'react'

const Persona = () => {
  const [nombre, setNombre] = useState('Charly')
  const [apellido, setApellido] = useState('Falco')
  const [email, setEmail] = useState('cfalco@gmail.com')

    return (
      <div>
        <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)}/>
        <input type="text" value={apellido} onChange={(e) => setApellido(e.target.value)}/>
        <input type="text" value={email} onChange={(e) => setEmail(e.target.value)}/>
        <hr/>
        <p>{nombre}</p>
        <p>{apellido}</p>
        <p>{email}</p>
      </div>
    )
}

export default Persona
```
Una vez que lo tenemos, vamos a añdadir este componente dentro del componente raíz de la
aplicación para mostrarlo.

**Archivo:** `/reactjs-hooks-usememo-lab/src/components/App.tsx`

```tsx
import React, { Component } from 'react'
import Persona from './Persona'

class App extends Component {
  render() {
    return (
      <div>
        <Persona />
      </div>
    )
  }
}

export default App
```
Lo siguiente que vamos a hacer es crear una función que va a calcular el nombre completo a partir
de las propiedades nombre y apellido del estado.

**Archivo:** `/reactjs-hooks-usememo-lab/src/components/Persona.tsx`

```tsx
import React, { useState } from 'react'

const Persona = () => {
  const [nombre, setNombre] = useState('Charly')
  const [apellido, setApellido] = useState('Falco')
  const [email, setEmail] = useState('cfalco@gmail.com')

const nombreCompleto = () => {
  return <p>{nombre} {apellido}</p>
}

    return (
      <div>
        <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)}/>
        <input type="text" value={apellido} onChange={(e) => setApellido(e.target.value)}/>
        <input type="text" value={email} onChange={(e) => setEmail(e.target.value)}/>
        <hr/>
        <p>{nombreCompleto()}</p>
        <p>{email}</p>
      </div>
    )
}

export default Persona
```
Ahora deberíamos de ver los valores del estado y poder cambiarlos, pero todavía hay algo que
podemos mejorar. ¿Que pasa si modificamos la propiedad del email? Vamos a mostrar por consola
un mensaje dentro de la función que calcula el nombre completo, para ver que está ocurriendo.

**Archivo:** `/reactjs-hooks-usememo-lab/src/components/Persona.tsx`

```tsx
import React, { useState } from 'react'

const Persona = () => {
  const [nombre, setNombre] = useState('Charly')
  const [apellido, setApellido] = useState('Falco')
  const [email, setEmail] = useState('cfalco@gmail.com')

const nombreCompleto = () => {
  console.log('nombreCompleto')
  return <p>{nombre} {apellido}</p>
}

     return (
       <div>
         <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)}/>
         <input type="text" value={apellido} onChange={(e) => setApellido(e.target.value)}/>
         <input type="text" value={email} onChange={(e) => setEmail(e.target.value)}/>
         <hr/>
         <p>{nombreCompleto()}</p>
         <p>{email}</p>
       </div>
     )
}

export default Persona
```
Si modificamos el email, vemos que se va calculando también el nombre completo, aunque no
hayan cambiado ni el nombre ni el apellido, y esto es algo que podríamos evitar con el hook
useMemo.

Vamos a meter dentro de este hook la función de nombreCompleto, y como este hook nos devuelve
el valor de la función ya memorizado vamos a dejar de ejecutar la función dentro de nuestro código
TSX.

**Archivo:** `/reactjs-hooks-usememo-lab/src/components/Persona.tsx`

```tsx
import React, { useState, useMemo } from 'react'

const Persona = () => {
  const [nombre, setNombre] = useState('Charly')
  const [apellido, setApellido] = useState('Falco')
  const [email, setEmail] = useState('cfalco@gmail.com')

const nombreCompleto = useMemo(() => {
   console.log('nombreCompleto')
   return <p>{nombre} {apellido}</p>
})

return (

        <div>
          <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)}/>
          <input type="text" value={apellido} onChange={(e) => setApellido(e.target.value)}/>
          <input type="text" value={email} onChange={(e) => setEmail(e.target.value)}/>
          <hr/>
          <p>{nombreCompleto}</p>
          <p>{email}</p>
        </div>
    )
}

export default Persona
```
Ahora si volvemos a probar a modificar el campo, vemos que sigue ocurriendo lo mismo. El
problema está en que no le estamos indicando cuando tiene que ejecutar la función para volver a
calcular el nuevo valor, y por tanto la está ejecutando todas las veces que se renderiza el
componente.

Para solucionarlo, tenemos que pasarle una lista de dependencias como segundo parámetro para
indicarle que solo tiene que volver ejecutarla cuando alguna de esas dependencias haya cambiado.
Por tanto, en este caso, vamos a pasarle un array con nombre y apellido como dependencias.

**Archivo:** `/reactjs-hooks-usememo-lab/src/components/Persona.tsx`

```tsx
import React, { useState, useMemo } from 'react'

const Persona = () => {
  const [nombre, setNombre] = useState('Charly')
  const [apellido, setApellido] = useState('Falco')
  const [email, setEmail] = useState('cfalco@gmail.com')

const nombreCompleto = useMemo(() => {
  console.log('nombreCompleto')
  return <p>{nombre} {apellido}</p>
}, [nombre, apellido])

    return (
      <div>
        <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)}/>
        <input type="text" value={apellido} onChange={(e) => setApellido(e.target.value)}/>
        <input type="text" value={email} onChange={(e) => setEmail(e.target.value)}/>
        <hr/>
        <p>{nombreCompleto}</p>
        <p>{email}</p>
      </div>
    )
}

export default Persona

Ahora ya podemos observar que cuando cambiamos el email, no se pasa por la función
```
nombreCompleto, sino que usa el valor memorizado la primera vez, y en el caso de que
cambiemos el nombre o el apellido, vuelve a ejecutar la función u memoriza el nuevo valor para
evitar tener que hacerlo en los siguientes renders.