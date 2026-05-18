# 28.3.1. Lab Useeffect

**PDF: páginas 153–156** (libro: 149–152)

---

En este laboratorio vamos a ver como crear un buscador de cocktails en el que usaremos el hook de
```tsx
useEffect para realizar las peticiones.
```
Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial y vamos a cambiarle el nombre del proyecto a reactjs-hooks-useeffect-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Una vez que tenemos el proyecto, vamos a crear un componente Autocomplete dentro de la
carpeta components.

En este componente vamos a empezar añadiendo un input que se va a encargar de guardar el texto
por el que vamos a buscar los cocktails. Y también añadiremos la lista de los cocktails que de
momento estará vacia.

**Archivo:** `/reactjs-hooks-useeffect-lab/src/components/Autocomplete.jsx`

```tsx
import React, { useState } from 'react'

const Autocomplete = () => {
  const [nombre, setNombre] = useState('');
  const [cocktails, setCocktails] = useState([]);

const listaCocktails = cocktails.map(c => <li key={c.idDrink}>{c.strDrink}</li>)

    return (
      <div>
        <input type="text" value={nombre} onChange={e => setNombre(e.target.value)} />
        <ul>
          {listaCocktails}
        </ul>
      </div>
    )
}

export default Autocomplete
```
Una vez que tenemos el estado del componente y ya estamos mostrando los elementos, vamos a
poner este componente dentro del componente App del proyecto.

**Archivo:** `/reactjs-hooks-useeffect-lab/src/components/App.jsx`

```tsx
import React, { Component } from 'react'
import Autocomplete from './Autocomplete'

class App extends Component {
  render() {
    return (
      <div>
        <Autocomplete />
      </div>
    )
  }
}

export default App
```
El siguiente paso es realizar la petición de busqueda a la API de cocktails que podemos encontrar
en https://www.thecocktaildb.com/api.php.

```tsx
Para ello, vamos a empezar añadiendo el hook del useEffect en el que añadiremos una petición
```
fetch a la API en la que pasaremos como parámetro de búsqueda el nombre que estamos
escribiendo en el campo de texto. Esta petición solo la haremos si este nombre tiene más de 3
caracteres.

Esta petición devuelve una promesa que nos da la respuesta de la que primero tendremos que
extraer los datos y después tendremos que sacar el array de bebidas, el cual guardaremos en el
estado que habíamos creado.

**Archivo:** `/reactjs-hooks-useeffect-lab/src/components/Autocomplete.jsx`

```tsx
import React, { useState, useEffect } from 'react'

const Autocomplete = () => {
  const [nombre, setNombre] = useState('');
  const [cocktails, setCocktails] = useState([]);

useEffect(() => {
   if (nombre.length > 3) {
     fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${nombre}`)
       .then(resp => resp.json())
       .then(({drinks}) => {
          setCocktails(() => drinks || [])
       })
   }
})

const listaCocktails = cocktails.map(c => <li key={c.idDrink}>{c.strDrink}</li>)

return (

        <div>
          <input type="text" value={nombre} onChange={e => setNombre(e.target.value)} />
          <ul>
            {listaCocktails}
          </ul>
        </div>
    )
}

export default Autocomplete
```
Ahora ya deberíamos de poder ver la lista con los cocktails que coinciden con el parámetro de
búsqueda que hemos puesto en el campo de texto.

Pero ahora mismo tenemos un problema que no estamos viendo, y es que no le hemos pasado una
lista de dependencias al hook, por lo que cuando cambie cualquier dato del componente, este se
ejecutará, aunque dicho cambio no le afecte a la petición. Esto lo podemos solucionar añadiendo el
nombre como dependencia, de tal forma que solo se va a ejecutar la petición a la API cuando se
vaya cambiando el nombre.

**Archivo:** `/reactjs-hooks-useeffect-lab/src/components/Autocomplete.jsx`

```tsx
import React, { useState, useEffect } from 'react'

const Autocomplete = () => {
  const [nombre, setNombre] = useState('');
  const [cocktails, setCocktails] = useState([]);

useEffect(() => {
  if (nombre.length > 3) {
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${nombre}`)
      .then(resp => resp.json())
      .then(({drinks}) => {
         setCocktails(() => drinks || [])
      })
  }
}, [nombre])

const listaCocktails = cocktails.map(c => <li key={c.idDrink}>{c.strDrink}</li>)

    return (
      <div>
        <input type="text" value={nombre} onChange={e => setNombre(e.target.value)} />
        <ul>
          {listaCocktails}
        </ul>
      </div>
    )
}

export default Autocomplete
```
El siguiente paso será seleccionar uno de los cocktails que se nos muestran para autocompletar el
input con el.

Ahora vamos a añadir una función que va a recibir el cocktail sobre el que pulsemos y se va a
setear el nombre de este en el estado.

**Archivo:** `/reactjs-hooks-useeffect-lab/src/components/Autocomplete.jsx`

```tsx
import React, { useState, useEffect } from 'react'

const Autocomplete = () => {
  const [nombre, setNombre] = useState('');
  const [cocktails, setCocktails] = useState([]);

useEffect(() => {
  if (nombre.length > 3) {
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${nombre}`)
      .then(resp => resp.json())
      .then(({drinks}) => {
         setCocktails(() => drinks || [])
      })
  }
}, [nombre])

const selectCocktail = (cocktailSeleccionado) => {
  setNombre(cocktailSeleccionado.strDrink)
}

const listaCocktails = cocktails.map(c => <li onClick={() => selectCocktail(c)} key={c.idDrink}>{c.strDrink}</li>)

    return (
      <div>
        <input type="text" value={nombre} onChange={e => setNombre(e.target.value)} />
        <ul>
          {listaCocktails}
        </ul>
      </div>
    )
}

export default Autocomplete
```
Y con esto ya tendriamos nuestro componente que autocompleta un campo con la opción
seleccionada de aquellas que se nos muestran al realizar la búsqueda.
