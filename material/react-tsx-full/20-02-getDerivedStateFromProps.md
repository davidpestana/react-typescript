# 20.2. Getderivedstatefromprops

**PDF: páginas 86–86** (libro: 82–82)

---

[← Índice](README.md) | [← Anterior: 20.1. Constructor](20-01-constructor.md) | [Siguiente: 20.3. Componentdidmount →](20-03-componentDidMount.md)

---

El método static getDerivedStateFromProps es un método que se va a ejecutar justo antes de
ejecutar el método de render de los componentes. Se ejecuta tanto al montar el componente como
al actualizarlo.

En este método recibimos las propiedades y el estado que vamos a tener después de renderizar el
componente por lo que podremos compararlas con las propiedades y estado actuales del
componente para calcular si el estado se tiene que modificar o no.

Si la función devuelve un null no se actualiza nada, pero si devolvemos un objeto, este actualizará
el estado del componente.

Es un método del ciclo de vida avanzado y que no se suele utilizar mucho, pero tendremos que
usarlo cuando el valor del estado depende del valor de alguna de las propiedades que recibe el
componente.

static getDerivedStateFromProps(props, state) {
```tsx
  return {
    texto: props.number % 2 === 0 ? 'es par' : 'es impar'
  }
}
```