# 21.1. Lab Referencias

**PDF: páginas 101–108** (libro: 97–104)

---

En este laboratorio vamos a crear los controles de reproducción de la etiqueta Audio utilizando las
```tsx
referencias de React. Podremos realizar las siguientes acciones:
```
- Reproducir el sonido

- Pausar el sonido

- Cambiar el volumen

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-refs-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Empezamos añadiendo en una carpeta src/assets el sonido que vamos a utilizar en el laboratorio,
yo usaré sonido-piolin.mp3, pero podéis usar cualquier otro archivo de sonido que tengáis a mano.

Vamos a empezar por crear el código HTML dentro del App para añadir los tres elementos con los
que controlaremos el audio.

**Archivo:** `/reactjs-refs-lab/src/components/App.jsx`

```tsx
import React, { Component } from 'react'

export default class App extends Component {
  constructor(props) {
    super(props);
  }

    render() {
      return (
        <div>
          <audio></audio>
          <button type="button">Play</button>
          <button type="button">Pause</button>
          <input type="range" min="0" max="100" />
        </div>
      )
    }
}
```
Ahora vamos a añadir las funciones y el estado que necesitaremos para manejar los controles.
Necesitaremos en el estado el valor del volumen, y luego tres funciones, una por cada control que
vamos a añadir.

**Archivo:** `/reactjs-refs-lab/src/components/App.jsx`

```tsx
import React, { Component } from 'react'

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      volumen: 100
    }
    this.handlePlay = this.handlePlay.bind(this);
    this.handlePause = this.handlePause.bind(this);
    this.handleChangeVolume = this.handleChangeVolume.bind(this);
  }
```
handlePlay() {

handlePause() {

handleChangeVolume() {

```tsx
    render() {
      return (
        <div>
          <audio></audio>
          <button type="button">Play</button>
          <button type="button">Pause</button>
          <input type="range" min="0" max="100" />
        </div>
      )
    }
}
```
El siguiente paso es crear la referencia y asignarla al atributo ref de la etiqueta audio.

**Archivo:** `/reactjs-refs-lab/src/components/App.jsx`

```tsx
import React, { Component } from 'react'

export default class App extends Component {
```
constructor(props) {
```tsx
  super(props);
  this.state = {
    volumen: 100
  }
  this.handlePlay = this.handlePlay.bind(this);
  this.handlePause = this.handlePause.bind(this);
  this.handleChangeVolume = this.handleChangeVolume.bind(this);
  this.refAudio = React.createRef(new Audio());
}
```
handlePlay() {

handlePause() {

handleChangeVolume() {

```tsx
    render() {
      return (
        <div>
          <audio ref={this.refAudio}></audio>
          <button type="button">Play</button>
          <button type="button">Pause</button>
          <input type="range" min="0" max="100" />
        </div>
      )
    }
}
```
También tenemos que añadir el src con el archivo de sonido. Para que Webpack genere los assets
correctamente en el proceso de construcción de la aplicación, tenemos que importar el archivo (al
igual que vimos con los archivos de estilos). El objeto que obtenemos al importar el sonido será el
valor que le vamos a dar al atributo src del audio.

**Archivo:** `/reactjs-refs-lab/src/components/App.jsx`

```tsx
import React, { Component } from 'react'
import sonidoPiolin from '../assets/sonido-piolin.mp3';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      volumen: 100

    }
    this.handlePlay = this.handlePlay.bind(this);
    this.handlePause = this.handlePause.bind(this);
    this.handleChangeVolume = this.handleChangeVolume.bind(this);
    this.refAudio = React.createRef(new Audio());
}
```
handlePlay() {

handlePause() {

handleChangeVolume() {

```tsx
    render() {
      return (
        <div>
          <audio src={sonidoPiolin} ref={this.refAudio}></audio>
          <button type="button">Play</button>
          <button type="button">Pause</button>
          <input type="range" min="0" max="100" />
        </div>
      )
    }
}
```
Ahora ya podemos dedicarnos a añadir la lógica de los botones e inputs que habíamos añadido al
principio.

Vamos a empezar por el botón de Play. Sobre dicho botón añadiremos el evento click para llamar a
la función handlePlay en la que mediante la referencia que tenemos vamos a llamar a la función
play de las etiquetas media.

**Archivo:** `/reactjs-refs-lab/src/components/App.jsx`

```tsx
import React, { Component } from 'react'
import sonidoPiolin from '../assets/sonido-piolin.mp3';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      volumen: 100
    }
    this.handlePlay = this.handlePlay.bind(this);

    this.handlePause = this.handlePause.bind(this);
    this.handleChangeVolume = this.handleChangeVolume.bind(this);
    this.refAudio = React.createRef(new Audio());
}
```
handlePlay() {
```tsx
  this.refAudio.current.play();
}
```
handlePause() {

handleChangeVolume(e) {

```tsx
    render() {
      return (
        <div>
          <audio src={sonidoPiolin} ref={this.refAudio}></audio>
          <button type="button" onClick={this.handlePlay}>Play</button>
          <button type="button">Pause</button>
          <input type="range" min="0" max="100" />
        </div>
      )
    }
}
```
El siguiente paso es hacer lo mismo con el botón de Pause llamando en este caso a la función
pause.

**Archivo:** `/reactjs-refs-lab/src/components/App.jsx`

```tsx
import React, { Component } from 'react'
import sonidoPiolin from '../assets/sonido-piolin.mp3';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      volumen: 100
    }
    this.handlePlay = this.handlePlay.bind(this);
    this.handlePause = this.handlePause.bind(this);
    this.handleChangeVolume = this.handleChangeVolume.bind(this);
    this.refAudio = React.createRef(new Audio());
  }
```
handlePlay() {

```tsx
    this.refAudio.current.play();
}
```
handlePause() {
```tsx
  this.refAudio.current.pause();
}
```
handleChangeVolume(e) {

```tsx
    render() {
      return (
        <div>
          <audio src={sonidoPiolin} ref={this.refAudio}></audio>
          <button type="button" onClick={this.handlePlay}>Play</button>
          <button type="button" onClick={this.handlePause}>Pause</button>
          <input type="range" min="0" max="100" />
        </div>
      )
    }
}
```
Con esto ya deberíamos de poder hacer que suene el sonido y pausarlo pulsando sobre esos dos
botones.

Vamos a por el volumen. En el input con el que vamos a controlar el volumen del sonido le vamos a
dar como valor aquel que tenemos guardado en el estado, y añadiremos el evento change para
llamar a la función que controlará el volumen cada vez que se cambie el valor del input.

**Archivo:** `/reactjs-refs-lab/src/components/App.jsx`

```tsx
import React, { Component } from 'react'
import sonidoPiolin from '../assets/sonido-piolin.mp3';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      volumen: 100
    }
    this.handlePlay = this.handlePlay.bind(this);
    this.handlePause = this.handlePause.bind(this);
    this.handleChangeVolume = this.handleChangeVolume.bind(this);
    this.refAudio = React.createRef(new Audio());
  }
```
handlePlay() {
```tsx
  this.refAudio.current.play();
}
```
handlePause() {
```tsx
  this.refAudio.current.pause();
}
```
handleChangeVolume(e) {

```tsx
    render() {
      return (
        <div>
          <audio src={sonidoPiolin} ref={this.refAudio}></audio>
          <button type="button" onClick={this.handlePlay}>Play</button>
          <button type="button" onClick={this.handlePause}>Pause</button>
          <input type="range" min="0" max="100" value={this.state.volumen} onChange={this.handleChangeVolume} />
        </div>
      )
    }
}
```
En la función de handleChangeVolume tenemos el evento que ha ocurrido del cual vamos a
obtener el valor del input que setearemos como nuevo valor del estado.

Al mismo tiempo cambiaremos el valor del volumen del audio mediante la referencia. Para ello le
asignamos al atributo volume un valor entre 0 y 1, por lo que el valor que hemos recibido del input
tendremos que dividirlo entre 100 para asignarle un valor que se encuentre entre los parámetros
que acepta.

**Archivo:** `/reactjs-refs-lab/src/components/App.jsx`

```tsx
import React, { Component } from 'react'
import sonidoPiolin from '../assets/sonido-piolin.mp3';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      volumen: 100
    }
    this.handlePlay = this.handlePlay.bind(this);
    this.handlePause = this.handlePause.bind(this);
    this.handleChangeVolume = this.handleChangeVolume.bind(this);
    this.refAudio = React.createRef(new Audio());
  }
```
handlePlay() {
```tsx
  this.refAudio.current.play();
}
```
handlePause() {
```tsx
  this.refAudio.current.pause();
}
```
handleChangeVolume(e) {
```tsx
const volumen = e.target.value;
```
this.refAudio.current.volume = volumen / 100;
this.setState({
volumen
```tsx
  })
}

render() {

        return (
          <div>
            <audio src={sonidoPiolin} ref={this.refAudio}></audio>
            <button type="button" onClick={this.handlePlay}>Play</button>
            <button type="button" onClick={this.handlePause}>Pause</button>
            <input type="range" min="0" max="100" value={this.state.volumen} onChange={this.handleChangeVolume} />
          </div>
        )
    }
}
```
Y con esto ya podemos utilizar nuestro panel de control para manejar los archivos media como
audio y video que queramos.
