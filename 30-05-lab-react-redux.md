# 30.5. Lab React Redux

**PDF: páginas 207–211** (libro: 203–207)

---

[← Índice](README.md) | [← Anterior: 30.4. Hooks React Redux](30-04-hooks-react-redux.md) | [Siguiente: 30.6.1. Redux Thunk →](30-06-01-redux-thunk.md)

---

En este laboratorio vamos a ver como utilizar la librería de Redux para gestionar el estado de un
contador pero esta vez utilizando la librería react-redux.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-react-redux-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Para poder usar redux y react-redux vamos a necesitar lanzar los siguientes comandos dentro de
la carpeta del proyecto:

```tsx
$ npm install redux
$ npm install react-redux
```
Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Vamos a empezar creando la estructura del contador dentro de nuestro componente App.

**Archivo:** `/reactjs-react-redux-lab/src/components/App.tsx`

```tsx
const App = (): JSX.Element => {
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

- store/config-store.ts

- store/contador/action-types.ts

- store/contador/actions.ts

- store/contador/index.ts

Vamos a empezar definiendo los distintos tipos de acciones que vamos a poder despachar. Esto lo
haremos en el archivo action-types.ts, en el que vamos a crear una serie de constantes que
exportaremos para usarlas luego más tarde en el reducer y en el archivo actions.ts.

**Archivo:** `/reactjs-react-redux-lab/src/store/contador/action-types.ts`

```tsx
export const INCREMENTAR = 'INCREMENTAR' as const;
export const DECREMENTAR = 'DECREMENTAR' as const;
```
Ahora vamos a crear las funciones action creators que se encargarán de crear los objetos de
acciones que vamos a despachar.

Nos vamos al archivo actions.ts en el que exportaremos dos funciones, una que devolverá la acción
para incrementar la cuenta, y la otra para decrementarla.

**Archivo:** `/reactjs-react-redux-lab/src/store/contador/actions.ts`

```tsx
import { INCREMENTAR, DECREMENTAR } from "./action-types";

export function incrementar() {
  return { type: INCREMENTAR } as const;
}

export function decrementar() {
  return { type: DECREMENTAR } as const;
}

export type ContadorAction =
  | ReturnType<typeof incrementar>
  | ReturnType<typeof decrementar>;
```
Una vez tenemos este archivo, vamos a rellenar el index.ts donde vamos a poner nuestro reducer,
es decir, una función que va a recibir el estado actual y una acción, y donde vamos a crear el nuevo
estado con los cambios indicados por la acción que llega. Esta función tiene que retornar el nuevo
estado.

**Archivo:** `/reactjs-react-redux-lab/src/store/contador/index.ts`

```tsx
import { DECREMENTAR, INCREMENTAR } from "./action-types";
import type { ContadorAction } from "./actions";

export default function contador(
  state = 0,
  action: ContadorAction
): number {
  switch (action.type) {
    case INCREMENTAR:
      return state + 1;
    case DECREMENTAR:
      return state - 1;
    default:
      return state;
  }
}
```
Con esto ya tenemos la parte de las acciones y el reducer, ahora solo tenemos que crear el store, y
esto lo haremos en el archivo config-store.ts.

Dentro de este archivo exportaremos otra función que va a retornar el store creado con la función
createStore de Redux a la que le vamos a pasar nuestro reducer.

**Archivo:** `/reactjs-react-redux-lab/src/store/config-store.ts`

```tsx
import { createStore } from 'redux'
import contadorReducer from './contador'

export const configStore = () => {
  return createStore(contadorReducer)
}
```
El siguiente paso es crear el store y pasarlo como propiedad a los componente. Aquí vamos a
envolver nuestro componente App con el componente Provider de react-redux al cual le
pasaremos el store y se encargará de hacerlo llegar a todos los componentes donde vayamos a
necesitarlo.

**Archivo:** `/reactjs-react-redux-lab/src/main.tsx`

```tsx
import { createRoot } from 'react-dom/client';
import App from './components/App';
import { Provider } from 'react-redux';
import './style.css';
import { configStore } from './store/config-store';

const store = configStore();

createRoot(document.getElementById('root')).render(<Provider store={store}><App /></Provider>);
```
Ahora vamos a obtener el estado dentro del componente App para mostrarlo en lugar del 0 que
hemos puesto hardcodeado anteriormente.

Necesitaremos llamar al hook de useSelector y retornar el estado del store, lo que nos devolverá la
cuenta actual.

**Archivo:** `/reactjs-react-redux-lab/src/components/App.tsx`

```tsx
import { useSelector } from 'react-redux';

const App = (): JSX.Element => {

const cuenta = useSelector(state => state);

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
Ahora nos toca añadir los eventos de click a los botones, con los que vamos a llamar a dos
funciones que vamos a crear desde las que despacharemos las acciones.

**Archivo:** `/reactjs-react-redux-lab/src/components/App.tsx`

```tsx
import { useSelector } from 'react-redux';
import { incrementar, decrementar } from '../store/contador/actions';

const App = (): JSX.Element => {
  const cuenta = useSelector(state => state);

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
Para poder despachar las acciones que nos devuelven los action creators, vamos a necesitar
ejecutar la función dispatch que nos devuelve el hook useDispatch. Por lo que lo importamos y
ejecutaremos dispatch(actionObj) dentro de ambas funciones a las que se llaman desde los
botones.

**Archivo:** `/reactjs-react-redux-lab/src/components/App.tsx`

```tsx
import { useSelector, useDispatch } from 'react-redux';

import { incrementar, decrementar } from '../store/contador/actions';

const App = (): JSX.Element => {
  const cuenta = useSelector(state => state);
  const dispatch = useDispatch()

const incrementarCuenta = () => {
  const actionObj = incrementar()
  dispatch(actionObj)
}

const decrementarCuenta = () => {
  const actionObj = decrementar()
  dispatch(actionObj)
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
Y con esto ya tenemos nuestro contador funcionando.

Si comparamos este laboratorio con el de Lab: Redux, podemos ver que es mucho
más fácil crear la misma aplicación utilizando la librería de react-redux que
usando solo redux.