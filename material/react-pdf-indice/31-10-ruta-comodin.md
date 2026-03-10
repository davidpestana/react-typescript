# 31.10. Ruta Comodin

**PDF: páginas 227–227** (libro: 223–223)

---

La ruta comodín es aquella que se va a ejecutar siempre que no se ejecute ninguna otra ruta. Esta
ruta se suele usar para mostrar una página de error, o para redireccionar a la página de inicio,
siempre que introduzcamos una URL que no existe en nuestra aplicación.

Para usar esta ruta, solo hay que poner el path * e indicar el componente a mostrar. Además, hay
que tener en cuenta que siempre la tenemos que poner en la última posición dentro de las rutas, ya
que se ejecutará solo si no se ha ejecutado antes de ella otra ruta.

```tsx
import { Routes, Route } from 'react-router-dom';
import { Error } from './components/error';

const App = (props) => {
  return (
    <div>
      <Routes>
        {/* otras rutas */}
        <Route path="*" element={<Error />} />
      </Routes>
    </div>
  )
}

export default App;
```
