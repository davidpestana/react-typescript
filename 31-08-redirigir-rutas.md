# 31.8. Redirigir Rutas

**PDF: páginas 225–225** (libro: 221–221)

---

[← Índice](README.md) | [← Anterior: 31.7. Rutas Anidadas](31-07-rutas-anidadas.md) | [Siguiente: 31.9. Guards →](31-09-guards.md)

---

El componente Navigate de React Router se encarga de cambiar de ruta en el momento en el que se
pinta, por lo que podemos encontrarle varios usos:

- Nos puede servir para redirigir de una ruta a otra.

- Nos servirá para cambiar de rutas dentro de los componentes de clase, ya que en ellos no
podemos utilizar el hook de useNavigate.

```tsx
import { Routes, Route, Navigate } from 'react-router-dom'

const App = (props) => {
  return (
    <div>
      <Routes>
        <Route path='/' element={<Inicio />} />
        <Route path="/redirigeme-al-inicio" element={<Navigate to="/" replace={true} />} />
      </Routes>
    </div>
  )
}

export default App
```