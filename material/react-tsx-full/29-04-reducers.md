# 29.4. Reducers

**PDF: páginas 191–191** (libro: 187–187)

---

[← Índice](README.md) | [← Anterior: 29.3. Actions](29-03-actions.md) | [Siguiente: 29.5.1. Funciones Store →](29-05-01-funciones-store.md)

---

Los reducers son funciones puras que cogen el estado actual y una action y los usan para crear el
nuevo estado y devolverlo. Este nuevo estado se inyecta en los componentes para refrescar la
interfaz de usuario con los nuevos datos.

```tsx
import { ACCION } from './action-types';

export default function reducer(state = 'hola mundo', action) {
  switch (action.type) {
    case ACCION:
      return state + '!';
    default:
      return state;
  }
}
```