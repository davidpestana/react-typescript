# 31.12. Lab React Router

**PDF: páginas 230–242** (libro: 226–242)

---

[← Índice](README.md) | [← Anterior: 31.11. Query Params](31-11-query-params.md)

---

En este laboratorio vamos a ver como utilizar la librería de React Router con todas sus
funcionalidades.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-react-router-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Necesitaremos instalar la dependencia de React Router en nuestro proyecto. Para ello, vamos a
lanzar el comando:

```tsx
$ npm install react-router-dom
```

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```

Vamos a empezar por crear dos componentes iniciales dentro de la carpeta components, uno al
que vamos a llamar Inicio y otro NuevoUsuario.

**Archivo:** `/reactjs-react-router-lab/src/components/Inicio.tsx`

```tsx
const Inicio = () => {
  return (
    <div>
      <h2>Inicio</h2>
    </div>
  )
}

export default Inicio
```

**Archivo:** `/reactjs-react-router-lab/src/components/NuevoUsuario.tsx`

```tsx
const NuevoUsuario = () => {
  return (
    <div>
      <h2>Nuevo usuario</h2>
    </div>
  )
}

export default NuevoUsuario
```

Una vez que tenemos nuestros dos primeros componentes, vamos a añadir las rutas iniciales para
poder navegar entre ellos. En el componente App vamos a añadir los componentes Route para
definir las rutas y que aquellos componentes que se tienen que mostrar.

**Archivo:** `/reactjs-react-router-lab/src/components/App.tsx`

```tsx
import { Routes, Route } from 'react-router-dom';
import Inicio from './Inicio';
import NuevoUsuario from './NuevoUsuario';

const App = () => {
  return (
    <div>
      <h1>React Router v6</h1>

          <Routes>
            <Route path="/" element={<Inicio />} />
            <Route path="/nuevo-usuario" element={<NuevoUsuario />} />
          </Routes>
        </div>
    )
}

export default App
```

Si probamos a entrar en las siguientes dos URLs podremos ver que los componentes se pintan
correctamente:

- http://localhost:8080

- http://localhost:8080/nuevo-usuario

Vamos a añadir un par de enlaces para poder cambiar entre estas dos rutas sin tener que
escribirlas a mano en la barra de direcciones del navegador.

Para ello vamos a crearnos un componente nuevo Header en el que pondremos dos enlaces que
apuntarán a las dos rutas que hemos definido.

**Archivo:** `/reactjs-react-router-lab/src/components/Header.tsx`

```tsx
const Header = () => {
  return (
    <div>
      <a href="/">Inicio</a> |
      <a href="/nuevo-usuario">Nuevo usuario</a>
    </div>
  )
}

export default Header
```

Tenemos que importar y usar este componente en nuestro App para poder verlo en nuestra
aplicación y así poder pulsar sobre los enlaces para navegar entre las rutas.

**Archivo:** `/reactjs-react-router-lab/src/components/App.tsx`

```tsx
import { Routes, Route } from 'react-router-dom';
import Header from './Header';
import Inicio from './Inicio';
import NuevoUsuario from './NuevoUsuario';

const App = () => {
  return (
    <div>
      <h1>React Router v6</h1>
      <Header />

          <Routes>
            <Route path="/" element={<Inicio />} />
            <Route path="/nuevo-usuario" element={<NuevoUsuario />} />
          </Routes>
        </div>
    )
}

export default App
```

Si probamos a cambiar entre las distintas páginas de la aplicación pulsando los enlaces vemos que
funciona correctamente, pero con un pequeño pero… La página se refresca cada vez que
cambiamos de ruta. Esto lo vamos a solucionar cambiando las etiquetas a por componentes Link en
el componente Header.

**Archivo:** `/reactjs-react-router-lab/src/components/Header.tsx`

```tsx
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <div>
      <Link to="/">Inicio</Link> |
      <Link to="/nuevo-usuario">Nuevo usuario</Link>
    </div>
  )
}

export default Header
```

Ahora ya lo tenemos solucionado, ya no se refresca la página, por lo que no perderemos el estado

de la aplicación que no se haya llegado a guardar en algún sitio.

El siguiente paso es ir al componente NuevoUsuario y añadir un botón que navegue
automáticamente a la página de inicio cuando se guarden los datos del formulario (algo que vamos
a simular con un setTimeout).

**Archivo:** `/reactjs-react-router-lab/src/components/NuevoUsuario.tsx`

```tsx
const NuevoUsuario = () => {

const guardar = (e) => {

    return (
      <div>
        <h2>Nuevo usuario</h2>
        <button onClick={guardar}>Crear usuario</button>
      </div>
    )
}

export default NuevoUsuario
```

Para navegar desde el código, vamos a utilizar la función navigate que nos devuelve el hook de
useNavigate. Por tanto vamos a poner esta llamada dentro de un setTimeout para que la
navegación no sea inmediata al igual que ocurriría si estuviesemos haciendo una petición POST
para guardar los datos en una BBDD.

**Archivo:** `/reactjs-react-router-lab/src/components/NuevoUsuario.tsx`

```tsx
import { useNavigate } from 'react-router-dom'

const NuevoUsuario = () => {
  const navigate = useNavigate()

const guardar = (e) => {
  setTimeout(() => {
    navigate('/')
  }, 2000)
}

    return (
      <div>
        <h2>Nuevo usuario</h2>
        <button onClick={guardar}>Crear usuario</button>
      </div>
    )
}

export default NuevoUsuario
```

Ahora ya podemos pulsar el botón y comprobar que cuando pasan 2 segundos, nos vamos hasta la
página inicial.

Vamos a cambiar un poco las rutas de la aplicación, y vamos a empezar por cambiar la ruta inicial
por /usuarios ya que es lo que vamos a mostrar al pintar el componente Inicio.

**Archivo:** `/reactjs-react-router-lab/src/components/App.tsx`

```tsx
import { Routes, Route } from 'react-router-dom';
import Header from './Header';
import Inicio from './Inicio';
import NuevoUsuario from './NuevoUsuario';

const App = () => {
  return (
    <div>
      <h1>React Router v6</h1>
      <Header />

          <Routes>
            <Route path="/usuarios" element={<Inicio />} />
            <Route path="/nuevo-usuario" element={<NuevoUsuario />} />
          </Routes>
        </div>
    )
}

export default App
```

Con este cambio nuestros enlaces han dejado de apuntar a la nueva ruta, y por tanto cuando vamos
a la ruta / no vemos nada salvo el menú de navegación. Esto lo vamos a solucionar haciendo que
cuando se pinte la ruta inicial, se haga una navegación a la ruta /usuarios.

Para realizar esto vamos a utilizar el componente Navigate de React Router que vamos usar como
elemento del componente Route. Le vamos a pasar la propiedad replace con un valor true para
que esta ruta intermedia no quede en el historial, sino que la reemplace por aquella a la que vamos
a navegar.

**Archivo:** `/reactjs-react-router-lab/src/components/App.tsx`

```tsx
import { Routes, Route, Navigate } from 'react-router-dom';
import Header from './Header';
import Inicio from './Inicio';
import NuevoUsuario from './NuevoUsuario';

const App = () => {
  return (
    <div>

<h1>React Router v6</h1>
<Header />

          <Routes>
            <Route path="/usuarios" element={<Inicio />} />
            <Route path="/nuevo-usuario" element={<NuevoUsuario />} />
            <Route path="/" element={<Navigate to="/usuarios" replace={true} />} />
          </Routes>
        </div>
    )
}

export default App
```

Aunque esto corrige el problema de los enlaces que van hasta /, no es la solución
definitiva, tendríamos que cambiar las rutas para evitar esa redirección. La
redirección solo debería de ejecutarse cuando entramos a la página inicial desde la
barra de navegación.

Una vez tenemos esto, vamos a hacer que en el componente Inicio se cargue una lista de usuarios
para mostrarlos en nuestra aplicación. Estos datos los vamos a obtener de la API de
jsonplaceholder.

Por tanto, nos vamos al componente de Inicio, donde vamos a añadir como estado un array vacío
que luego rellenaremos con los datos que vengan de la API.

**Archivo:** `/reactjs-react-router-lab/src/components/Inicio.tsx`

```tsx
import { useState } from 'react';

const Inicio = () => {
  const [usuarios, setUsuarios] = useState([])

const listaUsuarios = usuarios.map(u => (
   <li key={u.id}>
     <span>{u.username}</span>
   </li>
))

    return (
      <div>
        <h2>Inicio</h2>
        <ul>
          {listaUsuarios}
        </ul>
      </div>
    )
}

export default Inicio
```

Ahora dentro del useEffect vamos a realizar la petición GET a
http://jsonplaceholder.typicode.com/users para obtener la lista de usuarios y guardarla dentro del
estado. Como esta petición solo querremos hacerla una vez, vamos a pasarle al useEffect como lista
de dependencias un array vacío.

**Archivo:** `/reactjs-react-router-lab/src/components/Inicio.tsx`

```tsx
import { useEffect, useState } from 'react';

const Inicio = () => {
  const [usuarios, setUsuarios] = useState([])

useEffect(() => {
  fetch('http://jsonplaceholder.typicode.com/users')
    .then(resp => resp.json())
    .then(usuarios => setUsuarios(usuarios))
}, [])

const listaUsuarios = usuarios.map(u => (
   <li key={u.id}>
     <span>{u.username}</span>
   </li>
))

    return (
      <div>
        <h2>Inicio</h2>
        <ul>
          {listaUsuarios}
        </ul>
      </div>
    )
}

export default Inicio
```

Con esto ya deberíamos de ver una lista de nombres de usuarios en la página inicial. El siguiente
paso es poder ver más en detalle los datos de cada usuario, por lo que vamos a añadir una nueva
ruta, pero esta vez con parámetros.

Antes de añadir la ruta, vamos a añadir por cada usuario un enlace a la nueva ruta que vamos a
añadir. Para ello vamos a utilizar el componente Link y pondremos como valor de la propiedad to
el path /usuarios/ seguido del identificador de cada uno de ellos.

**Archivo:** `/reactjs-react-router-lab/src/components/Inicio.tsx`

```tsx
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const Inicio = () => {
  const [usuarios, setUsuarios] = useState([])

useEffect(() => {
  fetch('http://jsonplaceholder.typicode.com/users')
    .then(resp => resp.json())
    .then(usuarios => setUsuarios(usuarios))
}, [])

const listaUsuarios = usuarios.map(u => (
   <li key={u.id}>
     <span>{u.username}</span>
     <Link to={'/usuarios/' + u.id}>Ver + info</Link>
   </li>
))

    return (
      <div>
        <h2>Inicio</h2>
        <ul>
          {listaUsuarios}
        </ul>
      </div>
    )
}

export default Inicio
```

Ahora vamos a crear un nuevo componente Usuario en el que mostraremos la información de un
usuario en concreto.

**Archivo:** `/reactjs-react-router-lab/src/components/Usuario.tsx`

```tsx
const Usuario = () => {
  return (
    <div>
      <h3>Usuario con ID: ...</h3>
    </div>
  )
}

export default Usuario
```

Ahora que tenemos el componente, vamos a añadir la nueva ruta /usuarios/:usuarioId en el
componente App.

**Archivo:** `/reactjs-react-router-lab/src/components/App.tsx`

```tsx
import { Routes, Route, Navigate } from 'react-router-dom';

import Header from './Header';
import Inicio from './Inicio';
import NuevoUsuario from './NuevoUsuario';
import Usuario from './Usuario';

const App = () => {
  return (
    <div>
      <h1>React Router v6</h1>
      <Header />

          <Routes>
            <Route path="/usuarios" element={<Inicio />} />
            <Route path="/usuarios/:usuarioId" element={<Usuario />} />
            <Route path="/nuevo-usuario" element={<NuevoUsuario />} />
            <Route path="/" element={<Navigate to="/usuarios" replace={true} />} />
          </Routes>
        </div>
    )
}

export default App
```

Si pulsamos sobre cualquier enlace de los usuarios deberíamos ver el componente Usuario que
acabamos de crear, pero todavía nos falta una cosa. Tenemos que obtener de alguna forma el
identificador de la ruta para poder hacer una petición a la API y así mostrar los datos de este
usuario.

Aquí usaremos el hook de useParams del que vamos a extraer el usuarioId y que de momento
vamos a mostrar en el componente.

**Archivo:** `/reactjs-react-router-lab/src/components/Usuario.tsx`

```tsx
import { useParams } from 'react-router-dom';

const Usuario = () => {
  const { usuarioId } = useParams()

    return (
      <div>
        <h3>Usuario {usuarioId}</h3>
      </div>
    )
}

export default Usuario
```

El siguiente paso sería realizar la petición GET correspondiente para obtener los datos a mostrar. Al
igual que antes, la realizaremos en el hook useEffect y vamos a guardar el resultado en un estado.

**Archivo:** `/reactjs-react-router-lab/src/components/Usuario.tsx`

```tsx
import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom';

const Usuario = () => {
  const { usuarioId } = useParams()
  const [infoUsuario, setInfoUsuario] = useState('')

useEffect(() => {
  fetch(`https://jsonplaceholder.typicode.com/users/${usuarioId}`)
    .then(resp => resp.json())
    .then(datos => setInfoUsuario(JSON.stringify(datos, null, 2)))
}, [usuarioId])

    return (
      <div>
        <h3>Usuario {usuarioId}</h3>
        <pre>{infoUsuario}</pre>
      </div>
    )
}

export default Usuario
```

Con esto ya deberíamos de ver la información de los usuarios cuando pulsamos sobre los enlaces
que habíamos puesto para cada uno de ellos.

Pero, si nos fijamos, es un poco tedioso pasar de la información de uno de ellos a la de otro, ya que
tenemos que volver a la página de inicio y pulsar sobre el enlace de otro usuario.

Esto podemos mejorarlo utilizando las rutas anidadas. Vamos a hacer que al mismo tiempo que se
muestra la información de un usuario, también se muestra la lista de estos. Para ello anidaremos la
ruta /usuarios/:usuarioId dentro de la ruta de /usuarios.

Por tanto, vamos al componente App y vamos a modificar estas dos rutas, metiendo como
propiedad children a la ruta de /usuarios/:usuarioId cuyo path pasará a ser solo :usuarioId.

**Archivo:** `/reactjs-react-router-lab/src/components/App.tsx`

```tsx
import { Routes, Route, Navigate } from 'react-router-dom';
import Header from './Header';
import Inicio from './Inicio';
import NuevoUsuario from './NuevoUsuario';
import Usuario from './Usuario';

const App = () => {
  return (
    <div>
      <h1>React Router v6</h1>

<Header />

          <Routes>
            <Route path="/usuarios" element={<Inicio />}>
               <Route path=":usuarioId" element={<Usuario />} />
            </Route>
            <Route path="/nuevo-usuario" element={<NuevoUsuario />} />
            <Route path="/" element={<Navigate to="/usuarios" replace={true} />} />
          </Routes>
        </div>
    )
}

export default App
```

Ahora ya deberíamos de ver la lista, pero si pulsamos sobre cualquiera de los enlaces de los
usuarios veremos que el componente de Usuario no se muestra. Esto se debe a que nos falta una
última cosa por añadir.

Cuando usamos rutas anidadas, React Router no sabe donde tiene que colocar el componente a
pintar para las rutas anidadas, por lo que tenemos que ayudarle añadiendo el componente Outlet
dentro del componente principal, que en este caso sería nuestro componente Inicio.

**Archivo:** `/reactjs-react-router-lab/src/components/Inicio.tsx`

```tsx
import { useEffect, useState } from 'react';
import { Link, Outlet } from 'react-router-dom';

const Inicio = () => {
  const [usuarios, setUsuarios] = useState([])

useEffect(() => {
  fetch('http://jsonplaceholder.typicode.com/users')
    .then(resp => resp.json())
    .then(usuarios => setUsuarios(usuarios))
}, [])

const listaUsuarios = usuarios.map(u => (
   <li key={u.id}>
     <span>{u.username}</span>
     <Link to={'/usuarios/' + u.id}>Ver + info</Link>
   </li>
))

return (
  <div>
    <h2>Inicio</h2>
    <ul>
      {listaUsuarios}
    </ul>

          <Outlet />
        </div>
    )
}

export default Inicio
```

Para ir terminando, vamos a añadir una página de error para cuando los usuarios intenten acceder
a una ruta que no existe.

Vamos a crear un componente Error dentro de la carpeta components.

**Archivo:** `/reactjs-react-router-lab/src/components/Error.tsx`

```tsx
const Error = () => {
  return (
    <div>
      <h2 style={{color: 'red'}}>Error 404: Page not found!</h2>
    </div>
  )
}

export default Error
```

Una vez tengamos el componente, añadimos la ruta comodín dentro del componente App.

**Archivo:** `/reactjs-react-router-lab/src/components/App.tsx`

```tsx
import { Routes, Route, Navigate } from 'react-router-dom';
import Header from './Header';
import Inicio from './Inicio';
import NuevoUsuario from './NuevoUsuario';
import Usuario from './Usuario';
import Error from './Error';

const App = () => {
  return (
    <div>
      <h1>React Router v6</h1>
      <Header />

  <Routes>
    <Route path="/usuarios" element={<Inicio />}>
       <Route path=":usuarioId" element={<Usuario />} />
    </Route>
    <Route path="/nuevo-usuario" element={<NuevoUsuario />} />
    <Route path="/" element={<Navigate to="/usuarios" replace={true} />} />
    <Route path="*" element={<Error />} />
  </Routes>
</div>

    )
}

export default App
```

Si probamos a entrar en una ruta que no existe, entonces deberíamos de ver el error.