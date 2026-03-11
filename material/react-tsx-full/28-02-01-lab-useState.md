# 28.2.1. Lab Usestate

**PDF: páginas 148–150** (libro: 144–146)

---

[← Índice](README.md) | [← Anterior: 28.1. Reglas Hooks](28-01-reglas-hooks.md) | [Siguiente: 28.2. Usestate →](28-02-useState.md)

---

En este laboratorio vamos a ver como crear un componente contador y mantener su estado con el
```tsx
hook useState.
```
Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial y vamos a cambiarle el nombre del proyecto a reactjs-hooks-usestate-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Una vez que tenemos el proyecto levantado, vamos a crear un componente Contador funcional
dentro de la carpeta components.

**Archivo:** `/reactjs-hooks-usestate-lab/src/components/Contador.tsx`

```tsx
import React from 'react'

const Contador = () => {
  return (
    <div>
      <button type="button">-</button>
      <span>Cuenta: </span>
      <button type="button">+</button>
    </div>
  )
}

export default Contador;

Necesitamos añadir un estado en este componente para llevar la cuenta, y aquí es donde vamos a
usar el hook useState que primero vamos a importar desde react.
```
**Archivo:** `/reactjs-hooks-usestate-lab/src/components/Contador.tsx`

```tsx
import React, { useState } from 'react'

const Contador = () => {
  return (
    <div>
      <button type="button">-</button>
      <span>Cuenta: </span>
      <button type="button">+</button>
    </div>

    )
}

export default Contador;

Una vez importado, vamos a llamar a la función useState pasandole como parámetro el valor
```
inicial que queremos usar para el estado, en este caso le pasaremos 0 como valor inicial de la
cuenta.

Además, esta función devuelve un array de dos posiciones, donde la primera es el valor actual y la
segunda una función para cambiar el estado.

**Archivo:** `/reactjs-hooks-usestate-lab/src/components/Contador.tsx`

```tsx
import React, { useState } from 'react'

const Contador = () => {
  const [cuenta, setCuenta] = useState(0);

    return (
      <div>
        <button type="button">-</button>
        <span>Cuenta: </span>
        <button type="button">+</button>
      </div>
    )
}

export default Contador;
```
El siguiente paso es mostrar el valor actual de la cuenta en el span, como venimos haciendo
durante el curso.

**Archivo:** `/reactjs-hooks-usestate-lab/src/components/Contador.tsx`

```tsx
import React, { useState } from 'react'

const Contador = () => {
  const [cuenta, setCuenta] = useState(0);

    return (
      <div>
        <button type="button">-</button>
        <span>Cuenta: {cuenta}</span>
        <button type="button">+</button>
      </div>
    )
}

export default Contador;
```
Antes de continuar con este componente, vamos a comprobar que de momento ya se está
mostrando la cuenta, y para ello, vamos a añadir el componente de Contador, dentro del App.

**Archivo:** `/reactjs-hooks-usestate-lab/src/components/App.tsx`

```tsx
import React, { Component } from 'react'
import Contador from './Contador';

class App extends Component {
  render() {
    return (
      <div>
        <Contador />
      </div>
    )
  }
}

export default App
```
Ahora ya deberíamos de poder ver el contador en nuestro navegador en http://localhost:8080.

Lo siguiente es añadir la funcionalidad a los botones para modificar el estado de la cuenta.
Tenemos que usar el método setCuenta y pasarle como parámetro el nuevo valor de la cuenta.

**Archivo:** `/reactjs-hooks-usestate-lab/src/components/Contador.tsx`

```tsx
import React, { useState } from 'react'

const Contador = () => {
  const [cuenta, setCuenta] = useState(0);

    return (
      <div>
        <button type="button" onClick={() => setCuenta(cuenta-1)}>-</button>
        <span>Cuenta: {cuenta}</span>
        <button type="button" onClick={() => setCuenta(cuenta+1)}>+</button>
      </div>
    )
}

export default Contador;
```
Ahora ya deberíamos de poder modificar la cuenta sin problemas.