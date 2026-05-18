# 28.7. Usereducer

**PDF: páginas 176–176** (libro: 172–172)

---

[← Índice](README.md) | [← Anterior: 28.7.1. Lab Usereducer](28-07-01-lab-useReducer.md) | [Siguiente: 28.8.1. Lab Crear Hook →](28-08-01-lab-crear-hook.md)

---

El hook useReducer funciona como una función reducer de la librería Redux. Nos va a permitir
gestionar el estado o parte del estado de los componentes.

Este hook es una función que recibe como parámetros la función de reducer, que a su vez recibe el
estado actual y una acción, y el estado inicial. Y este hook devuelve un array de dos posiciones en la
que en la primera nos encontramos con el estado actual y en la segunda con un método dispatch
que usaremos para emitir las acciones que le llegarán al reducer.

```tsx
const initialState = {}

function reducer(state, action) {
  // ...
}

const [state, dispatch] = useReducer(reducer, initialState)

Pero entonces, ¿cuándo usamos useState y cuándo useReducer?

La diferencia entre usar useState y useReducer es que este último suele usarse cuando para
```
cambiar el estado necesitamos añadir algo de lógica.