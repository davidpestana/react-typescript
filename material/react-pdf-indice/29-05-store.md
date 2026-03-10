# 29.5. Store

**PDF: páginas 192–192** (libro: 188–188)

---

El store es la parte que se encarga de almacenar el estado de la aplicación y gestiona todas las
actualizaciones de estado. El patrón Flux permitía tener más de un store en la aplicación, pero con
Redux solo vamos a tener uno para la aplicación entera.

El store va a gestionar las actualizaciones del estado pasando el estado actual y la action a través de
un reducer que va a resultar de la combinación de varios reducers más pequeños que se centran en
parte más concretas. En principio, cuando se crea el store, este solo recibe un reducer como
argumento. De esta forma se pierde la modularidad, porque al recibir solo un reducer, tendríamos
que añadir en ese reducer toda la funcionalidad para manejar el estado. Pero nos permite evitar
eso combinando todos los reducers en uno solo que va a ser el que le pasemos como argumento.

Para crear el store se va a usar la función createStore(reducer, initial_state) el cual puede recibir
(opcionalmente) un segundo parámetro que sería un estado inicial.

```tsx
import { createStore } from 'redux';
import miReducer from './contador';

export default function configStore() {
  return createStore(miReducer);
}
```
Y para combinar los distintos reducers en uno solo se usa el método combineReducers() que
recibe como argumento un objeto con los reducers a combinar.

```tsx
import { createStore, combineReducers } from 'redux';
import reducer1 from './red1';
import reducer2 from './red2';

export default function configStore() {
  return createStore(combineReducers({
```
reducer1,
reducer2
```tsx
  }));
}
```
