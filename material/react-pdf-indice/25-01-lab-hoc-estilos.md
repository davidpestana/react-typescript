# 25.1. Lab Hoc Estilos

**PDF: páginas 124–129** (libro: 120–125)

---

En este laboratorio vamos a ver como crear un higher order component para añadir unos estilos
sobre los componentes y darles así el efecto de sombreado cuando pasamos el ratón por encima de
ellos.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-higher-order-components-
hover-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Vamos a empezar por crear un componente Boton dentro de la carpeta de components al que
después le aplicaremos los estilos con el HOC.

Este componente recibirá en las props el texto y el método que se ejecutará cuando se pulse sobre
el. Además, vamos a añadirle unos estilos en línea con JavaScript para que quede más curioso el
botón.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/components/Boton.jsx`

```tsx
const styles = {
  padding: '8px 12px',
  border: '1px solid black',
  borderRadius: '5px',
  backgroundColor: 'white'
}

const Boton = ({children, handleClick}) => {
  return (
    <button
      type="button"
      onClick={handleClick}
      style={styles}
    >
      {children}
    </button>
  )
}

export default Boton;
```
Una vez tenemos el botón ya podemos añadirlo en el componente App para mostrarlo.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/components/App.jsx`

```tsx
import Boton from './Boton';

const App = () => {
  return (
    <div>
      <Boton handleClick={() => alert('Hola mundo!!!')}>Saludar al mundo</Boton>
    </div>
  )
}

export default App
```
Ahora vamos a crear el HOC withHover en un archivo de JavaScript en una carpeta src/hoc.

Como ya sabemos, un HOC es una función a la que se le va a pasar el componente que queremos
envolver y añadirle una funcionalidad que no tiene. Por tanto empezamos creando esta función y
haciendo que esta devuelva el nuevo componente que queremos generar.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/hoc/withHover.js`

```tsx
const withHover = (WrappedCmp) => {
  return (props) => {
    return ()
  }
}

export default withHover;

Ahora dentro del return vamos a poner el componente que recibimos como parámetro y lo
```
envolveremos con una etiqueta div a la que le vamos a aplicar unos estilos.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/hoc/withHover.js`

```tsx
const withHover = (WrappedCmp) => {
  return (props) => {
    return (
      <div>
        <WrappedCmp />
      </div>
    )
  }
}

export default withHover;
```
Estos estilos dependerán de si el ratón está encima del botón o si está fuera de este. Por tanto,
vamos a necesitar un estado para controlar los estilos a aplicar.

```tsx
Importamos el hook de useState y creamos un estado del tipo booleano para indicar si el ratón está
```
encima o no.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/hoc/withHover.js`

```tsx
import { useState } from 'react';

const withHover = (WrappedCmp) => {
  return (props) => {
    const [isMouseOn, setIsMouseOn] = useState(false);

        return (
          <div>
            <WrappedCmp />
          </div>
        )
    }
}

export default withHover;
```
Ahora vamos a añadir dos eventos onMouseEnter y onMouseLeave para cambiar este estado de
valor.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/hoc/withHover.js`

```tsx
import { useState } from 'react';

const withHover = (WrappedCmp) => {
  return (props) => {
    const [isMouseOn, setIsMouseOn] = useState(false);

        return (
          <div
            onMouseEnter={() => setIsMouseOn(true)}
            onMouseLeave={() => setIsMouseOn(false)}
          >
            <WrappedCmp />
          </div>
        )
    }
}

export default withHover;
```
Para ir terminando con el HOC, tenemos que crear los estilos, que es un objeto donde pondremos la
propiedad opacity a 1 cuando el ratón está fuera del botón, y a 0.4 cuando está sobre el. También

vamos a hacer que se ajuste al contenido de la etiqueta con la propiedad width: 'max-content'.

Solo tenemos que asignarle el objeto con los estilos a la propiedad style del div.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/hoc/withHover.js`

```tsx
import { useState } from 'react';

const withHover = (WrappedCmp) => {
  return (props) => {
    const [isMouseOn, setIsMouseOn] = useState(false);

const styles = {
  opacity: isMouseOn ? '0.4' : '1',
  width: 'max-content'
}

        return (
          <div
            style={styles}
            onMouseEnter={() => setIsMouseOn(true)}
            onMouseLeave={() => setIsMouseOn(false)}
          >
            <WrappedCmp />
          </div>
        )
    }
}

export default withHover;
```
Ahora que ya tenemos el HOC creado, lo importamos en el componente App, donde vamos a crear
un componente BotonWithHover que se obtiene de envolver el componente Boton con el HOC.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/components/App.jsx`

```tsx
import withHover from '../hoc/withHover';
import Boton from './Boton';

const App = () => {
  const BotonWithHover = withHover(Boton);

    return (
      <div>
        <Boton handleClick={() => alert('Hola mundo!!!')}>Saludar al mundo</Boton>
      </div>
    )
}

export default App
```
Una vez que tenemos el nuevo componente, ya podemos pintarlo en nuestra aplicación pasandole
las propiedades que necesita.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/components/App.jsx`

```tsx
import withHover from '../hoc/withHover';
import Boton from './Boton';

const App = () => {
  const BotonWithHover = withHover(Boton);

    return (
      <div>
        <Boton handleClick={() => alert('Hola mundo!!!')}>Saludar al mundo</Boton>
        <BotonWithHover handleClick={() => alert('Bienvenid@s...')}>Dar bienvenida</BotonWithHover>
      </div>
    )
}

export default App
```
Si abrimos la aplicación en el navegador, http://localhost:8080 veremos algo como lo siguiente.

En la imagen podemos ver que el botón sobre el que hemos usado el HOC no muestra el texto que le
pasamos y si pulsamos sobre el tampoco ejecuta la función correspondiente. Esto se debe a que las
propiedades le están llegando al componente que estamos creando con el HOC, pero este no se las
está pasando al componente Boton.

Para hacérselas llegar al componente Boton y que de esta forma se muestre el texto del botón y se
ejecute la función al pulsar sobre el, le vamos a pasar al WrappedCmp todas las propiedades.

**Archivo:** `/reactjs-higher-order-components-hover-lab/src/hoc/withHover.js`

```tsx
import { useState } from 'react';

const withHover = (WrappedCmp) => {
  return (props) => {

const [isMouseOn, setIsMouseOn] = useState(false);

const styles = {
  opacity: isMouseOn ? '0.4' : '1',
  width: 'max-content'
}

        return (
          <div
            style={styles}
            onMouseEnter={() => setIsMouseOn(true)}
            onMouseLeave={() => setIsMouseOn(false)}
          >
            <WrappedCmp {...props} />
          </div>
        )
    }
}

export default withHover;
```
Ahora ya debería de verse todo correctamente, y si pasamos el ratón por encima del segundo botón
debería de aplicarse los estilos que añade sobre el nuestro HOC.
