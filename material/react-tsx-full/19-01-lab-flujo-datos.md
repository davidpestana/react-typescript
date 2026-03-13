# 19.1. Lab Flujo Datos

**PDF: _por definir_**

---

[← Índice](README.md) | [← Anterior: 19. Flujo Datos](19-00-flujo-datos.md) | [Siguiente: 20. Ciclo Vida →](20-00-ciclo-vida.md)

---

En este laboratorio vamos a practicar el **flujo de datos unidireccional** haciendo que:

- El **padre** tenga el **estado** con el número de clicks totales.
- El **hijo** muestre un botón y gestione el **evento de click**.
- El hijo llame a una **función que recibe por props** para avisar al padre de cada click, enviando la **cantidad de clicks** que lleva acumulados.
- El padre actualice su estado y se lo vuelva a pasar al hijo.

La idea es ver claramente el patrón de: **los datos bajan (props), los eventos suben (callbacks)**.

---

## Crear el componente hijo `ClickCounterButton`

Vamos a crear un componente hijo que será el encargado de:

- Mostrar un botón.
- Contar cuántas veces se ha pulsado ese botón.
- Avisar al componente padre cada vez que se pulse, enviando el **nuevo total de clicks**.

**Archivo (por ejemplo):** `src/components/ClickCounterButton.tsx`

```tsx
import React, { useState } from 'react'

type Props = {
  onClickCountChange: (totalClicks: number) => void
}

const ClickCounterButton: React.FC<Props> = ({ onClickCountChange }) => {
  const [clicks, setClicks] = useState(0)

  const handleClick = () => {
    const nuevoTotal = clicks + 1
    setClicks(nuevoTotal)
    onClickCountChange(nuevoTotal)
  }

  return (
    <button type="button" onClick={handleClick}>
      He sido pulsado {clicks} veces (hijo)
    </button>
  )
}

export default ClickCounterButton
```

---

## Usar el componente hijo desde tu componente padre

En tu componente padre actual (por ejemplo, `App.tsx`) añade un estado con el total de clicks y pasa una función al hijo para que pueda avisar hacia arriba:

```tsx
import { useState } from 'react'
import ClickCounterButton from './components/ClickCounterButton'

const App = () => {
  const [totalClicks, setTotalClicks] = useState(0)

  const handleChildClickCountChange = (totalClicksFromChild: number) => {
    setTotalClicks(totalClicksFromChild)
  }

  return (
    <div>
      <h1>Flujo de datos</h1>
      <p>Total de clicks (padre): {totalClicks}</p>

      <ClickCounterButton
        onClickCountChange={handleChildClickCountChange}
      />
    </div>
  )
}

export default App
```

No hace falta que crees un proyecto nuevo para este lab: puedes integrar este ejemplo en el proyecto de React + TypeScript que ya estés utilizando en el curso.


## ¿Qué estamos practicando?

En este laboratorio has practicado:

- Mantener el **estado en el componente padre**.
- Pasar una **función como prop** desde el padre al hijo.
- Que el **hijo gestione el evento de click** y llame a esa función, enviando **datos hacia arriba** (el número de clicks).
- Actualizar el estado en el padre con `setState` y volver a **propagar el nuevo valor hacia abajo** mediante props.

Este patrón es la base del **flujo de datos unidireccional** en React:  
**los datos bajan (props), los eventos suben (callbacks)**.

