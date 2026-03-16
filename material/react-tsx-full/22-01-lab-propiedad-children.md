# 22.1. Lab Propiedad Children

**PDF: páginas 110–114** (libro: 106–110)

---

[← Índice](README.md) | [← Anterior: 22. Propiedad Children](22-00-propiedad-children.md) | [Siguiente: 23. Fragments →](23-00-fragments.md)

---

En este laboratorio vamos a ver como utilizar la propiedad children en un componente que se
puede colapsar.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-children-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Empezaremos creando el componente Acordeon que se va a componer de una cabecera que
siempre se va a mostrar y el contenido que es aquello que queremos ocultar o expandir según
pulsemos sobre la cabecera.

**Archivo:** `/reactjs-children-lab/src/components/Acordeon.tsx`

```tsx
const Acordeon = () => {
  return (
    <div>
      <div>
        <h3>Aquí va el título</h3>
      </div>
      <div>

Aquí va el contenido
      </div>
    </div>
  )
}

export default Acordeon
```
Tanto el título como el contenido del acordeón vendrán desde los componentes superiores, por
tanto los vamos a recibir como propiedades.

Como el contenido no tiene porque mostrarse siempre con los mismos elementos de HTML, sino
que una vez podemos querer mostrar una lista, mientras que otra solo un párrafo de información,
vamos a pintar aquí aquello que pasen entre las etiquetas de apertura y cierre del componente. Es
decir, usaremos la propiedad children para indicar cual es el contenido del Acordeon.

Otra propiedad que vamos a recibir es la que indica si el contenido tiene que aparecer expandido o
no al crear el componente.

**Archivo:** `/reactjs-children-lab/src/components/Acordeon.tsx`

```tsx
const Acordeon = ({ children, titulo, cerrado = true }) => {
  return (
    <div>
      <div>
        <h3>{titulo}</h3>
      </div>
      <div>
        {children}
      </div>
    </div>
  )
}

export default Acordeon
```
Ahora vamos a añadir un estado para indicarle al componente si tiene que estar colapsado o
expandido.

**Archivo:** `/reactjs-children-lab/src/components/Acordeon.tsx`

```tsx
import { useState } from 'react';

const Acordeon = ({ children, titulo, cerrado = true }) => {
  const [estaCerrado, setEstaCerrado] = useState(null);

    return (
      <div>
        <div>
          <h3>{titulo}</h3>
        </div>
        <div>
          {children}
        </div>
      </div>
    )
}

export default Acordeon
```
Como podemos indicarle desde la propiedad cerrado el estado inicial y la propiedad puede
cambiar desde el exterior, vamos a utilizar el hook de useEffect para inicializar y sincronizar el

estado con esa propiedad.

**Archivo:** `/reactjs-children-lab/src/components/Acordeon.tsx`

```tsx
import { useState, useEffect } from 'react';

const Acordeon = ({ children, titulo, cerrado = true }) => {

const [estaCerrado, setEstaCerrado] = useState(null);

useEffect(() => {
  setEstaCerrado(cerrado);
}, [cerrado]);

    return (
      <div>
        <div>
          <h3>{titulo}</h3>
        </div>
        <div>
          {children}
        </div>
      </div>
    )
}

export default Acordeon
```
También tenemos que añadir el evento click sobre la cabecera para poder expandir y colapsar el
contenido.

**Archivo:** `/reactjs-children-lab/src/components/Acordeon.tsx`

```tsx
import { useState, useEffect } from 'react';

const Acordeon = ({ children, titulo, cerrado = true }) => {
  const [estaCerrado, setEstaCerrado] = useState(null);

useEffect(() => {
  setEstaCerrado(cerrado);
}, [cerrado]);

    return (
      <div>
        <div onClick={() => setEstaCerrado(!estaCerrado)}>
          <h3>{titulo}</h3>
        </div>
        <div>
          {children}
        </div>
      </div>
    )
}

export default Acordeon
```
Para que se vea un poco mejor el Acordeon vamos a crear un archivo de estilo en el que
aprovecharemos para añadir las clases de abierto y cerrado que se encargan de modificar la

altura del contenido para que se colapse o se expanda.

**Archivo:** `/reactjs-children-lab/src/style.css`

.acordeon {
```tsx
  border: 1px solid black;
  border-radius: 5px;
}

.acordeon-heading {
  text-align: center;
  border-bottom: 2px solid black;
  cursor: pointer;
}

.acordeon-content {
  overflow: hidden;
}
.acordeon-content.cerrado {
  height: 0;
}

.acordeon-content.abierto {
  height: auto;
  padding: 20px;
}
```
Ahora importamos el archivo de estilos y le añadimos a nuestro componente las clases anteriores
en sus elementos correspondientes.

**Archivo:** `/reactjs-children-lab/src/components/Acordeon.tsx`

```tsx
import { useState, useEffect } from 'react';
import './Acordeon.css';

const Acordeon = ({ children, titulo, cerrado = true }) => {
  const [estaCerrado, setEstaCerrado] = useState(null);

useEffect(() => {
  setEstaCerrado(cerrado);
}, [cerrado]);

return (
  <div className="acordeon">
    <div className="acordeon-heading" onClick={() => setEstaCerrado(!estaCerrado)}>
      <h3>{titulo}</h3>
    </div>
    <div className={'acordeon-content ' + (estaCerrado ? 'cerrado' : 'abierto')}>
      {children}
    </div>

        </div>
    )
}

export default Acordeon
```
Con esto ya tenemos nuestro Acordeon finalizado.

Vamos a utilizarlo en el componente App para mostrar varias cosas que se puedan colapsar.

**Archivo:** `/reactjs-children-lab/src/components/App.tsx`

```tsx
import Acordeon from './Acordeon';

const App = () => {
  return (
    <div>
      <Acordeon titulo="Una lista de productos">
         <ul>
           <li>Albahaca</li>
           <li>Queso parmesano</li>
           <li>Pechuga de pollo</li>
           <li>Tomates</li>
         </ul>
      </Acordeon>
      <Acordeon titulo="Librería JS" cerrado={false}>
         <div>
           <h4>¿Que es React?</h4>
           <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/React.svg/300px-React.svg.png" alt="Logo de

React"/>
           <p>React es una librería de JS que permite pintar interfaces de usuario...</p>
         </div>
      </Acordeon>
    </div>
  )
}

export default App
```
