# 30.6. Middleware

**PDF: páginas 212–212** (libro: 208–208)

---

El middleware en Redux nos va a permitir ejecutar piezas de código cuando se despachen las
acciones. Se pueden combinar múltiples middleware, que se iran ejecutando en cadena, y ninguno
de ellos sabrá cual se ha ejecutado antes o cual se va a ejecutar después. Estos middlewares se
suelen usar para trabajar con acciones asíncronas.

Para poder usar el middleware vamos a importar applyMiddleware desde redux. Al método de
createStore se le va a pasar como segundo parámetro el método applyMiddleware que llevará
como parámetro todos los middlewares que queramos aplicar. Las funciones de middleware
reciben como parámetro el store, y esta función tiene que devolver a su vez otra función la cual
recibe como parámetro el método next. El método next sirve para llamar a la siguiente función de
middleware. Esta función devuelve otra función más que recibe como parámetro el action que se
va a pasar como parámetro a la siguiente función middleware. En esta última función podemos
acceder, tanto al store como al action, por lo que podremos mostrar por consola el action que se ha
disparado y cual es el nuevo estado.

```tsx
import { createStore, applyMiddleware } from 'redux';
import miReducer from './reducer';

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

    return createStore(miReducer, applyMiddleware(logger));
}
```
Y de esta forma, cada vez que se lance una acción, nos va a mostrar la acción despachada y el
siguiente estado de la aplicación.
