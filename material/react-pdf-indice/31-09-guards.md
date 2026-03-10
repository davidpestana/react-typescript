# 31.9. Guards

**PDF: páginas 226–226** (libro: 222–222)

---

Las guardas nos permiten entrar en los componentes o no hacerlo dependiendo de alguna
condición. Por ejemplo, en una aplicación solo se podrá ver la información de un usuario en el caso
de que este usuario se haya logueado. Para añadir una guarda a nuestra aplicación es tan sencillo
como renderizar la ruta o no hacerlo dependiendo de la condición.

```tsx
import { Routes, Route } from 'react-router-dom'
import NuevoProyecto from './components/NuevoProyecto'

const App = (props) => {
  const [logueado, setLogueado] = useState(false)

    return (
      <div>
        <Routes>
          <Route path="/" element={<Inicio />} />
          {logueado && <Route path="/crear-proyecto" element={<NuevoProyecto />} />}
        </Routes>
      </div>
    )
}

export default App

De esta forma, como logueado es false, la ruta no se renderiza por lo que el componente asociado a
```
ella no se puede mostrar y no se cambia la url.
