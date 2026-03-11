# 31.11. Query Params

**PDF: páginas 228–229** (libro: 224–225)

---

[← Índice](README.md) | [← Anterior: 31.10. Ruta Comodin](31-10-ruta-comodin.md) | [Siguiente: 31.12. Lab React Router →](31-12-lab-react-router.md)

---

Otro tipo de parámetros con los que nos podemos encontrar en las rutas de la aplicación son los
parámetros de consulta, o query params, que son aquellos que van detrás del ? al final de la URL.

Para poder acceder a estos parámetros de query, React Router nos proporciona un hook
```tsx
useSearchParams que funciona de forma similar al useState, devolviendonos un array de dos
```
posiciones, donde la primera va a contener los parámetros, y la segunda es un método para poder
modificarlos.

```tsx
import { useSearchParams } from 'react-router-dom'

const ListaDatos = (props) => {
  const [queryParams, setQueryParams] = useSearchParams()
  const categoria = queryParams.get('categoria')

const datos = props.lista.filter(d => d.categoria === categoria).map(d => <li key={d.id}>{d.titulo}</li>)

    return (
      <ul>
        {datos}
      </ul>
    )
}

export default ListaDatos
```
Si quisieramos modificar los queryParams, tendríamos que llamar a la función de
setQueryParams pasandole como parámetro un objeto de JavaScript con los datos de los
parámetros.

```tsx
import { useSearchParams } from 'react-router-dom'

const Cmp = (props) => {
  const [queryParams, setQueryParams] = useSearchParams()

const fn = () => {
  setQueryParams({
     param1: 'val1',
     param2: 'val2',
  })
}

return (
  <div>
```
...
```tsx
      </div>
    )
}

export default Cmp
```