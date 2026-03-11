# 20.8. Lab Ciclo Vida

**PDF: páginas 92–99** (libro: 88–95)

---

[← Índice](README.md) | [← Anterior: 20.7. Componentwillunmount](20-07-componentWillUnmount.md) | [Siguiente: 21. Referencias →](21-00-referencias.md)

---

En este laboratorio vamos a ver como utilizar algunos de los métodos del ciclo de vida de los
componentes.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-ciclo-de-vida-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Empezaremos creando el componente CajaColor en el que vamos a utilizar un par de métodos del
ciclo de vida de los componentes.

Este componente va a ser de clase porque queremos utilizar los métodos del ciclo de vida. También
va a necesitar un estado en el que vamos a indicar de que color pintar la caja, que inicialmente
vamos a dejar como null.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/CajaColor.tsx`

```tsx
import { Component } from 'react'

class CajaColor extends Component {
  constructor(props) {
    super(props);
    this.state = {
      color: null
    }
  }

    render() {
      console.log('Se ha vuelto a pintar...');
      return (
        <div style={{
          width: '100px',
          height: '100px',
          backgroundColor: this.state.color,
        }}></div>
      )
    }
}

export default CajaColor;
```
El color de la caja va a depender de un valor numérico que va a recibir como propiedad desde el
componente App. La idea es que si el número es positivo, la caja se pinte en verde, mientras que si
es negativo se pintará en rojo.

Así que el primer método que vamos a utilizar dentro de este componente es el
getDerivedStateFromProps ya que como hemos dicho, el estado depende de un valor que se
recibe como propiedad.

En este método recibimos como parámetros las propiedades y el estado. Accederemos a la
propiedad del num y haremos que se devuelva un objeto con la parte del estado que queremos
inicializar en base al valor de la propiedad.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/CajaColor.tsx`

```tsx
import { Component } from 'react'

class CajaColor extends Component {
  constructor(props) {
    super(props);
    this.state = {
      color: null
    }
  }
```
static getDerivedStateFromProps(props, state) {
```tsx
  return {
    color: props.num < 0 ? 'red' : 'green'
  }
}

    render() {
      console.log('Se ha vuelto a pintar...');
      return (
        <div style={{
          width: '100px',
          height: '100px',
          backgroundColor: this.state.color,
        }}></div>
      )
    }
}

export default CajaColor;
```
Ahora vamos al componente App en el que crearemos un contador para cambiar un valor
numérico que pasaremos como propiedad a este componente.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/App.tsx`

```tsx
import { useState } from "react"
import CajaColor from "./CajaColor"

const App = () => {
  const [cantidadTotal, setCantidadTotal] = useState(0);

return (
  <div>
    <div>
      <label htmlFor="cantidadTotal">Introduce la cantidad total:</label>
      <input type="number" name="cantidadTotal" id="cantidadTotal" value={cantidadTotal} onChange={(e) =>
```
setCantidadTotal(e.target.value)} />
```tsx
      </div>
      <CajaColor num={cantidadTotal} />
    </div>
  )
}

export default App
```
Si vamos al navegador a probar estos componentes, veremos que la caja se pinta de verde o rojo
dependiendo del valor que introduzcamos en el campo de texto.

Pero tenemos un problema y es que si el número pasa de un valor positivo a otro positivo o de uno
negativo a otro negativo, el componente se vuelve a renderizar sin mostrar ningún cambio
significativo.

Vamos a solucionar este problema con el método shouldComponentUpdate el cual recibe las
siguientes propiedades y el siguiente estado como parámetros.

Usaremos el siguiente estado para compararlo con el actual. En caso de que sean distintos
```tsx
devolveremos un true para indicarle a React que tiene que renderizar el componente, pero en caso
de que sean iguales devolveremos un false porque el color no ha cambiado y por tanto no hace falta
```
volver a renderizar el componente.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/CajaColor.tsx`

```tsx
import { Component } from 'react'

class CajaColor extends Component {
  constructor(props) {
    super(props);
    this.state = {
      color: null
    }
  }
```
static getDerivedStateFromProps(props, state) {
```tsx
  return {
    color: props.num < 0 ? 'red' : 'green'
  }
}
```
shouldComponentUpdate(nextProps, nextState) {
```tsx
  return this.state.color !== nextState.color;
}

    render() {
      console.log('Se ha vuelto a pintar...');
      return (
        <div style={{
          width: '100px',
          height: '100px',
          backgroundColor: this.state.color,
        }}></div>
      )
    }
}

export default CajaColor;
```
Ahora solo deberíamos de ver por consola el mensaje de Se ha vuelto a pintar… cuando pasamos
de un número negativo a uno positivo o viceversa.

Para ver otros dos métodos del ciclo de vida, estos son de los más utilizados en React, vamos a crear
otro componente HoraActual.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/HoraActual.tsx`

```tsx
import { Component } from 'react'

class HoraActual extends Component {
  constructor(props) {
    super(props);
  }

render() {
  return (
    <div>

            </div>
        )
    }
}

export default HoraActual
```
Dentro del componente vamos a pintar la hora actual y para ello vamos a añadirla en el estado del
componente.

En el método render llamaremos al método toLocaleTimeString de la fecha para mostrar solo la
hora.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/HoraActual.tsx`

```tsx
import { Component } from 'react'

class HoraActual extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fechaActual: new Date(),
    }
  }

    render() {
      return (
        <div>
          <p>{this.state.fechaActual.toLocaleTimeString()}</p>
        </div>
      )
    }
}

export default HoraActual
```
Ahora tenemos que conseguir que cada segundo que pase, la fecha se vaya actualizando para que
se muestre la hora actual, y aquí es donde entra el primer método del ciclo de vida que vamos a
usar.

Añadimos el componentDidMount en el que crearemos un timer que se ejecutará cada segundo y
que irá modificando la fecha del estado.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/HoraActual.tsx`

```tsx
import { Component } from 'react'

class HoraActual extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fechaActual: new Date(),
    }
  }
```
componentDidMount() {
```tsx
  const intervalId = setInterval(() => {
    console.log('Pidiendo la hora actual...')
    this.setState({
       fechaActual: new Date()
    })
  }, 1000);
}

render() {
  return (

            <div>
              <p>{this.state.fechaActual.toLocaleTimeString()}</p>
            </div>
        )
    }
}

export default HoraActual
```
Ya deberíamos de ver en la aplicación la hora actualizándose cada segundo que pasa. Parece que ya
tenemos lo que queríamos, pero no está hecho del todo bien. ¿Qué pasaría si borramos el
componente y lo volvemos a crear?

Vamos a verlo. Para ello, en el componente App, vamos a añadir un botón para crear o eliminar
este componente. Este botón modificará el estado del componente, un booleano que indica si se
muestra o no la hora.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/App.tsx`

```tsx
import { useState } from 'react'
import CajaColor from './CajaColor'
import HoraActual from './HoraActual'

const App = () => {
  const [cantidadTotal, setCantidadTotal] = useState(0);
  const [mostrarHoraActual, setMostrarHoraActual] = useState(true);

return (
  <div>
    <div>
      <label htmlFor="cantidadTotal">Introduce la cantidad total:</label>
      <input type="number" name="cantidadTotal" id="cantidadTotal" value={cantidadTotal} onChange={(e) =>
```
setCantidadTotal(e.target.value)} />
```tsx
      </div>
      <CajaColor num={cantidadTotal} />
      <button type="button" onClick={() => setMostrarHoraActual(!mostrarHoraActual)}>Toggle HoraActual</button>
      <HoraActual />
    </div>
  )
}

export default App
```
Ahora vamos a utilizar el renderizado condicional de React para mostrar HoraActual cuando sea
necesario.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/App.tsx`

```tsx
import { useState } from 'react'
import CajaColor from './CajaColor'
import HoraActual from './HoraActual'

const App = () => {
  const [cantidadTotal, setCantidadTotal] = useState(0);
  const [mostrarHoraActual, setMostrarHoraActual] = useState(true);

return (

<div>
  <div>
    <label htmlFor="cantidadTotal">Introduce la cantidad total:</label>
    <input type="number" name="cantidadTotal" id="cantidadTotal" value={cantidadTotal} onChange={(e) =>
```
setCantidadTotal(e.target.value)} />
```tsx
      </div>
      <CajaColor num={cantidadTotal} />
      <button type="button" onClick={() => setMostrarHoraActual(!mostrarHoraActual)}>Toggle HoraActual</button>
      {mostrarHoraActual && <HoraActual />}
    </div>
  )
}

export default App
```
Si pulsamos varias veces el botón, el componente se va a crear y se va a eliminar varias veces. El
problema con ello es que si miramos la consola del navegador, seguramente veamos que nos
muestra un warning, además de que el mensaje que estamos pintando dentro del setInterval se
muestra muchas más veces de las que debería de mostrarse.

Esto se debe a que estamos acumulando timers cada vez que volvemos a crear el componente de
HoraActual, pero no los estamos eliminando al desmontar el componente.

Para solucionarlo vamos a utilizar el método componentWillUnmount en el que llamaremos a la
función de clearInterval para eliminar el timer que se ha creado.

El método anterior necesita recibir como parámetro el identificador del intervalo, por lo que
tendremos que guardarlo también en el estado.

**Archivo:** `/reactjs-ciclo-de-vida-lab/src/components/HoraActual.tsx`

```tsx
import { Component } from 'react'

class HoraActual extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fechaActual: new Date(),
      intervalId: null
    }
  }
```
componentDidMount() {
```tsx
const intervalId = setInterval(() => {
  console.log('Pidiendo la hora actual...')
  this.setState({
     fechaActual: new Date()
  })
}, 1000);
```
this.setState({

intervalId
```tsx
    })
}
```
componentWillUnmount() {
```tsx
  clearInterval(this.state.intervalId);
}

    render() {
      return (
        <div>
          <p>{this.state.fechaActual.toLocaleTimeString()}</p>
        </div>
      )
    }
}

export default HoraActual
```
Ahora ya podemos decir que este componente está funcionando correctamente y si pulsamos varias
veces el botón que hemos añadido antes podemos ver la diferencia, ahora solo tendremos un solo
timer ejecutándose en la aplicación.