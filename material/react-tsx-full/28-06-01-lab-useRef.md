# 28.6.1. Lab Useref

**PDF: páginas 169–175** (libro: 165–171)

---

[← Índice](README.md) | [← Anterior: 28.5. Usememo](28-05-useMemo.md) | [Siguiente: 28.6. Useref →](28-06-useRef.md)

---

En este laboratorio vamos a crear un panel de control para trabajar con la etiqueta audio y con el
cual vamos a poder reproducir, pausar y modificar el volumen.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial y vamos a cambiarle el nombre del proyecto a reactjs-hooks-useref-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Para este laboratorio necesitamos usar cualquier archivo de audio, que hay que meter dentro de la
carpeta dist/assets del proyecto.

Una vez que tenemos el proyecto vamos a empezar creando un nuevo componente funcional
AudioPlayer en la carpeta components.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/AudioPlayer.tsx`

```tsx
import React, { useRef } from 'react'

const AudioPlayer = () => {
  return (
    <div>
      <audio src="/assets/sonido-piolin.m4a" />
      <button type="button">Play</button>
      <button type="button">Pause</button>
      <input type="range" name="volume" id="volume" />
    </div>
  )
}

export default AudioPlayer
```
El siguiente paso es añadir el componente que hemos creado en el componente raíz de la
aplicación.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/App.tsx`

```tsx
import React, { Component } from 'react'
import AudioPlayer from './AudioPlayer'

class App extends Component {
  render() {
    return (
      <div>
        <AudioPlayer />
      </div>
    )

    }
}

export default App
```
Ahora vamos a usar el hook de useRef para añadir una referencia a la etiqueta de audio del
componente para poder acceder a todas sus funcionalidades. Para ello solo tenemos que importar
el hook, y pasarle a una propiedad ref de la etiqueta audio la referencia que nos ha devuelto el
hook.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/AudioPlayer.tsx`

```tsx
import React, { useRef } from 'react'

const AudioPlayer = () => {
  const audioRef = useRef(null);

    return (
      <div>
        <audio src="/assets/sonido-piolin.m4a" ref={audioRef} />
        <button type="button">Play</button>
        <button type="button">Pause</button>
        <input type="range" name="volume" id="volume" />
      </div>
    )
}

export default AudioPlayer
```
Pues el siguiente paso es añadir la funcionalidad a los botones y al input para poder controlar el
sonido que hayamos puesto.

Empezamos por crearnos una función para reproducir la canción cuando pulsemos el primer
botón. En esta función vamos a coger la referencia que nos ha devuelto el hook, accederemos a
current y ejecutaremos la función play de la etiqueta audio para reproducir el audio.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/AudioPlayer.tsx`

```tsx
import React, { useRef } from 'react'

const AudioPlayer = () => {
  const audioRef = useRef(null);

const play = () => {
  audioRef.current.play();
}

return (
  <div>
    <audio src="/assets/sonido-piolin.m4a" ref={audioRef} />

          <button type="button">Play</button>
          <button type="button">Pause</button>
          <input type="range" name="volume" id="volume" />
        </div>
    )
}

export default AudioPlayer
```
Ahora haremos lo mismo pero creando una función pause en la que llamaremos al método pause
de la referencia a la etiqueta audio.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/AudioPlayer.tsx`

```tsx
import React, { useRef } from 'react'

const AudioPlayer = () => {
  const audioRef = useRef(null);

const play = () => {
  audioRef.current.play();
}

const pause = () => {
  audioRef.current.pause();
}

    return (
      <div>
        <audio src="/assets/sonido-piolin.m4a" ref={audioRef} />
        <button type="button">Play</button>
        <button type="button">Pause</button>
        <input type="range" name="volume" id="volume" />
      </div>
    )
}

export default AudioPlayer
```
El siguiente paso es pasarle una referencia de estas dos funciones a los enventos onClick de cada
uno de los botones.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/AudioPlayer.tsx`

```tsx
import React, { useRef } from 'react'

const AudioPlayer = () => {
  const audioRef = useRef(null);

const play = () => {

    audioRef.current.play();
}

const pause = () => {
  audioRef.current.pause();
}

    return (
      <div>
        <audio src="/assets/sonido-piolin.m4a" ref={audioRef} />
        <button type="button" onClick={play}>Play</button>
        <button type="button" onClick={pause}>Pause</button>
        <input type="range" name="volume" id="volume" />
      </div>
    )
}

export default AudioPlayer
```
Ahora ya deberíamos de poder reproducir y pausar el sonido.

Lo siguiente es añadir la funcionalidad para poder cambiar el volumen del audio. Lo primero que
necesitamos es añadir un estado para guardar el valor del volumen y cambiarlo al mover el slider
del input. El valor inicial del estado lo vamos a obtener de la propiedad volume que obtenemos a
partir de la referencia.

La propiedad volume de las etiquetas audio y video coge un valor entre 0 y 1.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/AudioPlayer.tsx`

```tsx
import React, { useRef } from 'react'

const AudioPlayer = () => {
  const audioRef = useRef(null);
  const [volume, setVolume] = useState(audioRef.current.volume * 100)

const play = () => {
  audioRef.current.play();
}

const pause = () => {
  audioRef.current.pause();
}

return (
  <div>
    <audio src="/assets/sonido-piolin.m4a" ref={audioRef} />
    <button type="button" onClick={play}>Play</button>
    <button type="button" onClick={pause}>Pause</button>
    <input type="range" name="volume" id="volume" />

        </div>
    )
}

export default AudioPlayer
```
Antes de continuar, si miramos la consola del navegador, nos mostrará un error indicando que no
puede acceder a la propiedad volume de null. Esto se debe a que la referencia la hemos
inicializado con null, y por tanto no tiene propiedades a las que acceder. Para solucionarlo, vamos
a incializar esta referencia con una instancia de la clase Audio que es con la que se construyen las
etiquetas de este tipo, y la cual nos proporcionará acceso a todas las propiedades iniciales que tiene
esta etiqueta.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/AudioPlayer.tsx`

```tsx
import React, { useRef } from 'react'

const AudioPlayer = () => {
  const audioRef = useRef(new Audio());
  const [volume, setVolume] = useState(audioRef.current.volume * 100)

const play = () => {
  audioRef.current.play();
}

const pause = () => {
  audioRef.current.pause();
}

    return (
      <div>
        <audio src="/assets/sonido-piolin.m4a" ref={audioRef} />
        <button type="button" onClick={play}>Play</button>
        <button type="button" onClick={pause}>Pause</button>
        <input type="range" name="volume" id="volume" />
      </div>
    )
}

export default AudioPlayer
```
Solucionado este error, vamos a darle el valor al input y vamos a añadir el evento onChange que
llamará a la función changeVolume que vamos a crear a continuación.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/AudioPlayer.tsx`

```tsx
import React, { useRef } from 'react'

const AudioPlayer = () => {
  const audioRef = useRef(new Audio());

const [volume, setVolume] = useState(audioRef.current.volume * 100)

const play = () => {
  audioRef.current.play();
}

const pause = () => {
  audioRef.current.pause();
}

    return (
      <div>
        <audio src="/assets/sonido-piolin.m4a" ref={audioRef} />
        <button type="button" onClick={play}>Play</button>
        <button type="button" onClick={pause}>Pause</button>
        <input type="range" name="volume" id="volume" min="0" max="100" value={volume} onChange={changeVolume} />
      </div>
    )
}

export default AudioPlayer
```
Esta función que se va a ejecutar cuando vayamos moviendo el slider del volument lo que tiene que
hacer es acceder al valor del input a partir del evento que recibimos como parámetro y cambiar la
propiedad volume de la referencia y el estado.

**Archivo:** `/reactjs-hooks-useref-lab/src/components/AudioPlayer.tsx`

```tsx
import React, { useRef } from 'react'

const AudioPlayer = () => {
  const audioRef = useRef(new Audio());
  const [volume, setVolume] = useState(audioRef.current.volume * 100)

const play = () => {
  audioRef.current.play();
}

const pause = () => {
  audioRef.current.pause();
}

const changeVolume = (e) => {
  const newVolume = e.target.value;
  audioRef.current.volume = newVolume / 100;
  setVolume(newVolume);
}

    return (
      <div>
        <audio src="/assets/sonido-piolin.m4a" ref={audioRef} />
        <button type="button" onClick={play}>Play</button>
        <button type="button" onClick={pause}>Pause</button>
        <input type="range" name="volume" id="volume" min="0" max="100" value={volume} onChange={changeVolume} />
      </div>
    )
}

export default AudioPlayer
```
Y con esto ya deberíamos de ser capaces de cambiar el volumen del audio.