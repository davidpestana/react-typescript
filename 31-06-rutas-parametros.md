# 31.6. Rutas Parametros

**PDF: páginas 221–222** (libro: 217–218)

---

[← Índice](README.md) | [← Anterior: 31.5. Navegación por código (useNavigate)](31-05-useNavigate.md) | [Siguiente: 31.7. Rutas Anidadas →](31-07-rutas-anidadas.md)

---

Cuando tenemos listados de datos, es muy probable que necesitemos ver más en detalle la
información de cada elemento en la lista, y aquí es donde entran las rutas con parámetros. Estas
rutas tienen una parte dinámica que va a cambiar dependiendo de los datos que queramos
mostrar, donde normalmente se usa el identificador del dato.

Para indicar que una ruta tiene un valor dinámico o parámetro vamos a utilizar : delante del
```tsx
nombre del parámetro en el path.

import { Routes, Route } from 'react-router-dom'

const App = (props) => {
  return (
    <div>
      <Routes>
        <Route path="/noticias/:id" element={<Noticia />} />
      </Routes>
    </div>
  )
}

export default App
```
De esta forma ya podemos crear rutas como:

- /noticias/1

- /noticias/12893

- /noticias/-M73ljd39udHS92_J0ss2

- …

Luego en el componente asociado a dicha ruta necesitaremos recuperar el valor del parámetro, y
aquí entra el hook useParams de React Router, con el que obtendremos un objeto de JS con el
nombre del parámetro como clave, y asociado a este, el valor que le hemos puesto en la ruta.

```tsx
import { useParams } from 'react-router-dom'

const Noticia = (props) => {
  const { id } = useParams()

return (
  <div>
```
...
```tsx
      </div>
    )
}

export default Noticia
```