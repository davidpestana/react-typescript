# 21.1. Lab Referencias

**PDF: páginas 101–108** (libro: 97–104)

---

[← Índice](README.md) | [← Anterior: 21. Referencias](21-00-referencias.md) | [Siguiente: 22. Propiedad Children →](22-00-propiedad-children.md)

---

En este laboratorio vamos a crear los controles de reproducción de la etiqueta `<audio>` utilizando las
referencias de React **en componentes funcionales con TypeScript**. Podremos realizar las siguientes acciones:

- Reproducir el sonido
- Pausar el sonido
- Cambiar el volumen

Vamos a suponer que ya tienes un proyecto de React con TypeScript funcionando (por ejemplo, creado con Vite)
y que solo necesitas añadir el componente que controla el audio.

Empezamos añadiendo en una carpeta `src/assets` el sonido que vamos a utilizar en el laboratorio,
por ejemplo `sonido-piolin.mp3`, pero puedes usar cualquier otro archivo de sonido que tengas a mano.

---

## Crear el componente `App` con referencias

Vamos a crear un componente funcional `App` que:

- Tenga un **estado** `volumen` entre 0 y 100.
- Use una **referencia** para acceder al elemento `<audio>`.
- Tenga tres manejadores:
  - `handlePlay` → llama a `audio.play()`.
  - `handlePause` → llama a `audio.pause()`.
  - `handleChangeVolume` → actualiza el estado y el volumen real del audio.

**Archivo (por ejemplo):** `src/App.tsx`

```tsx
import { useRef, useState, ChangeEvent } from 'react'
import sonidoPiolin from './assets/sonido-piolin.mp3'

const App = () => {
  const [volumen, setVolumen] = useState(100)
  const audioRef = useRef<HTMLAudioElement | null>(null)

  const handlePlay = () => {
    audioRef.current?.play()
  }

  const handlePause = () => {
    audioRef.current?.pause()
  }

  const handleChangeVolume = (event: ChangeEvent<HTMLInputElement>) => {
    const nuevoVolumen = Number(event.target.value)
    setVolumen(nuevoVolumen)

    if (audioRef.current) {
      audioRef.current.volume = nuevoVolumen / 100
    }
  }

  return (
    <div>
      <audio ref={audioRef} src={sonidoPiolin} />

      <button type="button" onClick={handlePlay}>
        Play
      </button>

      <button type="button" onClick={handlePause}>
        Pause
      </button>

      <input
        type="range"
        min="0"
        max="100"
        value={volumen}
        onChange={handleChangeVolume}
      />
    </div>
  )
}

export default App
```

Con este componente:

- La referencia `audioRef` se asocia a la etiqueta `<audio>` mediante `ref={audioRef}`.
- `handlePlay` y `handlePause` usan `audioRef.current` para acceder al elemento DOM y llamar a
  los métodos `play()` y `pause()`.
- El input de tipo `range` está sincronizado con el estado `volumen`.
- En `handleChangeVolume`:
  - Leemos el nuevo valor del input.
  - Actualizamos el estado.
  - Convertimos ese valor (0–100) a un número entre 0 y 1 dividiéndolo entre 100 y lo asignamos a
    `audioRef.current.volume`.

Y con esto ya puedes utilizar tu panel de control para manejar archivos de audio (y podrías adaptarlo fácilmente para vídeo) usando **referencias en componentes funcionales**.

