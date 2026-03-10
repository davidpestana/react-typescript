# 30.6.1. Redux Thunk

**PDF: páginas 213–214** (libro: 209–210)

---

En nuestras aplicaciones seguramente que vamos a necesitar ejecutar código asíncrono, por
ejemplo para pedir los datos al servidor, y al usar redux puede no quedar muy claro como hacerlo.
Esto es lo que vamos a ver con redux-thunk. Redux thunk es un middleware que nos va a permitir
exactamente eso, ejecutar código asíncrono antes de despachar la acción. Para poder usarlo
tenemos que instalar la dependencia:

```tsx
$ npm install redux-thunk
```
Una vez instalado, como es un middleware, lo tendremos que pasar en la función de
applyMiddleware que se encuentra en el archivo de configuración del store.

```tsx
import { createStore, applyMiddleware } from 'redux';
import miReducer from './reducer';
import thunk from 'redux-thunk';

export default function configStore() {
  const logger = (store) => {
    return (next) => {
      return (action) => {
        console.log('Dispatched action: ', action);
        const res = next(action);
        console.log('Next state: ', store.getState());
        return res;
      }
    }
  }

    return createStore(miReducer, applyMiddleware(logger, thunk));
}
```
Redux-Thunk nos va a permite crear action creators que van a devolver una función en lugar de la
acción, por lo que antes de que se modifique el estado se va a haber ejecutado ese código asíncrono.
La función que devuelven estos action creators recibe como parámetros el método de dispatch
para despachar la acción una vez haya terminado el código asíncrono de ejecutarse y el método de
getState que nos da el estado actual del store. De esta forma una vez que ya tenemos los datos del
servidor, usamos el método dispatch para despachar la acción (que devolverá otro action creator).

```tsx
import * as ActionTypes from './action-types';

function accion() {
  return dispatch => {
    setTimeout(() => {
      dispatch(getAccionObj());
    }, 2000)
  }

function getAccionObj() {
  return {
    type: ActionTypes.ACCION
  }
}

export { accion };
```
