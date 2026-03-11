# 31.7. Rutas Anidadas

**PDF: páginas 223–224** (libro: 219–220)

---

[← Índice](README.md) | [← Anterior: 31.6. Rutas Parametros](31-06-rutas-parametros.md) | [Siguiente: 31.8. Redirigir Rutas →](31-08-redirigir-rutas.md)

---

Por ahora solo hemos creado rutas que se encuentran al mismo nivel, pero en algunos casos vamos
a necesitar mostrar componentes que comparten parte de la misma url, y en estos casos es cuando
podremos usar las rutas anidadas.

Por ejemplo, podríamos usarlo con un listado de datos para mostrar al mismo tiempo tanto la lista
como la información de alguno de estos datos:

- /usuarios: esta mostrará la lista de los usuarios.

- /usuarios/2: esta mostrará la información del usuario que tiene el id 2.

Otro caso podría ser en el que tenemos un listado de series/peliculas y podemos filtrarlas por el
género:

- /categorias: esta mostrará la lista de las categorías.

- /categorias/comedia: esta mostrará las series/peliculas de la categoría comedia.

- /categorias/comedia/-M1s1hXmn6_UopYgiIy6: esta mostrará la información de la serie/película
que tiene el id -M1s1hXmn6_UopYgiIy6 y pertenece a la categoría comedia.

Con las rutas anidadas conseguiremos mostrar los componentes asociados a cada parte de la ruta al
mismo tiempo, por lo que tendremos que añadir los componentes Route anidados según vayamos a
definir las rutas.

```tsx
import { Routes, Route } from 'react-router-dom'

const App = (props) => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Layout />}>
           <Route path="categorias" element={<ListaCategorias />}>
             <Route path=":categoria" element={<Categoria />}>
               <Route path=":serieId" element={<Serie />} />
             </Route>
           </Route>
        </Route>
      </Routes>
    </div>
  )
}

export default App
```
Una vez definidas las rutas, en aquellas que hemos puesto como rutas anidadas tendremos que
indicar en que posición dentro del elemento que se va a renderizar se tiene que renderizar el
```tsx
elemento perteneciente a la ruta anidada. Para esto usaremos el componente Outlet que viene de
```
la librería react-router-dom.

```tsx
import { Outlet, Link } from 'react-router-dom'

const ListaCategoria = (props) => {
  return (
    <div>
      <h2>Categorias</h2>
      <ul>
        <li><Link to="/categorias/comedia">Comedia</Link></li>
        <li><Link to="/categorias/terror">Terror</Link></li>
        <li><Link to="/categorias/drama">Drama</Link></li>
      </ul>
      <div>
        <Outlet />
      </div>
    </div>
  )
}

export default ListaCategoria
```