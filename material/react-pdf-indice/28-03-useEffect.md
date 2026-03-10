# 28.3. Useeffect

**PDF: páginas 151–152** (libro: 147–148)

---

```tsx
El hook useEffect es el hook que viene a sustituir a algunos de los métodos del ciclo de vida de los
```
componentes, en concreto viene a sustituir a:

- componentDidMount

- componentDidUpdate

- componentWillUnmount

Este hook, se ejecuta justo después de cada render, es decir, cuando se terminar de ejecutar

Este hook recibe como parámetro una función que es la que se va a ejecutar cada vez que se
renderice el componente, es decir, como si se estuvieran ejecutando componentDidMount y
componentDidUpdate.

Dentro de esta función será donde pondremos las suscripciones, timers, peticiones AJAX…

```tsx
useEffect(() => {
   // ...
})
```
Pero hay que tener cuidado con este hook, ya que puede provocar problemas de memoria porque la
función se estará ejecutando cada vez que el componente se renderice.

Esto lo solucionamos pasandole un segundo parámetro al hook. Tenemos las siguientes
posibilidades:

- Un array vacio: solo se ejecuta en el primer renderizado.

- Un array con el nombre de propiedades: solo se ejecuta si cambia alguna de estas propiedades.

- No le pasamos nada: se ejecuta cada vez que se renderiza el componente.

```tsx
useEffect(() => {
  // ...
}, [texto])
```
Y por último, para realizar las tareas de limpieza en el componente, como desuscribirnos de
eventos o eliminar los timers, aquellas que haríamos en dentro del componentWillUnmount, hay
que devolver una función dentro de la función que le hemos pasado al hook.

```tsx
useEffect(() => {
  // ...
  return () => {
    // ...
  }
}, [texto])
```
Una ventaja de este hook frente a los métodos del ciclo de vida de los componentes con clase es que
podemos usarlo varias veces separandolo por efectos de tal forma que el código queda más límpio
sin tener que llenar la función de condicionales que controlen si hay que ejecutar cierto código o
no.

```tsx
useEffect(() => {
  // Efecto 1
}, [])

useEffect(() => {
  // Efecto 2
}, [nombre])
```
