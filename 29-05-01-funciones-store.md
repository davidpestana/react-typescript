# 29.5.1. Funciones Store

**PDF: páginas 193–193** (libro: 189–189)

---

[← Índice](README.md) | [← Anterior: 29.4. Reducers](29-04-reducers.md) | [Siguiente: 29.5. Store →](29-05-store.md)

---

El objeto store que creamos con Redux nos da acceso a una serie de funciones para poder utilizar
las funcionalidades de esta librería.

Estas funciones son:

- getState(): con esta función obtenemos el estado actual del store.

- dispatch(actionObject): con esta función despachamos una acción para cambiar el estado de la
aplicación.

- subscribe(fn): el subscribe nos permite ejecutar la función de callback fn cada vez que cambia
el estado que almacena el store. Esta función nos devuelve la referencia a una función para
eliminar la suscripción.

```tsx
const App = ({store}) => {
  useEffect(() => {
    const unsubscribe = store.subscribe(() => {
       console.log(store.getState())
    })

  return unsubscribe;
}, [])

    return (
      <div>
        <button type="button" onClick={() => store.dispatch({type: 'ACCION'})}>Emitir acción</button>
      </div>
    )
}

export default App
```