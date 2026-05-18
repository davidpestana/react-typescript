# 31.3. Routes Route

**PDF: páginas 218–218** (libro: 214–214)

---

[← Índice](README.md) | [← Anterior: 31.2. Browser Router](31-02-browser-router.md) | [Siguiente: 31.4. Link →](31-04-link.md)

---

React Router nos proporciona dos componentes necesarios para definir las rutas de nuestra
aplicación, el componente Routes y el Route.

Con el componente Route vamos a definir las distintas rutas de la aplicación. Este componente
recibe como propiedades:

- path: el path con el que tiene que coincidir la url.

- element: el elemento HTML/TSX a renderizar cuando el path coincida con la URL a la que
hemos navegado.

El componente Routes es un contenedor para los componentes Route, y de lo que se va a encargar
es de recorrer todas las rutas que se le pasan como children para mostrar aquella que tenga la
mayor coincidencia con la URL. Esto es algo nuevo que se ha añadido en esta última versión de
react-router (la v6), ya que en las anteriores versiones se mostraban según el orden en el que se
```tsx
encontraban definidas, algo que puede llevar a darnos algún quebradero de cabeza.

import { Routes, Route } from 'react-router-dom'

const App = (props) => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Inicio />} />
        <Route path="/fin" element={<Fin />} />
      </Routes>
    </div>
  )
}

export default App

Necesitamos añadir la opción devServer.historyApiFallback: true en la
```
configuración de webpack para que funcione correctamente al cambiar entre las
distintas páginas.

Si no la añadimos, cada vez que se cambie la URL se hará una petición al servidor
pidiendo un archivo nuevo de HTML para descargar. El problema es que solo
tenemos un único index.html en nuestra aplicación. Con esta opción, le estamos
indicando que devuelva ese único archivo para todas las peticiones que le lleguen
al servidor.