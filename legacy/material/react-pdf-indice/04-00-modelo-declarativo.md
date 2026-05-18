# 4. Modelo Declarativo

**PDF: páginas 11–12** (libro: 7–8)

---

## Modelo declarativo

React sigue el paradigma de la programación declarativa, es decir, aquella donde las aplicaciones se
estructuran de forma que se da importancia a describir que debería pasar en lugar de definir como
tiene que pasar.

Normalmente estamos acostumbrados al estilo de la programación imperativa a la que solo le
importa como conseguir el resultado esperado especificando una secuencia de instrucciones lo que
```tsx
requiere dedicar más tiempo a observar el código para saber que está haciendo. Mientras que con
```
la programación declarativa se intenta que las instrucciones usadas describan lo que ese código
está haciendo sin necesidad de definir un flujo de control.

Veamos un ejemplo de cada una de ellas:

Imperativa

```tsx
var texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho
```
tiempo que vivía un hidalgo...";
```tsx
var textoNuevo = "";

for(var i=0; i < texto.length; i++) {
  if(texto[i] === " ") {
    textoNuevo += "-";
  } else {
    textoNuevo += texto[i];
  }
}

console.log(textoNuevo);
```
Declarativa

```tsx
var texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho
```
tiempo que vivía un hidalgo...";
```tsx
var textoNuevo = texto.replace(/ /g, "-");

console.log(textoNuevo);
```
Pero ¿qué tiene esto que ver con React?, pues la forma en que se construye el DOM.

Imperativa

```tsx
var app = document.getElementById('app');
var contenedor = document.createElement('div');
var titulo = document.createElement('h1');
```
contenedor.id = 'contenedor-saludo';
titulo.innerText = "Hola mundo";

```tsx
contenedor.appendChild(titulo);

app.appendChild(contenedor);
```
Declarativa

```tsx
import { createRoot } from 'react-dom/client';

const HolaMundo = () => (
  <div id="contenedor-saludo">
    <h1>Hola mundo</h1>
  </div>
)

createRoot(document.getElementById('app')).render(<HolaMundo />);
```
React es declarativo, y los componentes describen los elementos del DOM que se deben de
renderizar. Es la función render la que construye el DOM, y abstrae los detalles de como lo va a
renderizar en la aplicación.
