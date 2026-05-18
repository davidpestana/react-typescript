# 21. Referencias

**PDF: páginas 100–100** (libro: 96–96)

---

[← Índice](README.md) | [← Anterior: 20.8. Lab Ciclo Vida](20-08-lab-ciclo-vida.md) | [Siguiente: 21.1. Lab Referencias →](21-01-lab-referencias.md)

---

## Referencias

Las referencias de React nos permiten acceder a los elementos del DOM. Equivaldrían a utilizar
métodos como `getElementById` o `querySelector` del objeto `window.document`, pero como aquí
estamos trabajando con un Virtual DOM, tenemos que evitar esos métodos a toda costa ya que
pueden llegar a darnos algún problema.

Con las referencias, al poder acceder a los elementos HTML que se renderizan con los
componentes, podremos leer y modificar los atributos de estos.

Antes de ponernos a crear referencias en nuestros componentes, para poder acceder a ellos,
tenemos que pensar en que si una etiqueta HTML necesita ser cambiada, lo más recomendable
sería cambiar el valor del estado para que vuelva a renderizarse con el nuevo valor. **Solo
deberíamos usar las referencias cuando no tenemos otra forma de modificar dichos elementos.**

En componentes funcionales, para crear una referencia usamos el **hook `useRef`**.

```tsx
import { useRef } from 'react'

const MiComponente = () => {
  const miReferencia = useRef<HTMLInputElement | null>(null)

  const handleClick = () => {
    if (miReferencia.current) {
      console.log(miReferencia.current.value)
    }
  }

  return (
    <div>
      <input type="text" ref={miReferencia} />
      <button type="button" onClick={handleClick}>
        Leer valor
      </button>
    </div>
  )
}
```

En este ejemplo:

- Creamos la referencia con `useRef<HTMLInputElement | null>(null)`.
- La asociamos al input mediante el atributo `ref={miReferencia}`.
- Cuando pulsamos el botón, accedemos al elemento real del DOM con
  `miReferencia.current` y leemos su valor.  
  Siempre comprobamos antes que `current` no sea `null`.