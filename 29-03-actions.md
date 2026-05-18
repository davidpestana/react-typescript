# 29.3. Actions

**PDF: páginas 190–190** (libro: 186–186)

---

[← Índice](README.md) | [← Anterior: 29.3.1. Action Creators](29-03-01-action-creators.md) | [Siguiente: 29.4. Reducers →](29-04-reducers.md)

---

El primer principio que sigue Redux es el de tener el estado en un objeto global inmutable, pero el
estado se va a ir actualizando con las acciones de los usuarios. Al ser inmutable no se puede
modificar su valor, por lo que en lugar de hacer eso, se va a reemplazar por un nuevo estado. Para
poder realizar estos cambios, vamos a necesitar las actions. Las actions son instrucciones que
describen los cambios que se van a realizar.

Lo primero de todo es identificar las acciones que vamos a tener en la aplicación y definir el tipo de
acción en un archivo de constantes.

```tsx
export const ACCION = 'ACCION';

Todas las actions van a ser objetos, que como mínimo van a tener un atributo type cuyo valor va a
```
ser una de las constantes que se han declarado antes y va a indicar que tiene que ocurrir.

Algunas actions necesitan saber más datos a parte de la action para poder cambiar el estado. Estos
datos se conocen como payload y se añaden en el mismo objeto JavaScript.

### 29.3.1. Action creators

Los action objects son objetos JavaScript que definen como son las acciones. Y los action creators
son funciones que crean y devuelven esos action objects, de esta forma usamos el action creator
para crear la action que necesita emitir el método dispatch.

```tsx
import { ACCION } from './action-types';

export function accion1() {
  return {
    type: ACCION
  }
}
```