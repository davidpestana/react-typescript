# 24.1. Lab Context Api

**PDF: páginas 119–122** (libro: 115–118)

---

[← Índice](README.md) | [← Anterior: 24. Context Api](24-00-context-api.md) | [Siguiente: 25. Hoc →](25-00-hoc.md)

---

En este laboratorio vamos a ver como podríamos hacer que nuestra aplicación cambie entre el dark
mode y el light mode utilizando la Context API para compartir entre los componentes el tema que
se tiene que aplicar.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-context-api-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Empezaremos añadiendo en el componente raíz de la aplicación el estado y un botón para cambiar
entre ambos modos.

**Archivo:** `/reactjs-context-api-lab/src/components/App.tsx`

```tsx
import { useState } from 'react';

const App = () => {
  const [darkMode, setDarkMode] = useState(true);

    return (
      <div>
        <button type="button" onClick={() => setDarkMode(!darkMode)}>Activado {darkMode ? 'ἱ' : 'ἱ'}</button>
      </div>
    )
}

export default App
```
Ahora vamos a crear un objeto de estilos que se aplicarán dependiendo de la opción seleccionada.

**Archivo:** `/reactjs-context-api-lab/src/components/App.tsx`

```tsx
import { useState } from 'react';

const App = () => {
  const [darkMode, setDarkMode] = useState(true);
  const stylesThemeMode = darkMode ? {
    backgroundColor: 'black',
    color: 'white'
  } : {
    backgroundColor: 'white',
    color: 'black'
  }

    return (
      <div>
        <button type="button" onClick={() => setDarkMode(!darkMode)}>Activado {darkMode ? 'ἱ' : 'ἱ'}</button>
      </div>
    )
}

export default App
```
Una vez tenemos la lógica necesaria para cambiar entre el dark mode y el light mode, vamos a
crear el contexto ThemeContext con el que pasaremos el objeto con los estilos a los componentes
que lo necesiten.

Para ello importamos React y utilizamos la función de createContext. Para luego poder utilizar un
consumidor en otros componentes, tenemos que exportar el contexto.

**Archivo:** `/reactjs-context-api-lab/src/components/App.tsx`

```tsx
import React, { useState } from 'react';

export const ThemeContext = React.createContext();

const App = () => {
  const [darkMode, setDarkMode] = useState(true);
  const stylesThemeMode = darkMode ? {
    backgroundColor: 'black',
    color: 'white'
  } : {
    backgroundColor: 'white',
    color: 'black'
  }

    return (
      <div>
        <button type="button" onClick={() => setDarkMode(!darkMode)}>Activado {darkMode ? 'ἱ' : 'ἱ'}</button>
      </div>
    )
}

export default App
```
Ahora vamos a crear el componente CmpConsumidor que de momento vamos a dejar de la
siguiente forma.

**Archivo:** `/reactjs-context-api-lab/src/components/CmpConsumidor.tsx`

```tsx
import { ThemeContext } from './App';

const CmpConsumidor = () => {
  return (
    <div>
      <p>Este componente consumirá el valor del context</p>
    </div>
  )

export default CmpConsumidor;
```
Vamos a importar el nuevo componente en App y lo envolvemos con el Provider del contexto que
hemos creado, pasandole el objeto de estilos mediante el provider.

**Archivo:** `/reactjs-context-api-lab/src/components/App.tsx`

```tsx
import React, { useState } from 'react';
import CmpConsumidor from './CmpConsumidor';

export const ThemeContext = React.createContext();

const App = () => {
  const [darkMode, setDarkMode] = useState(true);
  const stylesThemeMode = darkMode ? {
    backgroundColor: 'black',
    color: 'white'
  } : {
    backgroundColor: 'white',
    color: 'black'
  }

return (
  <div>
    <button type="button" onClick={() => setDarkMode(!darkMode)}>Activado {darkMode ? 'ἱ' : 'ἱ'}</button>

          <ThemeContext.Provider value={stylesThemeMode}>
            <CmpConsumidor />
          </ThemeContext.Provider>
        </div>
    )
}

export default App
```
Al envolver con el Provider el componente CmpConsumidor, tanto este como cualquiera que se
renderice dentro de el (sus descendientes) podrán pedir el valor del contexto.

Por último, vamos a añadir el Consumer dentro del componente CmpConsumidor para recibir el
objeto con los estilos y así aplicarlos sobre las etiquetas de HTML que va a pintar.

Como children del componente Consumer pasaremos una función que va a devolver los elementos
que queremos pintar. En esta función recibimos los estilos como parámetro y ya podríamos
utilizarlos.

**Archivo:** `/reactjs-context-api-lab/src/components/CmpConsumidor.tsx`

```tsx
import { ThemeContext } from './App';

const CmpConsumidor = () => {
  return (
    <ThemeContext.Consumer>

           {(styles) => (
              <div style={styles}>
                <p>Este componente consumirá el valor del context</p>
              </div>
           )}
         </ThemeContext.Consumer>
     )
}

export default CmpConsumidor;
```