# 28.4.1. Lab Usecontext

**PDF: páginas 158–161** (libro: 154–157)

---

[← Índice](README.md) | [← Anterior: 28.3. Useeffect](28-03-useEffect.md) | [Siguiente: 28.4. Usecontext →](28-04-useContext.md)

---

```tsx
En este laboratorio vamos a ver como usar el hook useContext para traducir los textos de la
```
aplicación.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial y vamos a cambiarle el nombre del proyecto a reactjs-hooks-usecontext-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Lo primero que vamos a hacer es crear el componente Context, en el que vamos a crear un
contexto de React (que exportaremos) y añadiremos un objeto con las traducciones de nuestra
aplicación en distintos idiomas.

**Archivo:** `/reactjs-hooks-usecontext-lab/src/components/Context.tsx`

```tsx
import React from 'react'

export const LangCtx = React.createContext(null)

const traducciones = {
  es: {
     bienvenida: 'Bienvenido a mi Startup'
  },
  en: {
     bienvenida: 'Welcome to my Startup'
  },
  fr: {
     bienvenida: 'Bienvenue dans ma Startup'
  }
}

const Context = () => {

return (
  <div>

        </div>
    )
}

export default Context
```
Ahora vamos a añadir este componente dentro del componente raíz de la aplicación.

**Archivo:** `/reactjs-hooks-usecontext-lab/src/components/App.tsx`

```tsx
import React, { Component } from 'react'
import Context from './Context'

class App extends Component {
  render() {
    return (
      <div>
        <Context />
      </div>
    )
  }
}

export default App
```
Ahora vamos a crearnos un componente SelectLang que tendrá un desplegable para poder mostrar
los distintos idiomas y seleccionar en cual queremos que se muestre nuestra aplicación. Este
componente recibirá como propiedades los distintos lenguajes, el lenguaje seleccionado y la
función que cambia de lenguaje.

**Archivo:** `/reactjs-hooks-usecontext-lab/src/components/SelectLang.tsx`

```tsx
import React from 'react';

const SelectLang = ({langs, onChangeLang, selectedLang}) => {
  const optionsLang = langs.map((l, pos) => <option key={pos} value={l}>{l.toUpperCase()}</option>)

    return (
      <select onChange={(e) => onChangeLang(e.target.value)} value={selectedLang}>
        {optionsLang}
      </select>
    )
}

export default SelectLang
```
Una vez que tenemos el componente, vamos a añadirlo en el componente Context, donde
añadiremos el estado que guarda el lenguaje seleccionado.

**Archivo:** `/reactjs-hooks-usecontext-lab/src/components/Context.tsx`

```tsx
import React, { useState } from 'react'
import SelectLang from './SelectLang'

export const LangCtx = React.createContext(null)

const traducciones = {
  es: {

      bienvenida: 'Bienvenido a mi Startup'
    },
    en: {
       bienvenida: 'Welcome to my Startup'
    },
    fr: {
       bienvenida: 'Bienvenue dans ma Startup'
    }
}

const Context = () => {
  const [lang, setLang] = useState('es')

    return (
      <div>
        <SelectLang langs={Object.keys(traducciones)} onChangeLang={setLang} selectedLang={lang} />
      </div>
    )
}

export default Context
```
Ahora ya deberíamos de poder ver el desplegable y cambiar el valor del lenguaje.

```tsx
Lo siguiente es crear el componente Header en el que usaremos el hook del useContext para
```
pasarle las traducciones correspondientes al lenguaje seleccionado y así mostrar el título en
distintos idiomas.

En este componente importaremos el LangCtx que hemos creado anteriormente para pasarselo al
hook y que nos devuelva el valor que nos provee el contexto, para así poder mostrarlo.

**Archivo:** `/reactjs-hooks-usecontext-lab/src/components/Header.tsx`

```tsx
import React, { useContext } from 'react'
import { LangCtx } from './Context'

const Header = () => {
  const {bienvenida} = useContext(LangCtx)

    return (
      <h1>{bienvenida}</h1>
    )
}

export default Header
```
Por último, nos faltaría envolver este componente con el Provider y pasarle el valor a través de
esta etiqueta desde el componenten Context.

**Archivo:** `/reactjs-hooks-usecontext-lab/src/components/Context.tsx`

```tsx
import React, { useState } from 'react'

import SelectLang from './SelectLang'
import Header from './Header'

export const LangCtx = React.createContext(null)

const traducciones = {
  es: {
     bienvenida: 'Bienvenido a mi Startup'
  },
  en: {
     bienvenida: 'Welcome to my Startup'
  },
  fr: {
     bienvenida: 'Bienvenue dans ma Startup'
  }
}

const Context = () => {
  const [lang, setLang] = useState('es')

    return (
      <div>
        <SelectLang langs={Object.keys(traducciones)} onChangeLang={setLang} selectedLang={lang} />
        <LangCtx.Provider value={traducciones[lang]}>
          <Header />
        </LangCtx.Provider>
      </div>
    )
}

export default Context
```
Y con lo que acabamos de hacer ya debería de cambiar el texto del header al lenguaje que hayamos
seleccionado en el desplegable.