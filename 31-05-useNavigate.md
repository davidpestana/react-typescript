# 31.5. Navegación por código (useNavigate)

**PDF: páginas 220–220** (libro: 216–216)

---

[← Índice](README.md) | [← Anterior: 31.4. Link](31-04-link.md) | [Siguiente: 31.6. Rutas Parametros →](31-06-rutas-parametros.md)

---

Hemos visto como navegar usando los componentes Link de React Router, pero hay veces en las
que queremos cambiar de componente una vez se ha realizado una acción, como por ejemplo,
cuando guardamos los datos de un formulario. Esta navegación la haríamos a través de código.

Para realizar la navegación por código, tendremos que utilizar el hook de useNavigate que nos
proporciona React Router. Este hook es una función que nos va a devolver una función para
realizar la navegación a otra ruta.

Esta función se puede usar de dos formas:

- Le pasamos la ruta a la que queremos navegar como parámetro.

- O le pasamos un número (llamado delta) con el que le indicamos cuantas páginas queremos
avanzar o retroceder en la pila del historial, por ejemplo, pasarle un -1 significa que nos vamos
a la página anterior.

```tsx
import { useNavigate } from 'react-router-dom'

const App = (props) => {
  const navigate = useNavigate()

    return (
      <div>
        <button onClick={() => navigate('/mi-perfil')}>Mi perfil</button>
        <button onClick={() => navigate(-1)}>Volver atrás</button>
      </div>
    )
}

export default App
```