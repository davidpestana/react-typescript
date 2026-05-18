# 29.6. Lab Redux

**PDF: páginas 194–200** (libro: 190–196)

---

[← Índice](README.md) | [← Anterior: 29.5. Store](29-05-store.md) | [Siguiente: 30. React Redux →](30-00-react-redux.md)

---

En este laboratorio vamos a ver como utilizar la librería de Redux para gestionar el estado de un
contador.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-redux-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Para poder usar redux vamos a necesitar instalar la siguiente dependencia en nuestro proyecto:

```tsx
$ npm install redux
```
Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Vamos a empezar creando la estructura del contador dentro de nuestro componente App.

**Archivo:** `/reactjs-redux-lab/src/components/App.tsx`

```tsx
const App = () => {
  return (
    <div>
      <button>-</button>
      <span>Cuenta: 0</span>
      <button>+</button>
    </div>
  )
}

export default App
```
Ahora, vamos a empezar a crear los archivos que necesitaremos para utilizar Redux en nuestro
proyecto.

Empezamos creando una carpeta store dentro de la carpeta src. Dentro de esta carpeta vamos a
generar la siguiente estructura de archivos y carpetas:

- store/config-store.js

- store/contador/action-types.js

- store/contador/actions.js

- store/contador/index.js

Vamos a empezar definiendo los distintos tipos de acciones que vamos a poder despachar. Esto lo
haremos en el archivo de action-types.js, en el que vamos a crear una serie de constantes que
exportaremos para usarlas luego más tarde en el reducer y en el archivo de actions.js.

**Archivo:** `/reactjs-redux-lab/src/store/contador/action-types.js`

```tsx
export const INCREMENTAR = 'INCREMENTAR';
export const DECREMENTAR = 'DECREMENTAR';
```
Ahora vamos a crear las funciones action creators que se encargarán de crear los objetos de
acciones que vamos a despachar.

Nos vamos al archivo actions.js en el que exportaremos dos funciones, una que devolverá la acción
para incrementar la cuenta, y la otra para decrementarla.

**Archivo:** `/reactjs-redux-lab/src/store/contador/actions.js`

```tsx
import { INCREMENTAR, DECREMENTAR } from "./action-types"

export function incrementar() {
  return {
    type: INCREMENTAR,
  }
}

export function decrementar() {
  return {
    type: DECREMENTAR,
  }
}
```
Una vez tenemos este archivo, vamos a rellenar el index.js donde vamos a poner nuestro reducer,
es decir, una función que va a recibir el estado actual y una acción, y donde vamos a crear el nuevo
estado con los cambios indicados por la acción que llega. Esta función tiene que retornar el nuevo
estado.

**Archivo:** `/reactjs-redux-lab/src/store/contador/index.js`

```tsx
import { DECREMENTAR, INCREMENTAR } from "./action-types";

export default function contador(state = 0, action) {
  switch (action.type) {
    case INCREMENTAR:
      return state + 1;
    case DECREMENTAR:
      return state - 1;
    default:
      return state;
  }
```
Con esto ya tenemos la parte de las acciones y el reducer, ahora solo tenemos que crear el store, y
esto lo haremos en el archivo config-store.js.

Dentro de este archivo exportaremos otra función que va a retornar el store creado con la función
createStore de Redux a la que le vamos a pasar nuestro reducer.

**Archivo:** `/reactjs-redux-lab/src/store/config-store.js`

```tsx
import { createStore } from 'redux'
import contadorReducer from './contador'

export const configStore = () => {
  return createStore(contadorReducer)
}
```
El siguiente paso es crear el store y pasarlo como propiedad a los componentes. En nuestro caso lo
tenemos fácil porque solo tenemos un componente, por tanto, dentro del archivo src/index.js
llamaremos a esta función que acabamos de crear y le pasaremos el store como propiedad al
componente App.

**Archivo:** `/reactjs-redux-lab/src/index.js`

```tsx
import { createRoot } from 'react-dom/client';
import App from './components/App';
import './style.css';
import { configStore } from './store/config-store';

const store = configStore();

createRoot(document.getElementById('root')).render(<App store={store} />);
```
Ahora vamos a empezar por mostrar la cuenta actual en el componente App.

Como recibimos el store como propiedad, podemos pedir el estado actual llamando a la función
getState de este y mostrarlo donde habíamos puesto el 0 dentro de la etiqueta span.

**Archivo:** `/reactjs-redux-lab/src/components/App.tsx`

```tsx
const App = ({store}) => {

const cuenta = store.getState();

return (
  <div>
    <button>-</button>
    <span>Cuenta: {cuenta}</span>
    <button>+</button>

        </div>
    )
}

export default App
```
Ahora vamos a importar las funciones de los action creators en el componente, y vamos a añadir
dos funciones a los botones con las que ejecutaremos estos action creators para obtener las
acciones a despachar.

**Archivo:** `/reactjs-redux-lab/src/components/App.tsx`

```tsx
import { incrementar, decrementar } from "../store/contador/actions";

const App = ({store}) => {

const cuenta = store.getState();

const incrementarCuenta = () => {
  const actionObj = incrementar();
}

const decrementarCuenta = () => {
  const actionObj = decrementar();
}

    return (
      <div>
        <button type="button" onClick={decrementarCuenta}>-</button>
        <span>Cuenta: {cuenta}</span>
        <button type="button" onClick={incrementarCuenta}>+</button>
      </div>
    )
}

export default App
```
Ahora nos toca despachar estas dos acciones, y para ello, usaremos la función dispatch que nos
ofrece el store.

**Archivo:** `/reactjs-redux-lab/src/components/App.tsx`

```tsx
import { incrementar, decrementar } from "../store/contador/actions";

const App = ({store}) => {

const cuenta = store.getState();

const incrementarCuenta = () => {
  const actionObj = incrementar();

    store.dispatch(actionObj);
}

const decrementarCuenta = () => {
  const actionObj = decrementar();
  store.dispatch(actionObj);
}

    return (
      <div>
        <button type="button" onClick={decrementarCuenta}>-</button>
        <span>Cuenta: {cuenta}</span>
        <button type="button" onClick={incrementarCuenta}>+</button>
      </div>
    )
}

export default App
```
Si pulsamos sobre los botones, vemos que la cuenta no se actualiza. Esto se debe a que no nos
hemos suscrito a los cambios de estado del store, por lo que no estamos recibiendo el nuevo estado
cuando cambia.

```tsx
Entonces, el siguiente paso es añadir la suscripción a estos cambios dentro del hook de useEffect,
```
además tendremos que eliminar la suscripción cuando el componente se vaya a destruir, por lo que
devolveremos la función que nos retorna el store.subscribe.

**Archivo:** `/reactjs-redux-lab/src/components/App.tsx`

```tsx
import { useEffect } from 'react';
import { incrementar, decrementar } from "../store/contador/actions";

const App = ({store}) => {
  const cuenta = store.getState();

useEffect(() => {
  const unsubscribe = store.subscribe(() => {
     console.log(store.getState())
  })

  return unsubscribe;
}, [])

const incrementarCuenta = () => {
  const actionObj = incrementar();
  store.dispatch(actionObj);
}

const decrementarCuenta = () => {
  const actionObj = decrementar();

    store.dispatch(actionObj);
}

    return (
      <div>
        <button type="button" onClick={decrementarCuenta}>-</button>
        <span>Cuenta: {cuenta}</span>
        <button type="button" onClick={incrementarCuenta}>+</button>
      </div>
    )
}

export default App
```
Ahora que ya estamos recibiendo los cambios de estado, vamos a crear un estado para almacenar el
valor de la cuenta y lo cambiaremos por el nuevo dentro de la suscripción.

**Archivo:** `/reactjs-redux-lab/src/components/App.tsx`

```tsx
import { useEffect, useState } from 'react';
import { incrementar, decrementar } from "../store/contador/actions";

const App = ({store}) => {
  const [cuenta, setCuenta] = useState(0)

useEffect(() => {
  const unsubscribe = store.subscribe(() => {
     setCuenta(store.getState())
  })

  return unsubscribe;
}, [])

const incrementarCuenta = () => {
  const actionObj = incrementar();
  store.dispatch(actionObj);
}

const decrementarCuenta = () => {
  const actionObj = decrementar();
  store.dispatch(actionObj);
}

return (
  <div>
    <button type="button" onClick={decrementarCuenta}>-</button>
    <span>Cuenta: {cuenta}</span>
    <button type="button" onClick={incrementarCuenta}>+</button>
  </div>
)

export default App
```
Ahora ya podemos ver que la cuenta se actualiza cada vez que pulsamos los botones.