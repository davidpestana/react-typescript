# 25.2. Lab Hoc Cargar Datos

**PDF: páginas 130–136** (libro: 126–132)

---

[← Índice](README.md) | [← Anterior: 25.1. Lab Hoc Estilos](25-01-lab-hoc-estilos.md) | [Siguiente: 26. Suspense →](26-00-suspense.md)

---

En este laboratorio vamos a ver como crear un higher order component que se encargará de pedir
unos datos para inyectarlos en un componente, y mostrar un spinner mientras se piden.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-higher-order-components-
cargar-datos-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Empezaremos creando la siguiente estructura de archivos que después iremos rellenando:

- src/hoc/withData.js

- src/components/InfoUsuario.tsx

Vamos a empezar a rellenar el hoc withData con la función que recibe el componente y vamos a
hacer que retorne el nuevo componente que renderiza el WrappedCmp con las propiedades que se
le pasan.

**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/hoc/withData.js`

```tsx
import { Component } from 'react';

const withData = (WrappedCmp) => {
  return class extends Component {
    render() {
      return (
        <>
           <WrappedCmp {...this.props} />
        </>
      )
    }
  }
}

export default withData;
```
La idea es que desde este hoc realicemos una petición GET a una URL para obtener los datos que se
le van a pasar a nuestro componente. Entonces vamos a hacer que nuestro hoc reciba también la
URL.

Una vez que tenemos la URL, tenemos que hacer la petición, pero los datos recibidos tendremos que
almacenarlos en algún sitio para poder pasarselos al componente. Así que crearemos un estado
data que inicializamos a null hasta que los datos se hayan obtenido.

**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/hoc/withData.js`

```tsx
import { Component } from 'react';

const withData = (WrappedCmp, url) => {
  return class extends Component {
    constructor(props) {
      super(props);
      this.state = {
        data: null
      }
    }

        render() {
          return (
            <>
               <WrappedCmp {...this.props} />
            </>
          )
        }
    }
}

export default withData;
```
Ahora vamos a realizar la petición GET usando el método fetch en el método del ciclo de vida
componentDidMount, y una vez que hayamos obtenido los datos cambiaremos el estado.

**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/hoc/withData.js`

```tsx
import { Component } from 'react';

const withData = (WrappedCmp, url) => {
  return class extends Component {
    constructor(props) {
      super(props);
      this.state = {
        data: null
      }
    }
```
async componentDidMount() {
```tsx
const response = await fetch(url);
const datos = await response.json();
```
this.setState({
```tsx
data: datos

    })
}

        render() {
          return (
            <>
               <WrappedCmp {...this.props} />
            </>
          )
        }
    }
}

export default withData;
```
Una vez que tenemos los datos ya se los podemos pasar a nuestro componente WrappedCmp de la
misma forma en que le pasamos cualquier valor, en forma de propiedad.

**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/hoc/withData.js`

```tsx
import { Component } from 'react';

const withData = (WrappedCmp, url) => {
  return class extends Component {
    constructor(props) {
      super(props);
      this.state = {
        data: null
      }
    }
```
async componentDidMount() {
```tsx
  const response = await fetch(url);
  const datos = await response.json();
  this.setState({
     data: datos
  })
}

        render() {
          return (
            <>
               <WrappedCmp {...this.props} data={this.state.data} />
            </>
          )
        }
    }
}

export default withData;
```
Ahora que tenemos el hoc, podemos mejorarlo un poco más para hacer que no se pinte el
componente que espera los datos hasta que se hayan obtenido estos. Mientras se obtienen vamos a
mostrar un mensaje de loading.

Para hacer esto vamos a añadir en el estado otro atributo cargandoDatos que vamos a inicializar a
```tsx
true, y mientras este valor sea true, se mostrará el mensaje de loading.
```
**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/hoc/withData.js`

```tsx
import { Component } from 'react';

const withData = (WrappedCmp, url) => {
  return class extends Component {
    constructor(props) {
      super(props);
      this.state = {
        data: null,
        cargandoDatos: true
      }
    }
```
async componentDidMount() {
```tsx
  const response = await fetch(url);
  const datos = await response.json();
  this.setState({
     data: datos
  })
}

        render() {
          return (
            <>
               {this.state.cargandoDatos ? <p>Loading...</p> : <WrappedCmp {...this.props} data={this.state.data} />}
            </>
          )
        }
    }
}

export default withData;
```
De momento se queda siempre mostrando el mensaje de loading, y es porque cuando obtenemos
```tsx
los datos tenemos que cambiar el valor de cargandoDatos a false. Vamos a poner el cambio de
```
estado dentro de un setTimeout para ver que el mensaje se muestra.

**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/hoc/withData.js`

```tsx
import { Component } from 'react';

const withData = (WrappedCmp, url) => {
  return class extends Component {
    constructor(props) {
      super(props);
      this.state = {
        data: null,
        cargandoDatos: true
      }
    }
```
async componentDidMount() {
```tsx
  const response = await fetch(url);
  const datos = await response.json();
  setTimeout(() => {
    this.setState({
       data: datos,
       cargandoDatos: false
    })
  }, 1400)
}

        render() {
          return (
            <>
               {this.state.cargandoDatos ? <p>Loading...</p> : <WrappedCmp {...this.props} data={this.state.data} />}
            </>
          )
        }
    }
}

export default withData;
```
Por último para dejar este componente más completo, vamos a hacer que el loading se le pueda
configurar mandandoselo como parámetro del hoc de tal forma que podamos mostrar mensajes o
spinners que se adapten mejor a nuestra aplicación.

**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/hoc/withData.js`

```tsx
import { Component } from 'react';

const withData = (WrappedCmp, url, Loader = <p>Loading...</p>) => {
  return class extends Component {
    constructor(props) {
      super(props);
      this.state = {
        data: null,
        cargandoDatos: true
      }
    }
```
async componentDidMount() {
```tsx
  const response = await fetch(url);
  const datos = await response.json();
  setTimeout(() => {
    this.setState({
       data: datos,
       cargandoDatos: false
    })
  }, 1400)
}

render() {
  return (
    <>
       {this.state.cargandoDatos ? Loader : <WrappedCmp {...this.props} data={this.state.data} />}
    </>

            )
        }
    }
}

export default withData;
```
Ahora que tenemos el hoc completo, vamos a crear el componente que recibirá los datos y los
pintará.

**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/components/InfoUsuario.tsx`

```tsx
const InfoUsuario = ({ data }) => {
  const { name, email, picture } = data.results[0];
  return (
    <div>
      <h2>{name.first} {name.last}</h2>
      <img src={picture.medium} alt={`Foto de ${name.first}`} />
      <p>✉️: {email}</p>
    </div>
  )
}

export default InfoUsuario
```
Y ahora en el componente App vamos a utilizar nuestro hoc withData para inyectar en el
componente InfoUsuario los datos que obtenemos de la API de https://randomuser.me/api/.

**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/components/App.tsx`

```tsx
import withData from "../hoc/withData"
import InfoUsuario from './InfoUsuario';

const App = () => {
  const InfoUsuarioWithData = withData(InfoUsuario, 'https://randomuser.me/api/');

    return (
      <div>
        <InfoUsuarioWithData />
      </div>
    )
}

export default App
```
Con esto ya deberíamos de ver la información aleatoria de un usuario con el loader mientras se
cargan los datos.

Para hacer un poco más molón el ejemplo, vamos a utilizar algún spinner más currado. Para ello
utilizaremos la dependencia de spinners-react que podemos encontrar en

https://adexin.github.io/spinners/.

Instalamos la dependencia en nuestro proyecto lanzando el comando:

```tsx
$ npm install --save spinners-react
```
Una vez instalada, buscamos el spinner que más nos guste y lo importamos dentro de nuestro
componente principal, y se lo vamos a pasar a nuestro HOC.

**Archivo:** `/reactjs-higher-order-components-cargar-datos-lab/src/components/App.tsx`

```tsx
import withData from "../hoc/withData"
import InfoUsuario from './InfoUsuario';

const App = () => {
  const InfoUsuarioWithData = withData(
```
InfoUsuario,
```tsx
   'https://randomuser.me/api/',
   <SpinnerDotted size={50} thickness={100} speed={100} color="#36ad47" />
);

    return (
      <div>
        <InfoUsuarioWithData />
      </div>
    )
}

export default App
```