# 9. Qué es TSX

**PDF: páginas 34–36** (libro: 30–32)

---

[← Índice](README.md) | [← Anterior: 8.1. Lab Proyecto Inicial Desde 0](08-01-lab-proyecto-inicial-desde-0.md) | [Siguiente: 10. Componente sin TSX →](10-00-componente-sin-jsx.md)

---

## ¿Qué es TSX?

El equipo de Facebook también liberaron TSX al mismo tiempo que React, que provee de una
sintaxis para crear estructuras del DOM complejas con atributos. TSX es una extensión de JavaScript
que nos permite crear los componentes React usando una sintaxis similar a HTML (se podría decir
que es HTML incrustado en JavaScript). La sintaxis de TSX nos permite visualizar de una forma mas rápida
la estructura de nuestro componente. Para usar React no es necesario usar TSX pero lo hace más
fácil. Todo este código lo tenemos que poner en el método render que es el método más importante
```tsx
de los componentes React. Lo que devuelve este método es lo que finalmente vamos a ver.
```
Componente Input

```tsx
import React, { Component } from 'react';

class Input extends Component {
  const { type, maxLength, clases } = this.props;
  render() {
    return (
      <input type={ type } maxLength={ maxLength } className={ clases } />
    )
  }

export default Input;

En TSX se pueden usar etiquetas HTML o componentes propios creados con React. Por convención
```
los componentes propios tienen que empezar por mayúscula mientras que las etiquetas HTML se
escriben igual que en HTMl. Las etiquetas tienen que estar balanceadas, que significa que si
```tsx
abrimos una etiqueta, luego la tenemos que cerrar, y en el caso de algunas etiquetas como <br> que
no necesitan etiqueta de cierre se tienen que cerrar ellas mismas <br/>.
```
Etiqueta HTML

```tsx
<input type="text" />
```
Etiqueta TSX

```tsx
<input type="text" />
```
Etiqueta de componente de React

```tsx
<Input type="text" />
```
También se pueden poner atributos a los elementos HTML, y la norma es que si el nombre del
atributo contiene más de una palabra, este se escribe en camelCase. Hay dos excepciones, los
```tsx
atributos class y for se escriben como className y htmlFor en TSX. Y si los atributos pertenecen a
```
un componente de React, estos los define el propio componente y son libres (les podemos poner el
nombre que queramos). El valor de los atributos tiene que ir entre comillas "" (en caso de que sea
un string) o entre llaves {} (para cualquier otro valor).

Etiqueta HTML

```tsx
<input type="text" maxlength="15" class="borde-rojo" />
```
Etiqueta TSX

```tsx
<input type="text" maxLength={15} className="borde-rojo" />
```
Etiqueta de componente de React

```tsx
<Input type="text" maxLength={15} />
```
Los componentes de React solo pueden renderizar un nodo raíz.

Nodo raíz TSX válido

render () {
```tsx
  return <h1>Hola mundo</h1>
}
```
El siguiente caso no se puede dar:

Nodo raíz TSX inválido

render () {
```tsx
  return (
    <h1>Hola mundo</h1>
    <h1>Hola mundo de nuevo</h1>
  )
}
```
Se puede solucionar metiendo los dos elementos h1 dentro de un elemento div y de esta forma ya se
estaría devolviendo un solo nodo raíz que tiene elementos hijos.

Nodo raíz TSX válido

render () {
```tsx
return (
  <div>
    <h1>Hola mundo</h1>
    <h1>Hola mundo de nuevo</h1>
  </div>
)
```
Esto se debe a que cuando transforma el código TSX a JavaScript, React solo puede crear un elemento para
devolverlo.

Nodo raiz JS

```tsx
render() {
  return React.createElement('div', null,
             React.createElement('h1', null, 'Hola mundo'),
             React.createElement('h1', null, 'Hola mundo de nuevo')
           )
}
```